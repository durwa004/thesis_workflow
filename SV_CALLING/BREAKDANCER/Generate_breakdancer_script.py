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
    parser.add_argument(
            "-b", "--breed",
            default=argparse.SUPPRESS,
            metavar="",
            required=True,
            help="What breed group do the horses belong to? [required]")    
    return parser


if __name__ == '__main__':
     
    parser = make_arg_parser()
    args = parser.parse_args()

    data = os.path.abspath(args.data)
    horse_ids = os.path.abspath(args.ids)
    breed = args.breed

    header = (
              "#!/bin/bash -l\n"  
              "#PBS -l nodes=1:ppn=12,walltime=48:00:00,mem=12g\n"
              "#PBS -m abe\n"
              "#PBS -M durwa004@umn.edu\n"
              f"#PBS -o $PBS_JOBID.{breed}.breakdancer.out\n"
              f"#PBS -e $PBS_JOBID.{breed}.breakdancer.err\n"
              f"#PBS -N {breed}.breakdancer.pbs\n"
              "#PBS -q small\n"
             )
    
    tmp = []
    with open(horse_ids) as ids:
        for line in ids:
            tmp1 = line.strip()
            tmp2 = "./ibio_output_files/" + tmp1 + "/" + tmp1 + ".recalibrated.bam"
            tmp.append(tmp2)
    
    pbs = os.path.join(os.getcwd(),f"{breed}.breakdancer.pbs")
    
    with open(pbs, "w") as f:
        print(header, file=f)
        print(f"cd {data}\n", file=f)
        print("#Create config file\n/home/mccuem/durwa004/.conda/envs/breakdancer/bin/bam2cfg.pl "
        + " ".join(tmp)
        + f" > ibio_{breed}_breakdancer.cfg", file=f)
        print("\n\n#Run Breakdancer", file=f)
        print(f"/home/mccuem/shared/.local/conda/envs/HorseGenomeProject/bin/breakdancer/bin/breakdancer -q 10 ibio_{breed}_breakdancer.cfg > ibio_{breed}_breakdancer",file=f)
