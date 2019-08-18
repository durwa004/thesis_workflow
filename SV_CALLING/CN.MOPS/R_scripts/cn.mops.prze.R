#module load R/3.5.0
library(cn.mops)

BAMFiles <- c("./ibio_output_files/PRZE0150A/PRZE0150A.recalibrated.bam", "./ibio_output_files/PRZE0151A/PRZE0151A.recalibrated.bam", "./ibio_output_files/PRZE0152A/PRZE0152A.recalibrated.bam", "./ibio_output_files/PRZE0154A/PRZE0154A.recalibrated.bam", "./ibio_output_files/PRZE0155A/PRZE0155A.recalibrated.bam", "./ibio_output_files/MONG0153A/MONG0153A.recalibrated.bam", "./ibio_output_files/PRZE0159A/PRZE0159A.recalibrated.bam", "./ibio_output_files/PRZE0160A/PRZE0160A.recalibrated.bam", "./ibio_output_files/PRZE0161A/PRZE0161A.recalibrated.bam", "./ibio_output_files/PRZE0162A/PRZE0162A.recalibrated.bam", "./ibio_output_files/PRZE0156A/PRZE0156A.recalibrated.bam", "./ibio_output_files/PRZE0157A/PRZE0157A.recalibrated.bam", "./ibio_output_files/PRZE0158A/PRZE0158A.recalibrated.bam")
RefSeqNames = c("NC_009144.3", "NC_009145.3", "NC_009146.3", "NC_009147.3", "NC_009148.3", "NC_009149.3", "NC_009150.3", "NC_009151.3", "NC_009152.3", "NC_009153.3", "NC_009154.3", "NC_009155.3", "NC_009156.3", "NC_009157.3", "NC_009158.3", "NC_009159.3", "NC_009160.3", "NC_009161.3", "NC_009162.3", "NC_009163.3", "NC_009164.3", "NC_009165.3", "NC_009166.3", "NC_009167.3", "NC_009168.3", "NC_009169.3", "NC_009170.3", "NC_009171.3", "NC_009172.3", "NC_009173.3", "NC_009174.3", "NC_009175.3", "NC_001640.1")
sampleNames = c("PRZE0150A", "PRZE0151A", "PRZE0152A", "PRZE0154A", "PRZE0155A", "MONG0153A", "PRZE0159A", "PRZE0160A", "PRZE0161A", "PRZE0162A", "PRZE0156A", "PRZE0157A", "PRZE0158A")
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
write.csv(segm,file='ibio_prze_segmentation.csv')
write.csv(CNVs,file='ibio_prze_CNVs.csv')
write.csv(CNVRegions,file='ibio_prze_CNVR.csv')
