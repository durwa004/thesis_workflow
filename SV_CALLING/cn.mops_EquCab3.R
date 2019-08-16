#module load R/3.5.0
#R
library(cn.mops)

#For whatever reason, this doesn't work - gives me the dimnames error
#BAMFiles <- list.files("/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/dz_cases_bams_December_2018/", pattern = ".EquCab3_nucl.realigned.bam$", full.names = T)
BAMFiles <- c("/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/dz_cases_bams_December_2018//1KG_10.EquCab3_nucl.realigned.bam", "/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/dz_cases_bams_December_2018//1KG16.EquCab3_nucl.realigned.bam", "/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/dz_cases_bams_December_2018//1KG17.EquCab3_nucl.realigned.bam", "/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/dz_cases_bams_December_2018//1KG18.EquCab3_nucl.realigned.bam", "/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/dz_cases_bams_December_2018//1KG_1.EquCab3_nucl.realigned.bam", "/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/dz_cases_bams_December_2018//1KG_25.EquCab3_nucl.realigned.bam", "/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/dz_cases_bams_December_2018//1KG_4.EquCab3_nucl.realigned.bam", "/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/dz_cases_bams_December_2018//1KG_5.EquCab3_nucl.realigned.bam", "/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/dz_cases_bams_December_2018//1KG_6.EquCab3_nucl.realigned.bam", "/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/dz_cases_bams_December_2018//1KG_7.EquCab3_nucl.realigned.bam", "/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/dz_cases_bams_December_2018//1KG_8.EquCab3_nucl.realigned.bam")

RefSeqNames = c("chr10","chr11","chr12","chr13","chr14","chr15","chr16","chr17","chr18","chr19","chr1","chr20","chr21","chr22","chr23","chr24","chr25","chr26","chr27","chr28","chr29","chr2","chr30","chr31","chr3","chr4","chr5","chr6","chr7","chr8","chr9","chrX")

sampleNames = c("1KG_10", "1KG16", "1KG17", "1KG18", "1KG_1", "1KG_25", "1KG_4", "1KG_5", "1KG_6", "1KG_7", "1KG_8")

#NB needs to be in this exact order!
bamDataRanges <- getReadCountsFromBAM(BAMFiles,sampleNames, RefSeqNames, WL = 5000, parallel=4)

res <- cn.mops(bamDataRanges)
#Calculate integer copy numbers
results <- calcIntegerCopyNumbers(res)
segm <- as.data.frame(segmentation(results))
#Identify CNVs
CNVs <- as.data.frame(cnvs(results))
#Identify CNV regions
CNVRegions <- as.data.frame(cnvr(results))

#Output data
write.csv(segm,file="dz_cases_segmentation.csv")
write.csv(CNVs,file="dz_cases_CNVs.csv")      
write.csv(CNVRegions,file="dz_cases_CNVR.csv")

