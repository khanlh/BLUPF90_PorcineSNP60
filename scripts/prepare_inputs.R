#!/usr/bin/env Rscript

# prepare_inputs.R
# Convert raw pedigree.txt and phenotypes.txt into BLUPF90 format

library(data.table)

# Paths (adjust if needed)
ped_file <- "data/raw/pedigree.txt"
pheno_file <- "data/raw/phenotypes.txt"
out_ped <- "data/processed/pedigree.ped"
out_pheno <- "data/processed/phenotypes.dat"

# Create output dir
dir.create("data/processed", showWarnings = FALSE, recursive = TRUE)

# --- Pedigree ---
ped <- fread(ped_file, header = TRUE)
# BLUPF90 requires space-separated, unknown parents = 0
# Keep as is, remove header
fwrite(ped, out_ped, sep = " ", col.names = FALSE, quote = FALSE, na = "0")

# --- Phenotypes ---
pheno <- fread(pheno_file, header = TRUE)
# Replace '.' with NA
for (j in 2:ncol(pheno)) {
  pheno[[j]][pheno[[j]] == "."] <- NA
}
# Write space-separated, no header, missing = blank
fwrite(pheno, out_pheno, sep = " ", col.names = FALSE, quote = FALSE, na = "")

cat("Files written:\n", out_ped, "\n", out_pheno, "\n")
