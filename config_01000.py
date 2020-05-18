# config file for the allelic-MPRA design pipeline

# INPUT
# input file containing rsIDs
in_variant = './01000_dataset.rs' #'./testfiles/01_input_rs.txt'
# rsid file has header
in_header = 0
# input file in vcf format
in_vcf = None # './testfiles/02_input_vcf.txt'
# input file containing finished sequences
in_sequence = None # './testfiles/03_input_seq.txt'
# input file containing the barcodes to be used
in_barcode = './nt11_barcodes.json'
# barcode file type [txt (list/tsv), json]?
in_barcode_type = 'json'
# barcode file has header (if list input)
in_bc_header = 0

# DATABASE
db_host = 'localhost'
db_port = 27017
db_timeout = 2500
db_database = 'dbsnp_b151'
# 'standard' variants
db_collection_rs = 'rs'
# merged variants
db_collection_merged = 'merged'
# authentication file
db_auth = 'mongodb_auth.py'
# genome for use with pyfaidx.Fasta()
db_genome = './hs37d5.fa'

# DESIGN
# design order
de_order = 'abcde'
# added sequence 1 (default: five primer seq)
de_seq_1 = 'AGGACCGGATCAACT'
# added sequence 2 (default: spacer)
de_seq_2 = 'CCTGCAGGGAATTC'
# added sequence 3 (default: three prime seq)
de_seq_3 = 'CATTGCGTGAACCGA'

# SETTINGS
# feature size
set_feature_size = 85
# create all allelic features (1) or only reference features (0)
set_all_features = 1
# discard indels larger than this # can be used to remove all indels (1)
set_indel_max_length = 100
# only create full length features (else: account for different length of indels by creating multiple features (two ref for insertions, two alt for deletions))
set_indel_features = 0
# barcodes added to each distinct feature (e.g. ref and alt, each)
set_barcodes_per_feature = 100
# create reverse complementary versions of all features?
set_rev_comp = 0

# ENZYMES
# enzyme file (processed)
enz_file_processed = './enzymes_processed.csv'
# enzyme file (NEB REBASE format)
enz_file = './enzymes_new.txt'
# all enzymes used
enz_used = 'EcoRI,SbfI'
# OR: all relevant cut sites (only used if 'enz_used = None'; should be a regex list) --> e.g. ['AGTACT', 'CC[AT]GG']
enz_sites = "['GAATTC', 'CCTGCAGG']"
# total restriction sites expected (in final feature)
enz_cumul_cuts = 2
# total restriction sites expected (in barcode plus the sequence before and after it)
enz_cumul_cuts_bc = 2

# OUTPUT
# output as json or tsv
out_format = 'json'
# path to output
out_output = './mpra_design'
# path to logfile created during script execution
out_logfile = './logfile.txt'
