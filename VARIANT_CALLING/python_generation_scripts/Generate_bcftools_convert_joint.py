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
    return parser


if __name__ == '__main__':
     
    parser = make_arg_parser()
    args = parser.parse_args()

    data = os.path.abspath(args.data)
    chr_ids = os.path.abspath(args.chrs)
    
    ref = "/home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files/GCF_002863925.1_EquCab3.0_genomic/GCF_002863925.1_EquCab3.0_genomic.fna"
 
    print(f"Using bcftools with equine reference {ref}")

    header = (
              "#!/bin/bash -l\n"  
              "#PBS -l nodes=1:ppn=12,walltime=48:00:00,mem=12g\n"
              "#PBS -m abe\n"
              "#PBS -M durwa004@umn.edu\n"
              "#PBS -o $PBS_JOBID.bcftools_convert_joint.out\n"
              "#PBS -e $PBS_JOBID.bcftools_convert_joint.err\n"
              "#PBS -N bcftools_convert_joint.pbs\n"
              "#PBS -q small\n"
              "module load bcftools\n"
             )
    
    tmp = []
    for file_name in os.listdir(chr_ids):
        if file_name.endswith(".tbi"):
            a = file_name.split(".gvcf.gz.tbi")
            tmp.append(a[0])
    
    pbs = os.path.join(os.getcwd(), "bcftools_convert_joint.pbs")
    
    with open(pbs, "w") as f:
        print(header, file=f)
        print(f"cd {chr_ids}\n", file=f)
        print("for i in ", " ".join(tmp), "; do "
             + "bcftools convert ${i}.gvcf.gz --gvcf2vcf " 
             + f"-f {ref}"
             + "  -o bcftools_joint_genotyped/${i}.genotyped.vcf.gz; done", file=f)
