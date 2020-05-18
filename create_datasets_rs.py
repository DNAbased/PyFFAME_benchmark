import pandas as pd

variants = pd.read_csv('rs_10k_random_SNPs.txt', sep='\t', header=None)
insertions = pd.read_csv('rs_1k_random_insertions.txt', sep='\t', header=None)
deletions = pd.read_csv('rs_1k_random_deletions.txt', sep='\t', header=None)

def create_dataset(var_df, in_df, del_df, n):
    new_df = var_df.head(int(n*0.9)).append([in_df.head(int(n*0.05)), del_df.head(int(n*0.05))])
    return(new_df)

create_dataset(variants, insertions, deletions, 100).to_csv('00100_dataset_rs.txt', sep='\t', header=False, index=False)
create_dataset(variants, insertions, deletions, 500).to_csv('00500_dataset_rs.txt', sep='\t', header=False, index=False)
create_dataset(variants, insertions, deletions, 1000).to_csv('01000_dataset_rs.txt', sep='\t', header=False, index=False)
create_dataset(variants, insertions, deletions, 3000).to_csv('03000_dataset_rs.txt', sep='\t', header=False, index=False)
create_dataset(variants, insertions, deletions, 5000).to_csv('05000_dataset_rs.txt', sep='\t', header=False, index=False)
create_dataset(variants, insertions, deletions, 10000).to_csv('10000_dataset_rs.txt', sep='\t', header=False, index=False)
