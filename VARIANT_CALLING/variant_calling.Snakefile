configfile: "AFIB_config.yaml"

#This should take the individually called platypus vcfs and merge them into a union file
rule union_individual_platypus_vcfs:
    input:
        fna="/home/mccuem/shared/Projects/HorseGenomeProject/Data/ibio_EquCab3/NCBI_reference/GCF_002863925.1_EquCab3.0_genomic.fna",
        vcf=expand("{sample}/{sample}.platypus.vcf.gz",sample=config["samples"]),
    output:
        "union_individual/platypus.vcf.gz"
    threads: 4
#    params: inputString =  lambda wildcards, " --variant ".join(input)
    shell:
        "(java -Xmx4g -jar /home/mccuem/shared/.local/conda/envs/HorseGenomeProject/bin/GenomeAnalysisTK.jar -R input.fna -T CombineVariants -nt {threads} --variant ' --variant '.join({input.vcf}) -o {output})" 

#params: inputString = lambda wildcards, input: " -V ".join(input)

#rule combine_vcfs:
#     input:
#    expand("variants/{sample}_second_pass_raw.vcf", sample=SAMPLES)
#     output:
#    "database/gvcf"
#     params:
#    files = lambda wildcards, input: " -V ".join(input)
#     shell:
#    "{GATK} GenomicsDBImport -V {params.files} --genomicsdb-workspace-path {output} --intervals NC_024711.1"

