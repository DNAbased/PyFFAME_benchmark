library(biomaRt)
library(splitstackshape)
library(tidyverse)
library(mpradesigntools)

# where to get the snp information from
rsid_mart = useMart(biomart = 'ENSEMBL_MART_SNP', dataset = 'hsapiens_snp')

# load rsid datasets
rs_00100 = read.table("00100_dataset.rs", sep="\t", stringsAsFactors=FALSE)
rs_00500 = read.table("00500_dataset.rs", sep="\t", stringsAsFactors=FALSE)
rs_01000 = read.table("01000_dataset.rs", sep="\t", stringsAsFactors=FALSE)
rs_03000 = read.table("03000_dataset.rs", sep="\t", stringsAsFactors=FALSE)
rs_05000 = read.table("05000_dataset.rs", sep="\t", stringsAsFactors=FALSE)
rs_10000 = read.table("10000_dataset.rs", sep="\t", stringsAsFactors=FALSE)

# get snp information
vcf_00100 = getBM(attributes = c('refsnp_id', 'chr_name', 'chrom_start', 'allele'), filters = c('snp_filter'), values = rs_00100$V1, mart = rsid_mart)
vcf_00500 = getBM(attributes = c('refsnp_id', 'chr_name', 'chrom_start', 'allele'), filters = c('snp_filter'), values = rs_00500$V1, mart = rsid_mart)
vcf_01000 = getBM(attributes = c('refsnp_id', 'chr_name', 'chrom_start', 'allele'), filters = c('snp_filter'), values = rs_01000$V1, mart = rsid_mart)
vcf_03000 = getBM(attributes = c('refsnp_id', 'chr_name', 'chrom_start', 'allele'), filters = c('snp_filter'), values = rs_03000$V1, mart = rsid_mart)
vcf_05000 = getBM(attributes = c('refsnp_id', 'chr_name', 'chrom_start', 'allele'), filters = c('snp_filter'), values = rs_05000$V1, mart = rsid_mart)
vcf_10000 = getBM(attributes = c('refsnp_id', 'chr_name', 'chrom_start', 'allele'), filters = c('snp_filter'), values = rs_10000$V1, mart = rsid_mart)

# split 'allele' column
vcf_00100 = cSplit(vcf_00100, 'allele', sep='/', type.convert=FALSE)
vcf_00500 = cSplit(vcf_00500, 'allele', sep='/', type.convert=FALSE)
vcf_01000 = cSplit(vcf_01000, 'allele', sep='/', type.convert=FALSE)
vcf_03000 = cSplit(vcf_03000, 'allele', sep='/', type.convert=FALSE)
vcf_05000 = cSplit(vcf_05000, 'allele', sep='/', type.convert=FALSE)
vcf_10000 = cSplit(vcf_10000, 'allele', sep='/', type.convert=FALSE)

# rename columns
colnames(vcf_00100) = c('ID', 'CHROM', 'POS', 'REF', 'ALT1', 'ALT2','ALT3')
colnames(vcf_00500) = c('ID', 'CHROM', 'POS', 'REF', 'ALT1', 'ALT2','ALT3')
colnames(vcf_01000) = c('ID', 'CHROM', 'POS', 'REF', 'ALT1', 'ALT2','ALT3')
colnames(vcf_03000) = c('ID', 'CHROM', 'POS', 'REF', 'ALT1', 'ALT2','ALT3','ALT4','ALT5','ALT6')
colnames(vcf_05000) = c('ID', 'CHROM', 'POS', 'REF', 'ALT1', 'ALT2','ALT3','ALT4','ALT5','ALT6','ALT7','ALT8')
colnames(vcf_10000) = c('ID', 'CHROM', 'POS', 'REF', 'ALT1', 'ALT2','ALT3','ALT4','ALT5','ALT6','ALT7','ALT8')

# prepare concatenation of alt alleles
vcf_00100[is.na(vcf_00100)] <- ""
vcf_00500[is.na(vcf_00500)] <- ""
vcf_01000[is.na(vcf_01000)] <- ""
vcf_03000[is.na(vcf_03000)] <- ""
vcf_05000[is.na(vcf_05000)] <- ""
vcf_10000[is.na(vcf_10000)] <- ""

# concatenate alt alleles
vcf_00100$ALT = paste(vcf_00100$ALT1, vcf_00100$ALT2, vcf_00100$ALT3, sep=',')
vcf_00500$ALT = paste(vcf_00500$ALT1, vcf_00500$ALT2, vcf_00500$ALT3, sep=',')
vcf_01000$ALT = paste(vcf_01000$ALT1, vcf_01000$ALT2, vcf_01000$ALT3, sep=',')
vcf_03000$ALT = paste(vcf_03000$ALT1, vcf_03000$ALT2, vcf_03000$ALT3, vcf_03000$ALT4, vcf_03000$ALT5, vcf_03000$ALT6, sep=',')
vcf_05000$ALT = paste(vcf_05000$ALT1, vcf_05000$ALT2, vcf_05000$ALT3, vcf_05000$ALT4, vcf_05000$ALT5, vcf_05000$ALT6, vcf_05000$ALT7, vcf_05000$ALT8, sep=',')
vcf_10000$ALT = paste(vcf_10000$ALT1, vcf_10000$ALT2, vcf_10000$ALT3, vcf_10000$ALT4, vcf_10000$ALT5, vcf_10000$ALT6, vcf_10000$ALT7, vcf_10000$ALT8, sep=',')

# remove other columns
vcf_00100 = vcf_00100 %>% select(CHROM, ID, POS, REF, ALT)
vcf_00500 = vcf_00500 %>% select(CHROM, ID, POS, REF, ALT)
vcf_01000 = vcf_01000 %>% select(CHROM, ID, POS, REF, ALT)
vcf_03000 = vcf_03000 %>% select(CHROM, ID, POS, REF, ALT)
vcf_05000 = vcf_05000 %>% select(CHROM, ID, POS, REF, ALT)
vcf_10000 = vcf_10000 %>% select(CHROM, ID, POS, REF, ALT)

# remove commas
vcf_00100$ALT = gsub("^,*|(?<=,),|,*$", "", vcf_00100$ALT, perl=TRUE)
vcf_00500$ALT = gsub("^,*|(?<=,),|,*$", "", vcf_00500$ALT, perl=TRUE)
vcf_01000$ALT = gsub("^,*|(?<=,),|,*$", "", vcf_01000$ALT, perl=TRUE)
vcf_03000$ALT = gsub("^,*|(?<=,),|,*$", "", vcf_03000$ALT, perl=TRUE)
vcf_05000$ALT = gsub("^,*|(?<=,),|,*$", "", vcf_05000$ALT, perl=TRUE)
vcf_10000$ALT = gsub("^,*|(?<=,),|,*$", "", vcf_10000$ALT, perl=TRUE)

# set necessary info column
vcf_00100$INFO = 0
vcf_00500$INFO = 0
vcf_01000$INFO = 0
vcf_03000$INFO = 0
vcf_05000$INFO = 0
vcf_10000$INFO = 0

# remove non-chromosomal positions (e.g.'CHR_HG1362_PATCH')
vcf_00100 = vcf_00100 %>% filter(nchar(CHROM)<=2) # 100 of 100 remaining
vcf_00500 = vcf_00500 %>% filter(nchar(CHROM)<=2) # 500 of 500 remaining
vcf_01000 = vcf_01000 %>% filter(nchar(CHROM)<=2) # 999 of 1,000 remaining
vcf_03000 = vcf_03000 %>% filter(nchar(CHROM)<=2) # 2,992 of 3,000 remaining
vcf_05000 = vcf_05000 %>% filter(nchar(CHROM)<=2) # 4,988 of 5,000 remaining
vcf_10000 = vcf_10000 %>% filter(nchar(CHROM)<=2) # 9,977 of 10,000 remaining

# write vcfs for design function
write.table(vcf_00100, 'vcf_00100.vcf', row.names=FALSE, sep='\t', quote=FALSE)
write.table(vcf_00500, 'vcf_00500.vcf', row.names=FALSE, sep='\t', quote=FALSE)
write.table(vcf_01000, 'vcf_01000.vcf', row.names=FALSE, sep='\t', quote=FALSE)
write.table(vcf_03000, 'vcf_03000.vcf', row.names=FALSE, sep='\t', quote=FALSE)
write.table(vcf_05000, 'vcf_05000.vcf', row.names=FALSE, sep='\t', quote=FALSE)
write.table(vcf_10000, 'vcf_10000.vcf', row.names=FALSE, sep='\t', quote=FALSE)

# process vcf # might have to set barcode_set=`barcodes16-1` to have enough barcodes?
processVCF('vcf_00100.vcf', 1, 85, 85, 'ACTGGCCAG', 'CTCGGCGGCC', ensure_all_4_nuc=FALSE)
processVCF('vcf_05000.vcf', 100, 85, 85, 'ACTGGCCAG', 'CTCGGCGGCC', outPath='mpra.tsv', barcode_set=`barcodes16-1`)

# more barcodes (all possible 11mers)
my_barcodes = read.table("eleven.tsv", sep="\t", stringsAsFactors=FALSE)
my_barcodes = as.vector(my_barcodes$V1)

# timing (seconds); will always abort prematurely due to an error in the mpradesigntools code 
# 100 variants
# 143; 140; 138; 134; 127
system.time(processVCF('vcf_00100.vcf', 100, 85, 85, 'ACTGGCCAG', 'CTCGGCGGCC', ensure_all_4_nuc=FALSE, barcode_set=my_barcodes))

# 500 variants
# 582; 559; 553; 557; 559
system.time(processVCF('vcf_00500.vcf', 100, 85, 85, 'ACTGGCCAG', 'CTCGGCGGCC', ensure_all_4_nuc=FALSE, barcode_set=my_barcodes))

# 1k variants
# 1,125; 1,091; 1,096; 1,104; 1,110
system.time(processVCF('vcf_01000.vcf', 100, 85, 85, 'ACTGGCCAG', 'CTCGGCGGCC', ensure_all_4_nuc=FALSE, barcode_set=my_barcodes))

# 3k variants
# 3,584; 3,468; 3,462; 3,475; 3,454
system.time(processVCF('vcf_03000.vcf', 100, 85, 85, 'ACTGGCCAG', 'CTCGGCGGCC', ensure_all_4_nuc=FALSE, barcode_set=my_barcodes))

# 5k variants
# 6,468; 6,090; 6,140; 6,223; 6,113
system.time(processVCF('vcf_05000.vcf', 100, 85, 85, 'ACTGGCCAG', 'CTCGGCGGCC', ensure_all_4_nuc=FALSE, barcode_set=my_barcodes))

# 10k variants
# 14,180; 13,930; 14,100; 16,010; 14,070
system.time(processVCF('vcf_10000.vcf', 100, 85, 85, 'ACTGGCCAG', 'CTCGGCGGCC', ensure_all_4_nuc=FALSE, barcode_set=my_barcodes))
