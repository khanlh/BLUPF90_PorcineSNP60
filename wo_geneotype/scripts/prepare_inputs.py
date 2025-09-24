#!/usr/bin/env python3
# prepare_inputs.py
# Convert raw pedigree.txt and phenotypes.txt into BLUPF90 format

import pandas as pd
import os

# Paths
ped_file = "/mnt/c/Users/ddevkhan/Documents/blupf90/pig/PorcineSNP60_Common_Dataset/data/raw/pedigree.txt"
pheno_file = "/mnt/c/Users/ddevkhan/Documents/blupf90/pig/PorcineSNP60_Common_Dataset/data/raw/phenotypes.txt"
out_dir = "/mnt/c/Users/ddevkhan/Documents/blupf90/pig/PorcineSNP60_Common_Dataset/data/processed"
out_ped = os.path.join(out_dir, "pedigree.ped")
out_pheno = os.path.join(out_dir, "phenotypes.dat")

# Make output dir
os.makedirs(out_dir, exist_ok=True)


# --- Phenotypes ---
pheno = pd.read_csv(pheno_file, dtype=str, keep_default_na=False, na_filter=False)

expected_cols = ["ID", "t1", "t2", "t3", "t4", "t5"]
pheno = pheno.reindex(columns=expected_cols)

# Thay '.' hoặc rỗng thành -9999
pheno = pheno.replace(".", "-9999")
pheno = pheno.fillna("-9999")

# Xuất: luôn đủ 6 cột, NA = -9999
pheno.to_csv(out_pheno, sep=" ", index=False, header=False)

print("Files written:")
print(" -", out_ped)
print(" -", out_pheno)
