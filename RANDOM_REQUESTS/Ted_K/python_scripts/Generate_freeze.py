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
    
    s3cmd = "/usr/bin/s3cmd  --config /home/mccuem/shared/.local/.s3cfg"

    tmp = []
    for file_name in os.listdir(f"{data}"):
        if file_name.endswith(".updated.gvcf.gz"):
            a = file_name.rstrip("\n").split(".updated.gvcf.gz")
            pbs = os.path.join(os.getcwd(), "freeze_" + a[0] + ".pbs")
            header = (
                  "#!/bin/bash -l\n"
                  "#PBS -l nodes=1:ppn=4,walltime=48:00:00,mem=4g\n"
                  "#PBS -m abe\n"
                  "#PBS -M durwa004@umn.edu\n"
                  f"#PBS -o $PBS_JOBID.freeze_" + a[0] + ".out\n"
                  f"#PBS -e $PBS_JOBID.freeze_" + a[0] + ".err\n"
                  f"#PBS -N freeze_" + a[0] + ".pbs\n"
                  "#PBS -q small\n"
                 )
            with open(pbs, "w") as f:
                print(header, file=f)
                print(f"cd {data}/\n", file=f)
                print(f"{s3cmd} put {file_name} s3://durwa004/ibio_updated_gvcfs/ "
                      + f"&& {s3cmd} put {file_name}.tbi s3://durwa004/ibio_updated_gvcfs/",file=f,sep="") 
