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
            "-i", "--ids",
            default=argparse.SUPPRESS,
            metavar="",
            required=True,
            help="Text file containing horse ids - one per line [required]")
    parser.add_argument(
            "-c", "--chrom",
            default=argparse.SUPPRESS,
            metavar="",
            required=True,
            help="Text file containing chromosomes for analysis - one per line [required]")
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

    horse_ids = os.path.abspath(args.ids)
    chr_ids = os.path.abspath(args.chrom)
    breed = args.breed

    header = (
              "#module load R/3.5.0\n"
              "library(cn.mops)\n"
             )
    
    tmp = []
    tmp_id = []
    with open(horse_ids) as ids:
        for line in ids:
            tmp1 = line.strip()
            tmp2 = '"./ibio_output_files/' + tmp1 + '/' + tmp1 + '.recalibrated.bam"'
            tmp3 = '"' + tmp1 + '"'
            tmp.append(tmp2)
            tmp_id.append(tmp3)

    chr_tmp = [] 
    with open(chr_ids) as chroms:
        for line in chroms:
            chr_tmp1 = line.strip()
            chr_tmp2 = '"' + chr_tmp1 + '"'
            chr_tmp.append(chr_tmp2)

    pbs = os.path.join(os.getcwd(),f"cn.mops.{breed}.R")
    
    with open(pbs, "w") as f:
        print(header, file=f)
        print("BAMFiles <- c("
        + ", ".join(tmp)
        + ")", file=f)
        print("RefSeqNames = c("
        + ", ".join(chr_tmp)
        + ")", file=f)
        print("sampleNames = c("
        + ", ".join(tmp_id)
        + ")", file=f)
        print("bamDataRanges <- getReadCountsFromBAM(BAMFiles,sampleNames, RefSeqNames, WL = 5000, parallel=4)",file=f)
        print("res <- cn.mops(bamDataRanges)",file=f)
        print("#Calculate integer copy numbers", file=f)
        print("results <- calcIntegerCopyNumbers(res)",file=f)
        print("segm <- as.data.frame(segmentation(results))",file=f)
        print("#Identify CNVs", file=f)
        print("CNVs <- as.data.frame(cnvs(results))", file=f)
        print("#Identify CNV regions", file=f)
        print("CNVRegions <- as.data.frame(cnvr(results))",file=f)
        print("#Output data",file=f)
        print(f"write.csv(segm,file='ibio_{breed}_segmentation.csv')",file=f)
        print(f"write.csv(CNVs,file='ibio_{breed}_CNVs.csv')",file=f)
        print(f"write.csv(CNVRegions,file='ibio_{breed}_CNVR.csv')",file=f)

