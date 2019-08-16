#module load R/3.5.0
library(cn.mops)

BAMFiles <- c("./ibio_output_files/CLDB65664/CLDB65664.recalibrated.bam", "./ibio_output_files/CLDB65665/CLDB65665.recalibrated.bam", "./ibio_output_files/CLDB65666/CLDB65666.recalibrated.bam", "./ibio_output_files/M11008/M11008.recalibrated.bam", "./ibio_output_files/FRMO0041A/FRMO0041A.recalibrated.bam", "./ibio_output_files/FRMO0042A/FRMO0042A.recalibrated.bam", "./ibio_output_files/FRMO0043A/FRMO0043A.recalibrated.bam", "./ibio_output_files/FRMO0044A/FRMO0044A.recalibrated.bam", "./ibio_output_files/FRMO0045A/FRMO0045A.recalibrated.bam", "./ibio_output_files/FRMO0046A/FRMO0046A.recalibrated.bam", "./ibio_output_files/FRMO0047A/FRMO0047A.recalibrated.bam", "./ibio_output_files/FRMO0048A/FRMO0048A.recalibrated.bam", "./ibio_output_files/FRMO0049A/FRMO0049A.recalibrated.bam", "./ibio_output_files/FRMO0050A/FRMO0050A.recalibrated.bam", "./ibio_output_files/FRMO0051A/FRMO0051A.recalibrated.bam", "./ibio_output_files/FRMO0052A/FRMO0052A.recalibrated.bam", "./ibio_output_files/FRMO0053A/FRMO0053A.recalibrated.bam", "./ibio_output_files/FRMO0054A/FRMO0054A.recalibrated.bam", "./ibio_output_files/FRMO0055A/FRMO0055A.recalibrated.bam", "./ibio_output_files/FRMO0056A/FRMO0056A.recalibrated.bam", "./ibio_output_files/FRMO0057A/FRMO0057A.recalibrated.bam", "./ibio_output_files/FRMO0058A/FRMO0058A.recalibrated.bam", "./ibio_output_files/FRMO0059A/FRMO0059A.recalibrated.bam", "./ibio_output_files/FRMO0060A/FRMO0060A.recalibrated.bam", "./ibio_output_files/FRMO0061A/FRMO0061A.recalibrated.bam", "./ibio_output_files/FRMO0062A/FRMO0062A.recalibrated.bam", "./ibio_output_files/FRMO0063A/FRMO0063A.recalibrated.bam", "./ibio_output_files/FRMO0064A/FRMO0064A.recalibrated.bam", "./ibio_output_files/FRMO0065A/FRMO0065A.recalibrated.bam", "./ibio_output_files/FRMO0066A/FRMO0066A.recalibrated.bam", "./ibio_output_files/FRMO0067A/FRMO0067A.recalibrated.bam", "./ibio_output_files/FRMO0068A/FRMO0068A.recalibrated.bam", "./ibio_output_files/FRMO0037A/FRMO0037A.recalibrated.bam", "./ibio_output_files/FRMO0069A/FRMO0069A.recalibrated.bam")
RefSeqNames = c("NC_009144.3", "NC_009145.3", "NC_009146.3", "NC_009147.3", "NC_009148.3", "NC_009149.3", "NC_009150.3", "NC_009151.3", "NC_009152.3", "NC_009153.3", "NC_009154.3", "NC_009155.3", "NC_009156.3", "NC_009157.3", "NC_009158.3", "NC_009159.3", "NC_009160.3", "NC_009161.3", "NC_009162.3", "NC_009163.3", "NC_009164.3", "NC_009165.3", "NC_009166.3", "NC_009167.3", "NC_009168.3", "NC_009169.3", "NC_009170.3", "NC_009171.3", "NC_009172.3", "NC_009173.3", "NC_009174.3", "NC_009175.3", "NC_001640.1")
sampleNames = c("CLDB65664", "CLDB65665", "CLDB65666", "M11008", "FRMO0041A", "FRMO0042A", "FRMO0043A", "FRMO0044A", "FRMO0045A", "FRMO0046A", "FRMO0047A", "FRMO0048A", "FRMO0049A", "FRMO0050A", "FRMO0051A", "FRMO0052A", "FRMO0053A", "FRMO0054A", "FRMO0055A", "FRMO0056A", "FRMO0057A", "FRMO0058A", "FRMO0059A", "FRMO0060A", "FRMO0061A", "FRMO0062A", "FRMO0063A", "FRMO0064A", "FRMO0065A", "FRMO0066A", "FRMO0067A", "FRMO0068A", "FRMO0037A", "FRMO0069A")
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
write.csv(segm,file='ibio_other_draft_segmentation.csv')
write.csv(CNVs,file='ibio_other_draft_CNVs.csv')
write.csv(CNVRegions,file='ibio_other_draft_CNVR.csv')
