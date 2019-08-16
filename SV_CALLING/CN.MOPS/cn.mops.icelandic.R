#module load R/3.5.0
library(cn.mops)

BAMFiles <- c("./ibio_output_files/IT3/IT3.recalibrated.bam", "./ibio_output_files/IT4/IT4.recalibrated.bam", "./ibio_output_files/ICEL0143A/ICEL0143A.recalibrated.bam", "./ibio_output_files/ICEL0144A/ICEL0144A.recalibrated.bam", "./ibio_output_files/M487/M487.recalibrated.bam", "./ibio_output_files/M466/M466.recalibrated.bam", "./ibio_output_files/M467/M467.recalibrated.bam", "./ibio_output_files/M468/M468.recalibrated.bam", "./ibio_output_files/M469/M469.recalibrated.bam", "./ibio_output_files/M470/M470.recalibrated.bam", "./ibio_output_files/M472/M472.recalibrated.bam", "./ibio_output_files/M473/M473.recalibrated.bam", "./ibio_output_files/M475/M475.recalibrated.bam", "./ibio_output_files/M476/M476.recalibrated.bam", "./ibio_output_files/M477/M477.recalibrated.bam", "./ibio_output_files/M478/M478.recalibrated.bam", "./ibio_output_files/M479/M479.recalibrated.bam", "./ibio_output_files/ERR863167/ERR863167.recalibrated.bam", "./ibio_output_files/ERR793393/ERR793393.recalibrated.bam", "./ibio_output_files/SRR1167093/SRR1167093.recalibrated.bam", "./ibio_output_files/SRR1167052/SRR1167052.recalibrated.bam", "./ibio_output_files/SRR1167108/SRR1167108.recalibrated.bam", "./ibio_output_files/SRR1167109/SRR1167109.recalibrated.bam", "./ibio_output_files/SRR1167110/SRR1167110.recalibrated.bam", "./ibio_output_files/SRR1167891/SRR1167891.recalibrated.bam", "./ibio_output_files/SRR1167892/SRR1167892.recalibrated.bam", "./ibio_output_files/SRR1167893/SRR1167893.recalibrated.bam", "./ibio_output_files/SRR1167053/SRR1167053.recalibrated.bam", "./ibio_output_files/FJOR0142A/FJOR0142A.recalibrated.bam", "./ibio_output_files/YAKU0163A/YAKU0163A.recalibrated.bam", "./ibio_output_files/YAKU0164A/YAKU0164A.recalibrated.bam", "./ibio_output_files/YAKU0165A/YAKU0165A.recalibrated.bam", "./ibio_output_files/YAKU0166A/YAKU0166A.recalibrated.bam", "./ibio_output_files/YAKU0167A/YAKU0167A.recalibrated.bam", "./ibio_output_files/YAKU0168A/YAKU0168A.recalibrated.bam", "./ibio_output_files/YAKU0169A/YAKU0169A.recalibrated.bam", "./ibio_output_files/YAKU0170A/YAKU0170A.recalibrated.bam", "./ibio_output_files/YAKU0171A/YAKU0171A.recalibrated.bam")
RefSeqNames = c("NC_009144.3", "NC_009145.3", "NC_009146.3", "NC_009147.3", "NC_009148.3", "NC_009149.3", "NC_009150.3", "NC_009151.3", "NC_009152.3", "NC_009153.3", "NC_009154.3", "NC_009155.3", "NC_009156.3", "NC_009157.3", "NC_009158.3", "NC_009159.3", "NC_009160.3", "NC_009161.3", "NC_009162.3", "NC_009163.3", "NC_009164.3", "NC_009165.3", "NC_009166.3", "NC_009167.3", "NC_009168.3", "NC_009169.3", "NC_009170.3", "NC_009171.3", "NC_009172.3", "NC_009173.3", "NC_009174.3", "NC_009175.3", "NC_001640.1")
sampleNames = c("IT3", "IT4", "ICEL0143A", "ICEL0144A", "M487", "M466", "M467", "M468", "M469", "M470", "M472", "M473", "M475", "M476", "M477", "M478", "M479", "ERR863167", "ERR793393", "SRR1167093", "SRR1167052", "SRR1167108", "SRR1167109", "SRR1167110", "SRR1167891", "SRR1167892", "SRR1167893", "SRR1167053", "FJOR0142A", "YAKU0163A", "YAKU0164A", "YAKU0165A", "YAKU0166A", "YAKU0167A", "YAKU0168A", "YAKU0169A", "YAKU0170A", "YAKU0171A")
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
write.csv(segm,file='ibio_icelandic_segmentation.csv')
write.csv(CNVs,file='ibio_icelandic_CNVs.csv')
write.csv(CNVRegions,file='ibio_icelandic_CNVR.csv')
