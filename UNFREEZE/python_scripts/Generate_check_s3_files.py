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
            "-b", "--bucket",
            default=argparse.SUPPRESS,
            metavar="",
            required=True,
            help="bucket that needs to be investigated [required]")

    return parser


if __name__ == '__main__':
     
    parser = make_arg_parser()
    args = parser.parse_args()

    data = os.path.abspath(args.data)
    horse_ids = os.path.abspath(args.ids)
    buck = args.bucket

    s3cmd = "/usr/bin/s3cmd  --config /home/mccuem/shared/.local/.s3cfg"
    
    header = (
              "#!/bin/bash -l\n"  
              "#PBS -l nodes=1:ppn=4,walltime=06:00:00,mem=4g\n"
              "#PBS -m abe\n"
              "#PBS -M durwa004@umn.edu\n"
              f"#PBS -o $PBS_JOBID.s3cmd_check.out\n"
              f"#PBS -e $PBS_JOBID.s3cmd_check.err\n"
              f"#PBS -N s3cmd_check.pbs\n"
              "#PBS -q small\n"
             )
    
    tmp = []
    with open(horse_ids) as ids:
        for line in ids:
            tmp.append(line.strip())
    
    pbs = os.path.join(os.getcwd(),f"s3cmd_check.pbs")
    
    with open(pbs, "w") as f:
        print(header, file=f)
        print(f"cd {data}\n", file=f)
        for i in tmp:
            print(f"path='{s3cmd} ls s3://{buck}/" + i + "/" + i + ".bcftools.vcf.gz'\n"
                + "count=`$path | wc -l`\nif [[ $count -gt 0 ]]; then echo 'exist';"
                + f"else echo 'missing " + i + ".bcftools.vcf.gz'; fi\n"
                + f"path='{s3cmd} ls s3://{buck}/" + i + "/" + i + ".bcftools.vcf.gz.tbi\'n"
                + "count=`$path | wc -l`\nif [[ $count -gt 0 ]]; then echo 'exist';"
                + f"else echo 'missing " + i + ".bcftools.vcf.gz.tbi'; fi\n"
                + f"path='{s3cmd} ls s3://{buck}/" + i + "/" + i + ".gatk.gvcf.gz'\n"
                + "count=`$path | wc -l`\nif [[ $count -gt 0 ]]; then echo 'exist';"
                + f"else echo 'missing " + i + ".gatk.gvcf.gz'; fi\n"
                + f"path='{s3cmd} ls s3://{buck}/" + i + "/" + i + ".gatk.gvcf.gz.tbi'\n"
                + "count=`$path | wc -l`\nif [[ $count -gt 0 ]]; then echo 'exist';"
                + f"else echo 'missing " + i + ".gatk.gvcf.gz.tbi'; fi\n"
                + f"path='{s3cmd} ls s3://{buck}/" + i + "/" + i + ".platypus.vcf.gz'\n"
                + "count=`$path | wc -l`\nif [[ $count -gt 0 ]]; then echo 'exist';"
                + f"else echo 'missing " + i + ".platypus.vcf.gz'; fi\n"
                + f"path='{s3cmd} ls s3://{buck}/" + i + "/" + i + ".platypus.vcf.gz.tbi'\n"
                + "count=`$path | wc -l`\nif [[ $count -gt 0 ]]; then echo 'exist';"
                + f"else echo 'missing " + i + ".platypus.vcf.gz.tbi'; fi\n"
                + f"path='{s3cmd} ls s3://{buck}/" + i + "/" + i + ".recalibrated.bam'\n"
                + "count=`$path | wc -l`\nif [[ $count -gt 0 ]]; then echo 'exist';"
                + f"else echo 'missing " + i + ".recalibrated.bam'; fi\n"
                + f"path='{s3cmd} ls s3://{buck}/" + i + "/" + i + ".recalibrated.bai'\n"
                + "count=`$path | wc -l`\nif [[ $count -gt 0 ]]; then echo 'exist';"
                + f"else echo 'missing " + i + ".recalibrated.bai'; fi\n"
                + f"path='{s3cmd} ls s3://{buck}/" + i + "/unmapped.fq.gz'\n" 
                + "count=`$path | wc -l`\nif [[ $count -gt 0 ]]; then echo 'exist';"
                + f"else echo 'missing " + i + ".unmapped.fq.gz'; fi\n"
                + f"path='{s3cmd} ls s3://{buck}/" + i + "/fastqc/'\n" 
                + "count=`$path | wc -l`\nif [[ $count -gt 0 ]]; then echo 'exist';"
                + f"else echo 'missing " + i + "fastqc'; fi\n"
                + f"path='{s3cmd} ls s3://{buck}/" + i + "/metrics/'\n"
                + "count=`$path | wc -l`\nif [[ $count -gt 0 ]]; then echo 'exist';"
                + f"else echo 'missing " + i + ".metrics'; fi\n"
                + f"path='{s3cmd} ls s3://{buck}/" + i + "/unpaired/'\n"
                + "count=`$path | wc -l`\nif [[ $count -gt 0 ]]; then echo 'exist';"
                + f"else echo 'missing " + i + "unpaired'; fi", file=f, sep="")
