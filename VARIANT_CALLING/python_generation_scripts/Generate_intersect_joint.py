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
    
    source = "source /home/mccuem/shared/.local/conda/bin/activate gatk4_4.1.0"
    java = '--java-options "-Xmx4g"'
    ref = "/home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files/GCF_002863925.1_EquCab3.0_genomic/GCF_002863925.1_EquCab3.0_genomic.fna"
    select = "--interval-set-rule INTERSECTION"
 
    print(f"Using {source}\nwith equine reference {ref}")

    tmp = []
    for file_name in os.listdir(data + f"/joint_union/"):
        if file_name.endswith("_union_joint.vcf.gz"):
            a = file_name.split("_union_joint.vcf.gz")
            tmp.append(a[0])

    for i in tmp:
        pbs = os.path.join(os.getcwd(), f"intersect_joint_" + i + ".pbs")
        header = (
              "#!/bin/bash -l\n"
              "#PBS -l nodes=1:ppn=4,walltime=48:00:00,mem=4g\n"
              "#PBS -m abe\n"
              "#PBS -M durwa004@umn.edu\n"
              "#PBS -o $PBS_JOBID.intersect_joint_" + i + ".out\n"
              "#PBS -e $PBS_JOBID.intersect_joint_" + i + ".err\n"
              "#PBS -N intersect_joint_" + i + ".pbs\n"
              "#PBS -q small\n"
              f"{source}\n"

                 )
        with open(pbs, "w") as f:
            print(header, file=f)
            print(f"cd {data}/\n", file=f)
            print(f"gatk {java}"
                  + " SelectVariants -R "
                  + f"{ref} "
                  + "-V joint_union/" + i + "_union_joint.vcf.gz -O joint_intersect/" + i + "_intersect_joint.vcf.gz --select 'set == "
                  +'"Intersection";'
                  + "'", file=f, sep="")
