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
    select = "--exclude-sample-name /home/mccuem/shared/Projects/HorseGenomeProject/scripts/EquCab3/thesis_workflow/RANDOM_REQUESTS/Ted_K/horses_to_exclude.args"
    s3cmd = "/usr/bin/s3cmd  --config /home/mccuem/shared/.local/.s3cfg"
 
    print(f"Using {source}\nwith equine reference {ref}")

    tmp = []
    with open("//home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files/GCF_002863925.1_EquCab3.0_genomic/GCF_002863925.1_EquCab3.0_genomic_NC.fna.bed", "r") as input_f:
        for line in input_f:
            line = line.rstrip("\n").split("\t")
            a,b = line[0].split(".")
            c = a + "_" + b
            tmp.append(c)
   

    for i in tmp:
        pbs = os.path.join(os.getcwd(), "Extract_samples_" + i + ".pbs")
        header = (
              "#!/bin/bash -l\n"
              "#PBS -l nodes=1:ppn=4,walltime=48:00:00,mem=4g\n"
              "#PBS -m abe\n"
              "#PBS -M durwa004@umn.edu\n"
              f"#PBS -o $PBS_JOBID.Extract_samples_" + i + ".out\n"
              f"#PBS -e $PBS_JOBID.Extract_samples_" + i + ".err\n"
              f"#PBS -N Extract_samples_" + i + ".pbs\n"
              "#PBS -q small\n"
              f"{source}\n"
                 )
        with open(pbs, "w") as f:
            print(header, file=f)
            print(f"cd {data}/\n", file=f)
            print(f"{s3cmd} get s3://mccue-lab/ibiodatatransfer2019/joint_gatk/" + i +".gvcf.gz "
                  + f"&& {s3cmd} get s3://mccue-lab/ibiodatatransfer2019/joint_gatk/" + i +".gvcf.gz.tbi\n" 
                  + f"gatk {java}"
                  + " SelectVariants -R "
                  + f"{ref} {select} "
                  + f"-V " + i + ".gvcf.gz -O " + i + ".updated.gvcf.gz", file=f, sep="")
