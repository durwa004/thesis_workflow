import os
import gzip
import argparse
import subprocess

def union_VEPs(snpeff_dir,annovar_dir):
    '''
    Takes in directory containing output files for SnpEff and another for 
    ANNOVAR. Output = union of coding variants and intersect of coding 
    variants file.
    '''
    for filename in os.listdir(snpeff_dir):
        tmp = []
        if filename.endswith(".coding.ann.vcf.gz"):
            a = filename.split("_snpeff_intersect.coding.ann.vcf.gz")
            tmp.append(a)

    
    for i in tmp:
       with gzip.open(i + "_snpeff_intersect.coding.ann.vcf.gz", "rt") as snpeff:
            with open(annovar_dir + i + "_annovar_intersect.exonic_variant_function", "r") as annovar:
                with open(i + "_intersect_VEP_union.txt", "w") as output_file:
                    for line in snpeff:
                       line = line.rstrip("\n").split("\t") 
                       if "#" in line[0]:
                           if "#CHROM" in line[0]:
                               print("\t".join(line), file = output_file
                           else:
                               continue
                       else:
                            chrom,pos,*_ = line.rstrip("\n").split("\t")
                                else:
                                    if "HIGH" in line[7]:
                                        print("\t".join(line), file = high_output)
                                    elif "MODERATE" in line[7]:
                                        print("\t".join(line), file = mod_output)
                                    elif "LOW" in line[7]:
                                        print("\t".join(line), file = low_output)
    concatenate_sh = "cat " + disease_name + "/" + disease_name + "_high.txt " + disease_name + "/" + disease_name + "_mod.txt " + disease_name + "/" + disease_name + "_low.txt > " + disease_name + "/" + disease_name +"_coding.txt"
    subprocess.run(concatenate_sh, shell=True)
#    rv = subprocess.run(concatenate_sh, shell=True, capture_output=True)
#    if rv.returncode !=0:
#        print("WARNING: ", concatenate_sh)

#Instructions for running on the command line
if __name__ == '__main__':
    '''
        If the script is run from the command line, 
    '''
    try:
        parser = argparse.ArgumentParser(description='Extract list of candidate genes from vcf')
        parser.add_argument('--disease_name', help='name of disease that the candidate genes are for')
        args = parser.parse_args()
        extract_coding_variants(args.disease_name)
    except Exception as e:
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print("A bad thing happened: {}".format(e))
        print('Please see the command usage below:\n\n\n')
        print(parser.print_help())
