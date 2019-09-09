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
            help="Path to dir containing the ibio files to be moved to s3 [required]")
    parser.add_argument(
            "-c", "--command",
            default=argparse.SUPPRESS,
            metavar="",
            required=True,
            help="s3cmd command e.g. get, put [required]")
    parser.add_argument(
            "-ft", "--filetype",
            default=argparse.SUPPRESS,
            metavar="",
            required=True,
            help="file type to be extracted e.g. realigned.bam [required]")

    return parser


if __name__ == '__main__':
     
    parser = make_arg_parser()
    args = parser.parse_args()

    data = os.path.abspath(args.data)
    horse_ids = os.path.abspath(args.ids)
    com = args.command
    ft = args.filetype

    s3cmd = "/usr/bin/s3cmd  --config /home/mccuem/shared/.local/.s3cfg"
    
    header = (
              "#!/bin/bash -l\n"  
              "#PBS -l nodes=1:ppn=12,walltime=48:00:00,mem=4g\n"
              "#PBS -m abe\n"
              "#PBS -M durwa004@umn.edu\n"
              f"#PBS -o $PBS_JOBID.s3cmd_{com}.out\n"
              f"#PBS -e $PBS_JOBID.s3cmd_{com}.err\n"
              f"#PBS -N s3cmd_{com}.pbs\n"
              "#PBS -q small\n"
             )
    
    tmp = []
    with open(horse_ids) as ids:
        for line in ids:
            tmp.append(line.strip())
    
    pbs = os.path.join(os.getcwd(),f"s3cmd_{com}.pbs")
    
    with open(pbs, "w") as f:
        print(header, file=f)
        print(f"cd {data}\n", file=f)
        for i in tmp:
            print(f"{s3cmd} {com} s3://mccue-lab/ibiodatatransfer2019/{i}/{i}.{ft}",file=f) 
