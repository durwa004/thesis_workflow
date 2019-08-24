###Pipeline for thesis.

FAILED_FILES - Old scripts that I am not sure can be deleted yet! 

GeneratePBS.py - script to create pbs scripts for GATK combine variants
  #For GeneratePBS.py type scripts, need to use python 3.6 - which is available in the snakemake conda environment

GENETIC_BURDEN - scripts for running the genetic burden pipeline
#Individual and group union and intersect of VCs coding variants can be extracted using the scripts in the annotation folder.

MAPPING - scripts for mapping FASTQs

PROTOCOLS - all protocols for setting up and running pipeline

SV_CALLING - scripts for performing structural variant analysis 
#BREAKDANCER
  #pbs_scripts - by breed scripts for running BreakDancer
  #Generate_breakdancer_script.py - script to generate breakdancer .pbs scripts
#breed_group_ids - breed ids copied and pasted from intervalbio ID column in Samples_all_april19 google spreadsheet
#CN.MOPSi
  #GCF_002863925.1_EquCab3.0_genomic_exc_chrUn.list - list of EquCab3 chromosomes using RefSeq nomenclature (without chromosome unknown contigs)
  #Generate_cn.mops.py - create cn.mops R scripts
  #R_scripts - by breed scripts for running cn.mops
#GENOMESTRIP - 
  #create_metadata_bundle - scripts required to create metadata bundle for Genomestrip (not necessarily in right order)
  #.py files - scripts to generate different scripts for running genomestrip
  #pbs_sciprts - currently only done for arabs
    #1. SVPreprocessing
    #2. SVDiscovery
    #3. SVgenotyper
    #4. SVCNV_high/low

#test.py - scripts for modifying the GeneratePBS.py script (temp files)

TRANSFERRING_DATA - scripts for transferring data from interval bio to MSI

UNFREEZE - scripts to unfreeze data following transfer by ibio
  #Generate_unfreeze.py - python script to create .pbs
  #s3cmd_get.pbs - script to get particular type of file

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
#Generate_GenotypeVCFs_all.py - genotype joint called gatk gvcfs by chromosome
```
python python_generation_scripts/Generate_GenotypeVCFs_all.py -d /home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files/gatk_joint/gatk_joint_genotyped/ -c /home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files/gatk_joint/
```
#output file: gatk_genotypegvcfs_joint.pbs

#Convert bcftools gvcfs to vcfs
#Generate_bcftools_convert_joint.py
```
python python_generation_scripts/Generate_bcftools_convert_joint.py -d /home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files/bcftools_joint/bcftools_joint_genotyped/ -c /home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files/bcftools_joint/
```
#output_file: bcftools_convert_joint.pbs

#Need to get union/intersect scripts for each chromosome (TO DO)


VARIANT_PRIORITIZATION - scripts for prioritizing each of the diseases for investigation

