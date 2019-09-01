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
    return parser


if __name__ == '__main__':
     
    parser = make_arg_parser()
    args = parser.parse_args()

    data = os.path.abspath(args.data)
    
    gatk = "/home/mccuem/shared/.local/conda/envs/HorseGenomeProject/bin/gatk/gatk"
    java = '--java-options "-Xmx4g"'
    ref = "/home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files/GCF_002863925.1_EquCab3.0_genomic/GCF_002863925.1_EquCab3.0_genomic.fna"

 
    print(f"Using {gatk}\nwith equine reference {ref}")

    header = (
              "#!/bin/bash -l\n"  
              "#PBS -l nodes=1:ppn=12,walltime=48:00:00,mem=12g\n"
              "#PBS -m abe\n"
              "#PBS -M durwa004@umn.edu\n"
              "#PBS -o $PBS_JOBID.gatk_genotypegvcfs.out\n"
              "#PBS -e $PBS_JOBID.gatk_genotypegvcfs.err\n"
              "#PBS -N gatk_genotypegvcfs.pbs\n"
              "#PBS -q small\n"
             )
    
    tmp = []
    for file_name in os.listdir(data/bcftools_joint/):
        if file_name.endswith(".tbi"):
            a = file_name.split(".gvcf.gz.tbi")
            tmp.append(a[0])
    
    pbs = os.path.join(os.getcwd(), "gatk_genotypegvcfs_joint.pbs")
    
    with open(pbs, "w") as f:
        print(header, file=f)
        print(f"cd {chr_ids}\n", file=f)
        print("for i in ", " ".join(tmp), "; do ", file=f, sep = "")
        print(f"{gatk} {java}" 
              + " GenotypeGVCFs -R "
              + f"{ref} \\"
              + "-V ${i}.gvcf.gz", file=f)
        print(" -o gatk_joint_genotyped/${i}.genotyped.vcf.gz -nt 4; done", file=f)
        
