#module load R/3.5.0
library(cn.mops)

BAMFiles <- c("./ibio_output_files/CON15/CON15.recalibrated.bam", "./ibio_output_files/CON26/CON26.recalibrated.bam", "./ibio_output_files/CON3/CON3.recalibrated.bam", "./ibio_output_files/CON40/CON40.recalibrated.bam", "./ibio_output_files/SRR1048526/SRR1048526.recalibrated.bam", "./ibio_output_files/ERR1527966/ERR1527966.recalibrated.bam", "./ibio_output_files/HF13B/HF13B.recalibrated.bam", "./ibio_output_files/HF13C/HF13C.recalibrated.bam", "./ibio_output_files/HF13D/HF13D.recalibrated.bam", "./ibio_output_files/HF14A/HF14A.recalibrated.bam", "./ibio_output_files/HF14C/HF14C.recalibrated.bam", "./ibio_output_files/HF15A/HF15A.recalibrated.bam", "./ibio_output_files/HAFL0015A/HAFL0015A.recalibrated.bam", "./ibio_output_files/SRR527804/SRR527804.recalibrated.bam", "./ibio_output_files/SRR527528/SRR527528.recalibrated.bam", "./ibio_output_files/SRR527799/SRR527799.recalibrated.bam", "./ibio_output_files/SRR527803/SRR527803.recalibrated.bam", "./ibio_output_files/SRR526907/SRR526907.recalibrated.bam", "./ibio_output_files/SRR527520/SRR527520.recalibrated.bam", "./ibio_output_files/SRR527521/SRR527521.recalibrated.bam", "./ibio_output_files/SRR527806/SRR527806.recalibrated.bam", "./ibio_output_files/SRR516118/SRR516118.recalibrated.bam", "./ibio_output_files/SRR526908/SRR526908.recalibrated.bam", "./ibio_output_files/SRR526909/SRR526909.recalibrated.bam", "./ibio_output_files/SRR527805/SRR527805.recalibrated.bam", "./ibio_output_files/SRR527527/SRR527527.recalibrated.bam", "./ibio_output_files/SRR527807/SRR527807.recalibrated.bam", "./ibio_output_files/SRR527825/SRR527825.recalibrated.bam", "./ibio_output_files/SRR527519/SRR527519.recalibrated.bam", "./ibio_output_files/SRR527809/SRR527809.recalibrated.bam", "./ibio_output_files/SRR527802/SRR527802.recalibrated.bam", "./ibio_output_files/SRR527801/SRR527801.recalibrated.bam", "./ibio_output_files/SRR527800/SRR527800.recalibrated.bam", "./ibio_output_files/M11011/M11011.recalibrated.bam", "./ibio_output_files/M11009/M11009.recalibrated.bam")
RefSeqNames = c("NC_009144.3", "NC_009145.3", "NC_009146.3", "NC_009147.3", "NC_009148.3", "NC_009149.3", "NC_009150.3", "NC_009151.3", "NC_009152.3", "NC_009153.3", "NC_009154.3", "NC_009155.3", "NC_009156.3", "NC_009157.3", "NC_009158.3", "NC_009159.3", "NC_009160.3", "NC_009161.3", "NC_009162.3", "NC_009163.3", "NC_009164.3", "NC_009165.3", "NC_009166.3", "NC_009167.3", "NC_009168.3", "NC_009169.3", "NC_009170.3", "NC_009171.3", "NC_009172.3", "NC_009173.3", "NC_009174.3", "NC_009175.3", "NC_001640.1")
sampleNames = c("CON15", "CON26", "CON3", "CON40", "SRR1048526", "ERR1527966", "HF13B", "HF13C", "HF13D", "HF14A", "HF14C", "HF15A", "HAFL0015A", "SRR527804", "SRR527528", "SRR527799", "SRR527803", "SRR526907", "SRR527520", "SRR527521", "SRR527806", "SRR516118", "SRR526908", "SRR526909", "SRR527805", "SRR527527", "SRR527807", "SRR527825", "SRR527519", "SRR527809", "SRR527802", "SRR527801", "SRR527800", "M11011", "M11009")
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
write.csv(segm,file='ibio_other_pony_segmentation.csv')
write.csv(CNVs,file='ibio_other_pony_CNVs.csv')
write.csv(CNVRegions,file='ibio_other_pony_CNVR.csv')
