#module load R/3.5.0
library(cn.mops)

BAMFiles <- c("./ibio_output_files/M6337/M6337.recalibrated.bam", "./ibio_output_files/M6449/M6449.recalibrated.bam", "./ibio_output_files/M6462/M6462.recalibrated.bam", "./ibio_output_files/M6468/M6468.recalibrated.bam", "./ibio_output_files/M6482/M6482.recalibrated.bam", "./ibio_output_files/M6536/M6536.recalibrated.bam", "./ibio_output_files/M6539/M6539.recalibrated.bam", "./ibio_output_files/M6558/M6558.recalibrated.bam", "./ibio_output_files/M6598/M6598.recalibrated.bam", "./ibio_output_files/M6682/M6682.recalibrated.bam", "./ibio_output_files/M6252/M6252.recalibrated.bam", "./ibio_output_files/M6253/M6253.recalibrated.bam", "./ibio_output_files/M6798/M6798.recalibrated.bam", "./ibio_output_files/M6807/M6807.recalibrated.bam", "./ibio_output_files/M6813/M6813.recalibrated.bam", "./ibio_output_files/M6212/M6212.recalibrated.bam", "./ibio_output_files/M6294/M6294.recalibrated.bam", "./ibio_output_files/M6296/M6296.recalibrated.bam", "./ibio_output_files/M10999/M10999.recalibrated.bam", "./ibio_output_files/M11020/M11020.recalibrated.bam", "./ibio_output_files/M11003/M11003.recalibrated.bam", "./ibio_output_files/M11005/M11005.recalibrated.bam", "./ibio_output_files/M11006/M11006.recalibrated.bam", "./ibio_output_files/ERR953413/ERR953413.recalibrated.bam")
RefSeqNames = c("NC_009144.3", "NC_009145.3", "NC_009146.3", "NC_009147.3", "NC_009148.3", "NC_009149.3", "NC_009150.3", "NC_009151.3", "NC_009152.3", "NC_009153.3", "NC_009154.3", "NC_009155.3", "NC_009156.3", "NC_009157.3", "NC_009158.3", "NC_009159.3", "NC_009160.3", "NC_009161.3", "NC_009162.3", "NC_009163.3", "NC_009164.3", "NC_009165.3", "NC_009166.3", "NC_009167.3", "NC_009168.3", "NC_009169.3", "NC_009170.3", "NC_009171.3", "NC_009172.3", "NC_009173.3", "NC_009174.3", "NC_009175.3", "NC_001640.1")
sampleNames = c("M6337", "M6449", "M6462", "M6468", "M6482", "M6536", "M6539", "M6558", "M6598", "M6682", "M6252", "M6253", "M6798", "M6807", "M6813", "M6212", "M6294", "M6296", "M10999", "M11020", "M11003", "M11005", "M11006", "ERR953413")
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
write.csv(segm,file='ibio_morgan_segmentation.csv')
write.csv(CNVs,file='ibio_morgan_CNVs.csv')
write.csv(CNVRegions,file='ibio_morgan_CNVR.csv')
