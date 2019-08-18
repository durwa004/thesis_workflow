#module load R/3.5.0
library(cn.mops)

BAMFiles <- c("./ibio_output_files/K744/K744.recalibrated.bam", "./ibio_output_files/M10638/M10638.recalibrated.bam", "./ibio_output_files/M10641/M10641.recalibrated.bam", "./ibio_output_files/M10642/M10642.recalibrated.bam", "./ibio_output_files/ARAB0132A/ARAB0132A.recalibrated.bam", "./ibio_output_files/ARAB0016A/ARAB0016A.recalibrated.bam", "./ibio_output_files/ARAB0133A/ARAB0133A.recalibrated.bam", "./ibio_output_files/ARAB0134A/ARAB0134A.recalibrated.bam", "./ibio_output_files/ARAB0017A/ARAB0017A.recalibrated.bam", "./ibio_output_files/ARAB0018A/ARAB0018A.recalibrated.bam", "./ibio_output_files/ARAB0135A/ARAB0135A.recalibrated.bam", "./ibio_output_files/ARAB0136A/ARAB0136A.recalibrated.bam", "./ibio_output_files/ARAB0019A/ARAB0019A.recalibrated.bam", "./ibio_output_files/ARAB0020A/ARAB0020A.recalibrated.bam", "./ibio_output_files/ARAB0141A/ARAB0141A.recalibrated.bam", "./ibio_output_files/ARAB0034A/ARAB0034A.recalibrated.bam", "./ibio_output_files/ARAB0035A/ARAB0035A.recalibrated.bam", "./ibio_output_files/ARAB0036A/ARAB0036A.recalibrated.bam", "./ibio_output_files/BROOKS2174/BROOKS2174.recalibrated.bam", "./ibio_output_files/M10998/M10998.recalibrated.bam", "./ibio_output_files/M11000/M11000.recalibrated.bam", "./ibio_output_files/M11002/M11002.recalibrated.bam", "./ibio_output_files/M11013/M11013.recalibrated.bam", "./ibio_output_files/ERR1527951/ERR1527951.recalibrated.bam", "./ibio_output_files/SRR4054279/SRR4054279.recalibrated.bam", "./ibio_output_files/SRR4054242/SRR4054242.recalibrated.bam", "./ibio_output_files/SRR4054277/SRR4054277.recalibrated.bam", "./ibio_output_files/SRR3726219/SRR3726219.recalibrated.bam", "./ibio_output_files/SRR1046129/SRR1046129.recalibrated.bam", "./ibio_output_files/M10648/M10648.recalibrated.bam", "./ibio_output_files/M10649/M10649.recalibrated.bam", "./ibio_output_files/M10639/M10639.recalibrated.bam", "./ibio_output_files/M10658/M10658.recalibrated.bam", "./ibio_output_files/M10640/M10640.recalibrated.bam", "./ibio_output_files/M10661/M10661.recalibrated.bam")
RefSeqNames = c("NC_009144.3", "NC_009145.3", "NC_009146.3", "NC_009147.3", "NC_009148.3", "NC_009149.3", "NC_009150.3", "NC_009151.3", "NC_009152.3", "NC_009153.3", "NC_009154.3", "NC_009155.3", "NC_009156.3", "NC_009157.3", "NC_009158.3", "NC_009159.3", "NC_009160.3", "NC_009161.3", "NC_009162.3", "NC_009163.3", "NC_009164.3", "NC_009165.3", "NC_009166.3", "NC_009167.3", "NC_009168.3", "NC_009169.3", "NC_009170.3", "NC_009171.3", "NC_009172.3", "NC_009173.3", "NC_009174.3", "NC_009175.3", "NC_001640.1")
sampleNames = c("K744", "M10638", "M10641", "M10642", "ARAB0132A", "ARAB0016A", "ARAB0133A", "ARAB0134A", "ARAB0017A", "ARAB0018A", "ARAB0135A", "ARAB0136A", "ARAB0019A", "ARAB0020A", "ARAB0141A", "ARAB0034A", "ARAB0035A", "ARAB0036A", "BROOKS2174", "M10998", "M11000", "M11002", "M11013", "ERR1527951", "SRR4054279", "SRR4054242", "SRR4054277", "SRR3726219", "SRR1046129", "M10648", "M10649", "M10639", "M10658", "M10640", "M10661")
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
write.csv(segm,file='ibio_arab_segmentation.csv')
write.csv(CNVs,file='ibio_arab_CNVs.csv')
write.csv(CNVRegions,file='ibio_arab_CNVR.csv')
