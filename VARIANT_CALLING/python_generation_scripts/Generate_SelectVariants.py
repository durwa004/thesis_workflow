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
            "-p", "--prog",
            default=argparse.SUPPRESS,
            metavar="",
            required=True,
            help="Program that created the gvcfs [required]")
    return parser


if __name__ == '__main__':
     
    parser = make_arg_parser()
    args = parser.parse_args()

    data = os.path.abspath(args.data)
    prog = args.prog
    
    source = "source /home/mccuem/shared/.local/conda/bin/activate gatk4_4.1.0"
    java = '--java-options "-Xmx4g"'
    ref = "/home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files/GCF_002863925.1_EquCab3.0_genomic/GCF_002863925.1_EquCab3.0_genomic.fna"
    select = "--select-type-to-include SNP --select-type-to-include INDEL --select-type-to-include MNP"
 
    print(f"Using {source}\nwith equine reference {ref}")

    tmp = []
    for file_name in os.listdir(data + f"/joint_{prog}/"):
        if file_name.endswith(".tbi"):
            a = file_name.split(".gvcf.gz.tbi")
            tmp.append(a[0])
   

    for i in tmp:
        pbs = os.path.join(os.getcwd(), f"{prog}_selectvariants_joint_" + i + ".pbs")
        header = (
              "#!/bin/bash -l\n"
              "#PBS -l nodes=1:ppn=4,walltime=48:00:00,mem=4g\n"
              "#PBS -m abe\n"
              "#PBS -M durwa004@umn.edu\n"
              f"#PBS -o $PBS_JOBID.{prog}_selectvariants_joint_" + i + ".out\n"
              f"#PBS -e $PBS_JOBID.{prog}_selectvariants_joint_" + i + ".err\n"
              f"#PBS -N {prog}_selectvariants_joint_" + i + ".pbs\n"
              "#PBS -q small\n"
              f"{source}\n"
                 )
        with open(pbs, "w") as f:
            print(header, file=f)
            print(f"cd {data}/joint_{prog}\n", file=f)
            print(f"gatk {java}"
                  + " SelectVariants -R "
                  + f"{ref} {select} "
                  + f"-V " + i + ".gvcf.gz -O " + i + ".genotyped.vcf.gz", file=f, sep="")
