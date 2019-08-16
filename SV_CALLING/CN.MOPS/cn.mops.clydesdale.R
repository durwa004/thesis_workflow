#module load R/3.5.0
library(cn.mops)

BAMFiles <- c("./ibio_output_files/M1557/M1557.recalibrated.bam", "./ibio_output_files/M1559/M1559.recalibrated.bam", "./ibio_output_files/M1561/M1561.recalibrated.bam", "./ibio_output_files/M1568/M1568.recalibrated.bam", "./ibio_output_files/M1570/M1570.recalibrated.bam", "./ibio_output_files/M1571/M1571.recalibrated.bam", "./ibio_output_files/M1579/M1579.recalibrated.bam", "./ibio_output_files/M1581/M1581.recalibrated.bam", "./ibio_output_files/M1583/M1583.recalibrated.bam", "./ibio_output_files/M7645/M7645.recalibrated.bam", "./ibio_output_files/M1556/M1556.recalibrated.bam", "./ibio_output_files/M1565/M1565.recalibrated.bam", "./ibio_output_files/M1563/M1563.recalibrated.bam", "./ibio_output_files/M2023/M2023.recalibrated.bam", "./ibio_output_files/M2025/M2025.recalibrated.bam", "./ibio_output_files/M2039/M2039.recalibrated.bam", "./ibio_output_files/M2044/M2044.recalibrated.bam", "./ibio_output_files/M2060/M2060.recalibrated.bam", "./ibio_output_files/M2068/M2068.recalibrated.bam")
RefSeqNames = c("NC_009144.3", "NC_009145.3", "NC_009146.3", "NC_009147.3", "NC_009148.3", "NC_009149.3", "NC_009150.3", "NC_009151.3", "NC_009152.3", "NC_009153.3", "NC_009154.3", "NC_009155.3", "NC_009156.3", "NC_009157.3", "NC_009158.3", "NC_009159.3", "NC_009160.3", "NC_009161.3", "NC_009162.3", "NC_009163.3", "NC_009164.3", "NC_009165.3", "NC_009166.3", "NC_009167.3", "NC_009168.3", "NC_009169.3", "NC_009170.3", "NC_009171.3", "NC_009172.3", "NC_009173.3", "NC_009174.3", "NC_009175.3", "NC_001640.1")
sampleNames = c("M1557", "M1559", "M1561", "M1568", "M1570", "M1571", "M1579", "M1581", "M1583", "M7645", "M1556", "M1565", "M1563", "M2023", "M2025", "M2039", "M2044", "M2060", "M2068")
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
write.csv(segm,file='ibio_clydesdale_segmentation.csv')
write.csv(CNVs,file='ibio_clydesdale_CNVs.csv')
write.csv(CNVRegions,file='ibio_clydesdale_CNVR.csv')
