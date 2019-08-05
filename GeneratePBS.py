#!/usr/bin/env python3
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
            "-i", "--ids",
            default=argparse.SUPPRESS,
            metavar="",
            required=True,
            help="Text file containing horse ids - one per line [required]")
    
    return parser


if __name__ == '__main__':
     
    parser = make_arg_parser()
    args = parser.parse_args()

    data = os.path.abspath(args.data)
    horse_ids = os.path.abspath(args.ids)

    gatk = "/home/mccuem/shared/.local/conda/envs/HorseGenomeProject/bin/GenomeAnalysisTK.jar"
    ref = "/home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/NCBI_reference/GCF_002863925.1_EquCab3.0_genomic.fna"
    
    print(f"Using {gatk}\nwith equine reference {ref}")

    header = (
              "#!/bin/bash -l\n"  
              "#PBS -l nodes=1:ppn=12,walltime=48:00:00,mem=12g\n"
              "#PBS -m abe\n"
              "#PBS -M durwa004@umn.edu\n"
              "#PBS -o $PBS_JOBID.union_platypus.out\n"
              "#PBS -e $PBS_JOBID.union_platypus.err\n"
              "#PBS -N union_platypus.pbs\n"
              "#PBS -q small\n"
             )
    
    tmp = []
    with open(horse_ids) as ids:
        for line in ids:
            tmp.append(line.strip())
    
    pbs = os.path.join(os.getcwd(),"union_platypus.pbs")
    
    with open(pbs, "w") as f:
        print(header, file=f)
        print(f"cd {data}\n", file=f)
        print(f"java -Xmx4g -jar {gatk}" 
              + " -T CombineVariants -R "
              + f"{ref} \\", file=f)
    
        for i in tmp:
            print(f"  --variant:{i} " 
                  + f"./ibio_output_files/{i}/{i}.platypus.vcf.gz \\", file=f)
        print("  -o AFIB_cases_PL.vcf.gz -nt 4", file=f)
        

        
