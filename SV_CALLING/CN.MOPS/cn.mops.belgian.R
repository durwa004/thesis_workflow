#module load R/3.5.0
library(cn.mops)

BAMFiles <- c("./ibio_output_files/A4416/A4416.recalibrated.bam", "./ibio_output_files/M1552/M1552.recalibrated.bam", "./ibio_output_files/M1930/M1930.recalibrated.bam", "./ibio_output_files/M1931/M1931.recalibrated.bam", "./ibio_output_files/M1932/M1932.recalibrated.bam", "./ibio_output_files/M1937/M1937.recalibrated.bam", "./ibio_output_files/M1939/M1939.recalibrated.bam", "./ibio_output_files/M1942/M1942.recalibrated.bam", "./ibio_output_files/M1944/M1944.recalibrated.bam", "./ibio_output_files/M1946/M1946.recalibrated.bam", "./ibio_output_files/M1941/M1941.recalibrated.bam", "./ibio_output_files/M1964/M1964.recalibrated.bam", "./ibio_output_files/M1966/M1966.recalibrated.bam", "./ibio_output_files/M1967/M1967.recalibrated.bam", "./ibio_output_files/M1968/M1968.recalibrated.bam", "./ibio_output_files/M1970/M1970.recalibrated.bam", "./ibio_output_files/M315/M315.recalibrated.bam", "./ibio_output_files/M316/M316.recalibrated.bam", "./ibio_output_files/M367/M367.recalibrated.bam", "./ibio_output_files/M369/M369.recalibrated.bam", "./ibio_output_files/BROOKS3148/BROOKS3148.recalibrated.bam", "./ibio_output_files/M1542/M1542.recalibrated.bam", "./ibio_output_files/M1545/M1545.recalibrated.bam")
RefSeqNames = c("NC_009144.3", "NC_009145.3", "NC_009146.3", "NC_009147.3", "NC_009148.3", "NC_009149.3", "NC_009150.3", "NC_009151.3", "NC_009152.3", "NC_009153.3", "NC_009154.3", "NC_009155.3", "NC_009156.3", "NC_009157.3", "NC_009158.3", "NC_009159.3", "NC_009160.3", "NC_009161.3", "NC_009162.3", "NC_009163.3", "NC_009164.3", "NC_009165.3", "NC_009166.3", "NC_009167.3", "NC_009168.3", "NC_009169.3", "NC_009170.3", "NC_009171.3", "NC_009172.3", "NC_009173.3", "NC_009174.3", "NC_009175.3", "NC_001640.1")
sampleNames = c("A4416", "M1552", "M1930", "M1931", "M1932", "M1937", "M1939", "M1942", "M1944", "M1946", "M1941", "M1964", "M1966", "M1967", "M1968", "M1970", "M315", "M316", "M367", "M369", "BROOKS3148", "M1542", "M1545")
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
write.csv(segm,file='ibio_belgian_segmentation.csv')
write.csv(CNVs,file='ibio_belgian_CNVs.csv')
write.csv(CNVRegions,file='ibio_belgian_CNVR.csv')
