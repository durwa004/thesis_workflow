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
            "-c", "--chrs",
            default=argparse.SUPPRESS,
            metavar="",
            required=True,
            help="Path to directory containing group vcfs from bcftools call[required]")
    parser.add_argument(
            "-p", "--prog",
            default=argparse.SUPPRESS,
            metavar="",
            required=True,
            help="output gvcf type e.g. bcftools/gatk [required]")
    return parser


if __name__ == '__main__':
     
    parser = make_arg_parser()
    args = parser.parse_args()

    chr_ids = os.path.abspath(args.chrs)
    program = args.prog
    i = "${i}"

    print(f"Using {program}")

    header = (
              "#!/bin/bash -l\n"  
              "#PBS -l nodes=1:ppn=12,walltime=48:00:00,mem=12g\n"
              "#PBS -m abe\n"
              "#PBS -M durwa004@umn.edu\n"
              f"#PBS -o $PBS_JOBID.{program}_bgzip_tabix_joint.out\n"
              f"#PBS -e $PBS_JOBID.{program}_bgzip_tabix_joint.err\n"
              f"#PBS -N {program}_bgzip_tabix_joint.pbs\n"
              "#PBS -q small\n"
             )
    
    tmp = []
    for file_name in os.listdir(chr_ids):
        if file_name.endswith(".gz"):
            a = file_name.split(".genotyped.vcf.gz")
            tmp.append(a[0])
    
    pbs = os.path.join(os.getcwd(), f"{program}_bgzip_tabix_joint.pbs")
    
    with open(pbs, "w") as f:
        print(header, file=f)
        print(f"cd {chr_ids}\n", file=f)
        print("for i in ", " ".join(tmp), "; do "
             + f"/panfs/roc/msisoft/htslib/1.6/bin/bgzip ",i,".genotyped.vcf.gz && "
             + f"/home/mccuem/shared/.local/conda/envs/HorseGenomeProject/bin/svtoolkit_2.00.1833/svtoolkit/tabix -p vcf ",i,".genotyped.vcf.gz.gz; done", file=f,sep="")
