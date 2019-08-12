###Pipeline for thesis.
#For GeneratePBS.py type scripts, need to use python 3.6 - which is available in the snakemake conda environment

PROTOCOLS - all protocols for setting up and running pipeline

MAPPING - scripts for mapping FASTQs

VARIANT_CALLING - scripts for obtaining individual and group gvcfs from bcftools and gatk, and individual gvcfs from platypus
#Generate_union_PBS.py - create union of variant PBS for bcftools and platypus for the individually called vcfs.
#gatk_GenotypeVCFs_all.py - genotype all gatk gvcfs together

VARIANT_ANNOTATION - scripts for running SnpEff, Ensembl-VEP and ANNOVAR

GENETIC_BURDEN - scripts for running the genetic burden pipeline

VARIANT_PRIORITIZATION - scripts for prioritizing each of the diseases for investigation
TRANSFERRING_DATA - scripts for transferring data from interval bio to MSI
