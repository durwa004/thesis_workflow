#Create bed file for gc mask (of X chromosome and unmapped contigs)
with open("GCF_002863925.1_EquCab3.0_genomic.fasta.fai", "r") as input_file:
    with open("GCF_002863925.1_EquCab3.0_genomic.gcmask.bed" ,"w") as output_file:
        for line in input_file:
            line = line.rstrip("\n").split("\t")
            a = line[0].split("_")
            if "009175.3" in a[1] or "001640.1" in a[1] or "NW" in a[0]:
                print(line[0], "1", line[1], file = output_file, sep = "\t")

#Create bed file for overall sequencing depth estimation - just autosomes
with open("GCF_002863925.1_EquCab3.0_genomic.fasta.fai", "r") as input_file:
    with open("GCF_002863925.1_EquCab3.0_genomic.rdmask.bed" ,"w") as output_file:
        for line in input_file:
            line = line.rstrip("\n").split("\t")
            if "NC_009175.3" in line or "NC_001640.1" in line:
                next
            elif line[0].startswith("NW_"):
                next
            else:
                print(line[0], "1", line[1], file = output_file, sep = "\t")
