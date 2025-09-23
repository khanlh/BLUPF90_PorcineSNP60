# BLUPF90 Porcine SNP60

## Dataset

This repository provides a working example of using **BLUPF90** with the public dataset from:

> Cleveland, M.A., Hickey, J.M., & Forni, S. (2012). *A Common Dataset for Genomic Analysis of Livestock Populations.* G3: Genes, Genomes, Genetics, 2(4), 429–435.  
> https://doi.org/10.1534/g3.111.001453

The dataset (PorcineSNP60) includes:
- `pedigree.txt` — pedigree file (`ID,SIRE,DAM`)
- `phenotypes.txt` — five anonymized continuous traits (`t1–t5`)
- `genotypes.txt` — PorcineSNP60 SNP genotypes
- `ebvs.txt` — example EBVs and accuracies

> ⚠️ Traits `t1–t5` are anonymized in the original paper. They are continuous quantitative traits with varying heritability. The exact biological meaning is not disclosed.

---

## Workflow

1. **Prepare inputs**
   ```bash
   Rscript scripts/prepare_inputs.R
   ```

   This will create BLUPF90-compatible pedigree and phenotype files in `data/processed/`.

2. **Run renumf90**
   ```bash
   renumf90 < blupf90_pars/renum.par
   ```

3. **Run airemlf90** (variance components)
   ```bash
   airemlf90 < blupf90_pars/aireml.par
   ```

4. **Run blupf90** (prediction of EBVs)
   ```bash
   blupf90 < blupf90_pars/blup.par
   ```

---

## Example `renum.par`

```txt
DATAFILE
../data/processed/phenotypes.dat

TRAITS
2 3 4 5 6

FIELDS_PASSED TO OUTPUT
1

WEIGHT(S)
1 1 1 1 1

RESIDUAL_VARIANCE
1

EFFECT
2 cross

EFFECT
3 cross

EFFECT
4 cross

EFFECT
5 cross

EFFECT
6 cross

EFFECT
7 cross alpha

PEDFILE
../data/processed/pedigree.ped

PED_DEPTH
3

OPTION SNP_file ../data/raw/genotypes.txt
OPTION no_quality_control
OPTION save_renum_id
```

---

## Notes
- `TRAITS 2 3 4 5 6` assumes first column is ID, followed by 5 traits.
- Each trait is modeled as random additive genetic effect.
- You may adapt fixed effects if additional covariates are available.
- `genotypes.txt` must be in BLUPF90 SNP format.
- `OPTION save_renum_id` will produce `renaddxx.ped` and `renaddxx.dat` files for downstream programs.

---

## References
- BLUPF90 suite: http://nce.ads.uga.edu/wiki/doku.php?id=blupf90
- Original dataset publication: Cleveland et al., 2012, G3.

