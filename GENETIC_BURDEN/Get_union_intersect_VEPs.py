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
    return parser


if __name__ == '__main__':
     
    parser = make_arg_parser()
    args = parser.parse_args()

    data = os.path.abspath(args.data)

    union = data + "/union_SnpEff_annovar.txt"

    with open(union,"w") as union_file:
        count_union = 0
        count_intersect = 0
        with open("SnpEff/SnpEff_chrom_pos_impact.txt", "r") as SnpEff:
            SnpEff_chrom_pos = []
            SnpEff_impact = []
            SnpEff.readline()
            for line in SnpEff:
                line = line.rstrip("\n").split("\t")
                if "NW_" in line[0] or line[0] == "NC_001640.1":
                    continue
                else:
                    a = line[0] + ":" + line[1]
                    SnpEff_chrom_pos.append(a)
                    SnpEff_impact.append(line[2])
        with open("annovar/annovar_chrom_pos_impact.txt", "r") as annovar:
             annovar_chrom_pos = [] 
             annovar_impact = []
             annovar.readline()
             for line in annovar:
                 line = line.rstrip("\n").split("\t")
                 if "NW_" in line[0] or line[0] == "NC_001640.1":
                     continue
                 else:
                     b = line[0] + ":" + line[1]
                     annovar_chrom_pos.append(b)
                     annovar_impact.append(line[2])
        annovar_high = []
        annovar_mod = [] 
        annovar_low = []
        SnpEff_high = []
        SnpEff_mod = []
        SnpEff_low = []
        for i in range(len(annovar_impact)):
            if annovar_impact[i] == "HIGH":
                annovar_high.append(annovar_chrom_pos[i])
            elif annovar_impact[i] == "MODERATE":
                annovar_mod.append(annovar_chrom_pos[i])
            elif annovar_impact[i] == "LOW":
                annovar_low.append(annovar_chrom_pos[i])
        for i in range(len(SnpEff_impact)):
            if SnpEff_impact[i] == "HIGH":
                SnpEff_high.append(SnpEff_chrom_pos[i])
            elif SnpEff_impact[i] == "MODERATE":
                SnpEff_mod.append(SnpEff_chrom_pos[i])
            elif SnpEff_impact[i] == "LOW":
                SnpEff_low.append(SnpEff_chrom_pos[i])
        #Get union
        union_high = list(set(annovar_high + SnpEff_high))
        union_mod = list(set(annovar_mod + SnpEff_mod))
        union_low = list(set(annovar_low + SnpEff_low))
        #Get intersect
        intersect_high = list(set(annovar_high) & set(SnpEff_high))
        intersect_mod = list(set(annovar_mod) & set(SnpEff_mod))
        intersect_low = list(set(annovar_low) & set(SnpEff_low))
        #output (sorted)
        union_high_sorted = sorted(union_high)
        for i in range(len(union_high_sorted)):
            a = union_high_sorted[i].split(":")
            print(a[0], a[1], file=union_file, sep = "\t")
        
