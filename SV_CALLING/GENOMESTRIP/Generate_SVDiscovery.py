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
    breed = args.breed
    
    header = (
              "#!/bin/bash -l\n"  
              "#PBS -l nodes=1:ppn=12,walltime=48:00:00,mem=12g\n"
              "#PBS -m abe\n"
              "#PBS -M durwa004@umn.edu\n"
              f"#PBS -o $PBS_JOBID.{breed}.SVDiscovery.out\n"
              f"#PBS -e $PBS_JOBID.{breed}.SVDiscovery.err\n"
              f"#PBS -N {breed}.SVDiscovery.pbs\n"
              "#PBS -q small\n\n"
              "source ~/.genomestrip_bashrc"
             )
    
    pbs = os.path.join(os.getcwd(),f"{breed}.genomestrip.SVDiscovery.pbs")
    
    with open(pbs, "w") as f:
        print(header, file=f)
        print(f"cd {data}\n", file=f)
        print(f"runDir={data}/SVDiscovery", file=f)
        print("java -Xmx2g -cp ${SV_CLASSPATH} \\"
        + "    org.broadinstitute.gatk.queue.QCommandLine \\"
        + "    -S ${SV_DIR}/qscript/SVPreprocess.q \\"
        + "    -S ${SV_DIR}/qscript/SVQScript.q \\"
        + "    -cp ${SV_CLASSPATH} \\"
        + "    -gatk ${SV_DIR}/lib/gatk/GenomeAnalysisTK.jar \\"
        + "    -configFile ${SV_DIR}/conf/genstrip_parameters.txt \\"
        + "    -tempDir ${SV_TMPDIR} \\"
        + "    -R ${runDir}/../References/GCF_002863925.1_EquCab3.0_genomic.fasta \\"
        + "    -runDirectory ${runDir} \\"
        + "    -md ${runDir}/../SVPreprocessing/metadata \\"
        + "    -I {data}/genomestrip_{breed}.list \\"
        + "    -minimumSize 100 \\"
        + "    -maximumSize 100000 \\"
        + "    -jobLogDir ${runDir}/logs \\"
        + "    -genderMaskBedFile ${runDir}../References/GCF_002863925.1_EquCab3.0_genomic.gendermask.bed \\"
        + "    -ploidyMapFile ${runDir}../References/GCF_002863925.1_EquCab3.0_genomic.ploidymap.txt \\"
        + "    -copyNumberMaskFile ${runDir}../References/GCF_002863925.1_EquCab3.0_genomic.gcmask.fasta \\"
        + "    -genomeMaskFile ${runDir}../References/GCF_002863925.1_EquCab3.0_genomic.svmask.fasta \\"
        + "    -readDepthMaskFile ${runDir}../References/GCF_002863925.1_EquCab3.0_genomic.rdmask.bed \\"
        + "    -rmd ${runDir}../References/ \\"
        + "    -O ${runDir}/ibio_" + breed + "_genomestrip.dels.vcf \\"
        + "    -jobRunner Drmaa \\"
        + "      -gatkJobRunner Drmaa \\"
        + "      -jobQueue mcqueue \\"
        + "      -memLimit 10 \\"
        + '        -jobNative "-l nodes=1:ppn=4,walltime=02:00:00,mem=2gb" \\'
        + '        -jobWrapperScript "source ~/.genomestrip_bashrc &&" \\'
        + "    -maxConcurrentRun 6 \\"
        + "    -run", file=f)
