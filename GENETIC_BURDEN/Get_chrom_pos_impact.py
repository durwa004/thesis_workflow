#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 11:04:17 2019

@author: jonahcullen
"""

import argparse
import os
import gzip

def make_arg_parser():
    parser = argparse.ArgumentParser(
            prog="GeneratePBS.py",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
            "-d", "--data",
            default=argparse.SUPPRESS,
            metavar="",
            required=True,
            help="Path to dir containing the ibio intersect by chromosome files [required]")
    parser.add_argument(
            "-p", "--prog",
            default=argparse.SUPPRESS,
            metavar="",
            required=True,
            help="Path to dir containing the ibio intersect/union by chromosome files [required]")
    return parser


if __name__ == '__main__':
     
    parser = make_arg_parser()
    args = parser.parse_args()

    data = os.path.abspath(args.data)
    program = args.prog

    impact = data + "/" + program + "/" + program + "_chrom_pos_impact.txt"

    with open(impact, "w") as output_file:
        count_high = 0
        count_mod = 0
        count_low = 0
        count_modifier = 0
        count_unknown = 0
        print("CHROM\tPOS\tIMPACT", file= output_file)
        if program == "SnpEff":
            for file_name in os.listdir(data + "/" +  program):
                if file_name.endswith(".vcf.gz"):
                    with gzip.open(data + "/" + program + "/" + file_name,"rt") as snpeff:
                        for line in snpeff:
                            line = line.rstrip("\n").split("\t")
                            if "#" in line[0]:
                                next
                            else:
                                 if "HIGH" in line[7]: 
                                     count_high +=1
                                     print(line[0],line[1], "HIGH", file = output_file, sep = "\t")
                                 elif "MODERATE" in line[7]:
                                     count_mod +=1
                                     print(line[0],line[1], "MODERATE", file = output_file, sep = "\t")
                                 elif "LOW" in line[7]:
                                     count_low +=1
                                     print(line[0],line[1], "LOW", file = output_file, sep = "\t")
                                 elif "MODIFIER" in line[7]:
                                     count_modifier +=1
                                     print(line[0],line[1], "MODIFIER", file = output_file, sep = "\t")
                                 else:
                                     count_unknown +=1
                                     print(line[0],line[1], "UNKNOWN", file = output_file, sep = "\t")
            print(f"{file_name} {program}\nhigh impact: {count_high}\nmoderate impact: {count_mod}\nlow impact: {count_low}\nunknown impact: {count_unknown}")
        elif program == "annovar":
            for file_name in os.listdir(data + "/" +  program):
                if file_name.endswith(".exonic_variant_function"):
                    with open(data + "/" + program + "/" + file_name,"r") as annovar:
                        for line in annovar:
                            line = line.rstrip("\n").split("\t")
                            if "frameshift" in line[1] or "stopgain" in line[1] or "stoplost" in line[1]:
                                count_high +=1
                                print(line[3],line[4], "HIGH", file = output_file, sep = "\t")
                            elif "nonframeshift" in line[1] or "nonsynonymous" in line[1]:
                                count_mod +=1
                                print(line[3],line[4], "MODERATE", file = output_file, sep = "\t")
                            elif "synonymous SNV" in line[1]:
                                count_low +=1
                                print(line[3],line[4], "LOW", file = output_file, sep = "\t")
                            elif "unknown" in line[1]:
                                count_unknown +=1
                                print(line[3],line[4], "MODIFIER", file = output_file, sep = "\t")
                            else:
                                count_unknown +=1
                                print(line[3],line[4], "UNKNOWN", file = output_file, sep = "\t")
            print(f"{file_name} {program}\nhigh impact: {count_high}\nmoderate impact: {count_mod}\nlow impact: {count_low}\nmodifier {count_modifier}\nunknown impact: {count_unknown}")
