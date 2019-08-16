###Pipeline for thesis.
#For GeneratePBS.py type scripts, need to use python 3.6 - which is available in the snakemake conda environment

PROTOCOLS - all protocols for setting up and running pipeline

MAPPING - scripts for mapping FASTQs

VARIANT_CALLING - scripts for obtaining individual and group gvcfs from bcftools and gatk, and individual gvcfs from platypus
###INDIVIDUAL###
#Generate_GATK_ind_calling_scripts.py - Individual variant calling for gatk
```
python python_generation_scripts/Generate_GATK_ind_calling_scripts.py -d /home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files -i horse_ids.txt -p GenotypeGVCFs
``` 
#output files: gatk_individual_calling/gatk_GenotypeGVCFs_YAKU0171A.pbs etc. 

#Generate_union_PBS.py - create union of variant PBS for bcftools, gatk and platypus for the individually called vcfs.
```
python python_generation_scripts/Generate_union_PBS.py -i horse_ids.txt -d /home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files -p bcftools
```
#output files: union_bcftools.pbs  union_gatk.pbs  union_platypus.pbs

#Get union of the 3 VCs: union_all.pbs
#Get intersect of the 3 VCs: intersect_all.pbs

###JOINT###
#gatk_GenotypeVCFs_all.py - genotype all gatk gvcfs together
```
python python_Generation_scripts/gatk_GenotypeVCFs_all.py -i horse_ids.txt -d /home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files -p GenotypeGVCFS
```
#output file: gatk_GenotypeGVCFs.pbs

#Need to get union/intersect scripts for each chromosome (TO DO)


VARIANT_ANNOTATION - scripts for running SnpEff, Ensembl-VEP and ANNOVAR
###INDIVIDUAL###
##union##
#SnpEff/SnpEff_union_ind.pbs - run SnpEff on union file
#ANNOVAR/ANNOVAR_union.pbs
#Ensembl-VEP/Ensembl-VEP_union_ind.pbs

##intersect##
#SnpEff/SnpEff_intersect_ind.pbs - run SnpEff on union file
#ANNOVAR/ANNOVAR_intersect.pbs
#Ensembl-VEP/Ensembl-VEP_intersect_ind.pbs 

###GROUP###
##union##

##intersect##

###Extract coding variants###
##union and intersect##
#Already done for ANNOVAR
#Ensembl-VEP/Ensembl-VEP_filter.pbs
#SnpEff/Snpsift.pbs

GENETIC_BURDEN - scripts for running the genetic burden pipeline
#Individual and group union and intersect of VCs coding variants can be extracted using the scripts in the annotation folder.

VARIANT_PRIORITIZATION - scripts for prioritizing each of the diseases for investigation

TRANSFERRING_DATA - scripts for transferring data from interval bio to MSI

GeneratePBS.py - script to create pbs scripts for GATK combine variants
