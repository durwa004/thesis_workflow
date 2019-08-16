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
              f"#PBS -o $PBS_JOBID.{breed}.SCVNV_high.out\n"
              f"#PBS -e $PBS_JOBID.{breed}.SCVNV_high.err\n"
              f"#PBS -N {breed}.SCVNV_high.pbs\n"
              "#PBS -q small\n\n"
              "source ~/.genomestrip_bashrc\n"
              "export OMP_NUM_THREADS=1"
             )
    
    pbs = os.path.join(os.getcwd(),f"{breed}.genomestrip.SCVNV_high.pbs")
    
    with open(pbs, "w") as f:
        print(header, file=f)
        print(f"cd {data}\n", file=f)
        print(f"runDir={data}/SCVNV_high", file=f)
        print("java -Xmx12g -cp ${SV_CLASSPATH} \\"
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
        + "    -tilingWindowSize 1000 \\"
        + "    -tilingWindowOverlap 500 \\"
        + "    -maximumReferenceGapLength 1000 \\"
        + "    -boundaryPrecision 100 \\"
        + "    -minimumRefinedLength 500 \\"
        + "    -jobLogDir ${runDir}/logs \\"
        + "    -genderMaskBedFile ${runDir}../References/GCF_002863925.1_EquCab3.0_genomic.gendermask.bed \\"
        + "    -ploidyMapFile ${runDir}../References/GCF_002863925.1_EquCab3.0_genomic.ploidymap.txt \\"
        + "    -copyNumberMaskFile ${runDir}../References/GCF_002863925.1_EquCab3.0_genomic.gcmask.fasta \\"
        + "    -genomeMaskFile ${runDir}../References/GCF_002863925.1_EquCab3.0_genomic.svmask.fasta \\"
        + "    -readDepthMaskFile ${runDir}../References/GCF_002863925.1_EquCab3.0_genomic.rdmask.bed \\"
        + "    -intervalListi ${runDir}../References/GCF_002863925.1_EquCab3.0_genomic_exc_chrUn.list \\"
        + "    -rmd ${runDir}../References/ \\"
        + "    -jobRunner Drmaa \\"
        + "      -gatkJobRunner Drmaa \\"
        + "      -jobQueue mcqueue \\"
        + "      -memLimit 10 \\"
        + '        -jobNative "-l nodes=1:ppn=6,walltime=10:00:00,mem=20gb" \\'
        + '        -jobWrapperScript "source ~/.genomestrip_bashrc &&" \\'
        + "    -maxConcurrentRun 20 \\"
        + "    -run", file=f)
