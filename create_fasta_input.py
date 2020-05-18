import pandas as pd
from pyfaidx import Fasta

vcf_00100 = pd.read_csv('00100_dataset_split.vcf', sep='\t')
vcf_00500 = pd.read_csv('00500_dataset_split.vcf', sep='\t')
vcf_01000 = pd.read_csv('01000_dataset_split.vcf', sep='\t')
vcf_03000 = pd.read_csv('03000_dataset_split.vcf', sep='\t')
vcf_05000 = pd.read_csv('05000_dataset_split.vcf', sep='\t')
vcf_10000 = pd.read_csv('10000_dataset_split.vcf', sep='\t')

def get_fasta(df, output, genome='../../hs37d5.fa', n=85):
    for i in df.index:
        sequence = Fasta(genome)[str(df.at[i, 'CHROM'])][(df.at[i, 'POS'] - (n + 1)):(df.at[i, 'POS'] + n)]
        with open(output, 'a') as f:
            f.write('>sequence' + str(i+1) + 'chr' + sequence.fancy_name + ',id' + str(i+1) + '\n')
            f.write(sequence.seq + '\n')

get_fasta(vcf_00100, output='context_00100.fa')
get_fasta(vcf_00500, output='context_00500.fa')
get_fasta(vcf_01000, output='context_01000.fa')
get_fasta(vcf_03000, output='context_03000.fa')
get_fasta(vcf_05000, output='context_05000.fa')
get_fasta(vcf_10000, output='context_10000.fa')
