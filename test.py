#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 11:04:17 2019

@author: jonahcullen
"""

import argparse
import os


def make_arg_parser():
    parser = argparse.ArgumentParser(
            prog="GeneratePBS.py",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
            "-d", "--data",
            default=argparse.SUPPRESS,
            metavar="",
            required=True,
            help="Path to dir containing the ibio output files [required]")
    parser.add_argument(
            "-v", "--vcf",
            default=argparse.SUPPRESS,
            metavar="",
            required=True,
            help="Location of vcf file for analysis [required]")
    parser.add_argument(
            "-v", "--vcf",
            default=argparse.SUPPRESS,
            metavar="",
            required=True,
            help="Location of vcf file for analysis [required]")
    return parser


if __name__ == '__main__':
     
    parser = make_arg_parser()
    args = parser.parse_args()

    data = os.path.abspath(args.data)
    vcf_file = args.vcf

    gatk = "/home/mccuem/shared/.local/conda/envs/HorseGenomeProject/bin/gatk/gatk"
    java = '--java-options "-Xmx4g"'
    ref = "/home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/NCBI_reference/GCF_002863925.1_EquCab3.0_genomic.fna"
 
    print(f"Using {gatk}\nwith equine reference {ref}")

    header = (
              "#!/bin/bash -l\n"  
              "#PBS -l nodes=1:ppn=12,walltime=48:00:00,mem=12g\n"
              "#PBS -m abe\n"
              "#PBS -M durwa004@umn.edu\n"
              f"#PBS -o $PBS_JOBID.gatk_intersect.out\n"
              f"#PBS -e $PBS_JOBID.gatk_intersect.err\n"
              f"#PBS -N gatk_intersect.pbs\n"
              "#PBS -q small\n"
             )
    
    pbs = os.path.join(os.getcwd(), f"gatk_intersect.pbs")
    
    with open(pbs, "w") as f:
        print(header, file=f)
        print(f"cd {data}\n", file=f)
        print(f"{gatk} {java}" 
              + f" {prog} -R "
              + f"{ref} \\"
              + "  -V "
              + f"{vcf_file} \\"
              + f" -o ibio_all_intersect.vcf.gz -nt 4", file=f)
