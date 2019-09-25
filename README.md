###Pipeline for thesis.

##################################################################################################################################################################################
FAILED_FILES - Old scripts that I am not sure can be deleted yet! 
bcftools_bgzip_tabix_joint.pbs - performs bgzip and tabix on bcftools output
gatk_convert_joint.pbs and bcftools_convert_joint.pbs - perform bcftools call (used to select only variants (i.e. convert gvcf to vcf) but output doesn't work with gatk so used a different method)

##################################################################################################################################################################################

GeneratePBS.py - script to create pbs scripts for GATK combine variants
  #For GeneratePBS.py type scripts, need to use python 3.6 - which is available in the snakemake conda environment

##################################################################################################################################################################################

GENETIC_BURDEN - scripts for running the genetic burden pipeline
#Individual and group union and intersect of VCs coding variants can be extracted using the scripts in the annotation folder.

#JOINT CALLING for SnpEff/annovar
Create list of chrom/pos/impact for analysis
```
$ python Get_chrom_pos_impact.py -d /home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files/joint_intersect/ -p SnpEff
```
Output: SnpEff_chrom_pos_impact.txt and annovar_chrom_pos_impact.txt
```
$ python Get_union_intersect_VEPs.py -d /home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files/joint_intersect/
```
Output

##################################################################################################################################################################################

MAPPING - scripts for mapping FASTQs

##################################################################################################################################################################################

PROTOCOLS - all protocols for setting up and running pipeline
##################################################################################################################################################################################

RANDOM_REQUESTS - any additional requests I get with regard to this data
#Ted_K - scripts to transfer gvcfs (excluding PPID and 1KG horses) to Ted

##################################################################################################################################################################################

UNFREEZE - scripts to unfreeze data following transfer by ibio
  #Generate_unfreeze.py - python script to create .pbs
  #s3cmd_get.pbs - script to get particular type of file
#Download coverage info for each horse
```
$ python Generate_unfreeze_coverage.py -d /home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files/DOC/ -c get -i ../horse_ids.txt -f coverage.tsv
$ qsub /home/mccuem/shared/Projects/HorseGenomeProject/scripts/EquCab3/thesis_workflow/UNFREEZE/s3cmd_get_coverage.tsv.pbs 
```

##################################################################################################################################################################################

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
#Convert gvcfs to vcfs
```
python python_generation_scripts/Generate_SelectVariants.py -d /home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files/ -p gatk
```
#Output: gatk_selectvariants_joint_NC_001640_1.pbs/bcftools_selectvariants_jointNC_001640_1.pbs

###Union scripts for each chromosome###
```
python python_generation_scripts/Generate_union_by_chr.py -d /home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files/)
```
#Output_file (for each chromosome): union_joint_NC_001640_1.pbs 

###Intersect scripts for each chromosome###
```
python python_generation_scripts/Generate_intersect_joint.pbs -d /home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/ibio_output_files/
```
#Output_file (for each chromosome): intersect_joint_NC_001640_1.pbs 

##################################################################################################################################################################################

VARIANT_PRIORITIZATION - scripts for prioritizing each of the diseases for investigation

