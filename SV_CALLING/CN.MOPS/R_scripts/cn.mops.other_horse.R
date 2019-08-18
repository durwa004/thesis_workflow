#module load R/3.5.0
library(cn.mops)

BAMFiles <- c("./ibio_output_files/ERR1397962/ERR1397962.recalibrated.bam", "./ibio_output_files/ERR1397965/ERR1397965.recalibrated.bam", "./ibio_output_files/LIPI0186A/LIPI0186A.recalibrated.bam", "./ibio_output_files/LIPI0187A/LIPI0187A.recalibrated.bam", "./ibio_output_files/LIPI0188A/LIPI0188A.recalibrated.bam", "./ibio_output_files/LIPI0189A/LIPI0189A.recalibrated.bam", "./ibio_output_files/ERR982794/ERR982794.recalibrated.bam", "./ibio_output_files/M11014/M11014.recalibrated.bam", "./ibio_output_files/ERR982786/ERR982786.recalibrated.bam", "./ibio_output_files/SRR2142313/SRR2142313.recalibrated.bam", "./ibio_output_files/SRR1046135/SRR1046135.recalibrated.bam", "./ibio_output_files/SRR1564422/SRR1564422.recalibrated.bam", "./ibio_output_files/SRR1564421/SRR1564421.recalibrated.bam", "./ibio_output_files/SRR1564419/SRR1564419.recalibrated.bam", "./ibio_output_files/K743/K743.recalibrated.bam", "./ibio_output_files/SRR1564423/SRR1564423.recalibrated.bam", "./ibio_output_files/BROOKS1032/BROOKS1032.recalibrated.bam")
RefSeqNames = c("NC_009144.3", "NC_009145.3", "NC_009146.3", "NC_009147.3", "NC_009148.3", "NC_009149.3", "NC_009150.3", "NC_009151.3", "NC_009152.3", "NC_009153.3", "NC_009154.3", "NC_009155.3", "NC_009156.3", "NC_009157.3", "NC_009158.3", "NC_009159.3", "NC_009160.3", "NC_009161.3", "NC_009162.3", "NC_009163.3", "NC_009164.3", "NC_009165.3", "NC_009166.3", "NC_009167.3", "NC_009168.3", "NC_009169.3", "NC_009170.3", "NC_009171.3", "NC_009172.3", "NC_009173.3", "NC_009174.3", "NC_009175.3", "NC_001640.1")
sampleNames = c("ERR1397962", "ERR1397965", "LIPI0186A", "LIPI0187A", "LIPI0188A", "LIPI0189A", "ERR982794", "M11014", "ERR982786", "SRR2142313", "SRR1046135", "SRR1564422", "SRR1564421", "SRR1564419", "K743", "SRR1564423", "BROOKS1032")
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
write.csv(segm,file='ibio_other_horse_segmentation.csv')
write.csv(CNVs,file='ibio_other_horse_CNVs.csv')
write.csv(CNVRegions,file='ibio_other_horse_CNVR.csv')
