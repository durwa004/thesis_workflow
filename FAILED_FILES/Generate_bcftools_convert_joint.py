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
            "-c", "--chrs",
            default=argparse.SUPPRESS,
            metavar="",
            required=True,
            help="Path to directory containing group gvcfs [required]")
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

    data = os.path.abspath(args.data)
    chr_ids = os.path.abspath(args.chrs)
    program = args.prog
    i = "${i}"

    print(f"Using {program}")

    header = (
              "#!/bin/bash -l\n"  
              "#PBS -l nodes=1:ppn=12,walltime=48:00:00,mem=12g\n"
              "#PBS -m abe\n"
              "#PBS -M durwa004@umn.edu\n"
              f"#PBS -o $PBS_JOBID.{program}_convert_joint.out\n"
              f"#PBS -e $PBS_JOBID.{program}_convert_joint.err\n"
              f"#PBS -N {program}_convert_joint.pbs\n"
              "#PBS -q small\n"
              "module load bcftools\n"
             )
    
    tmp = []
    for file_name in os.listdir(chr_ids):
        if file_name.endswith(".tbi"):
            a = file_name.split(".gvcf.gz.tbi")
            tmp.append(a[0])
    
    pbs = os.path.join(os.getcwd(), f"{program}_convert_joint.pbs")
    
    with open(pbs, "w") as f:
        print(header, file=f)
        print(f"cd {chr_ids}\n", file=f)
        print("for i in ", " ".join(tmp), "; do "
             + "bcftools view ${i}.gvcf.gz -g hom -g het" 
             + f" -o {program}_joint_genotyped/",i,".genotyped.vcf\n"
             + f"/home/mccuem/shared/.local/conda/envs/HorseGenomeProject/bin/svtoolkit_2.00.1833/svtoolkit/bgzip {program}_joint_genotyped/",i,".genotyped.vcf\n"
             + f"/home/mccuem/shared/.local/conda/envs/HorseGenomeProject/bin/svtoolkit_2.00.1833/svtoolkit/tabix {program}_joint_genotyped/",i,".genotyped.vcf.gz; done", file=f,sep="")
