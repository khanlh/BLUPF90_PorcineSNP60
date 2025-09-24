## BLUPF90 Porcine SNP60
### Dataset

This repository provides a working example of using BLUPF90 with the public dataset from:

Cleveland, M.A., Hickey, J.M., & Forni, S. (2012). A Common Dataset for Genomic Analysis of Livestock Populations. G3: Genes, Genomes, Genetics, 2(4), 429–435.
https://doi.org/10.1534/g3.111.001453

The dataset (PorcineSNP60) includes:

  - pedigree.txt — pedigree file (ID,SIRE,DAM)
  - phenotypes.txt — five anonymized continuous traits (t1–t5)
  - genotypes.txt — PorcineSNP60 SNP genotypes
  - ebvs.txt — example EBVs and accuracies


    ** Note: Traits t1–t5 are anonymized in the original paper. They are continuous quantitative traits with varying heritability. The exact biological meaning is not disclosed.








## Theory of Options and `accf90` in BLUPF90 Family

## Theory of Options for `renumf90`, `airemlf90`, and `blupf90`:

### 1. `OPTION missing -9999`
- **Purpose**: This option specifies that `-9999` will be treated as the **missing value** in the input data. Any data entry with the value `-9999` will be considered missing and excluded from the analysis.
- **Application**: This is useful when you have missing data in your phenotype dataset, and you want to exclude those records from the analysis.

### 2. `OPTION method VCE`
- **Purpose**: This option selects the **Variance Component Estimation (VCE)** method for estimating variance components in the genetic model. The VCE method is commonly used for estimating genetic, environmental, and residual variances in animal breeding.
- **Application**: It is typically used in `airemlf90` when you need to estimate the genetic variance components for a specific trait or set of traits.

### 3. `OPTION conv_crit 1d-12`
- **Purpose**: This option specifies the **convergence criterion** for the algorithm. The `1d-12` value means that the algorithm will stop once the change between iterations is smaller than `1e-12`.
- **Application**: This ensures that the algorithm converges to a high precision level before terminating, which is essential for obtaining reliable estimates in complex models.

### 4. `OPTION use_yams`
- **Purpose**: This option instructs the program to use **YAMS (Yet Another MME Solver)**, a specialized solver for large matrix equations often used in genetic analysis programs.
- **Application**: When running `airemlf90` or `blupf90`, using YAMS can improve performance by providing a more efficient method to solve the large systems of equations involved in mixed model estimation.

### 5. `OPTION saveGInve2se`
- **Purpose**: This option tells the program to save the **inverse of the genetic relationship matrix (G)**. The G-matrix is crucial for genetic evaluations as it describes the genetic relationships between individuals.
- **Application**: Useful if you need to store or analyze the inverse G-matrix for further genetic or breeding analysis.

### 6. `OPTION maxrounds 1000`
- **Purpose**: This option specifies the **maximum number of iterations** the algorithm will run before terminating. If convergence is not achieved within these iterations, the program will stop.
- **Application**: This is useful to prevent the program from running indefinitely in case convergence is not reached within a reasonable number of iterations.

### 7. `OPTION blksize 1`
- **Purpose**: This option defines the **block size** for matrix operations. Specifically, `blksize 1` means each block in matrix operations contains just one element.
- **Application**: This setting can affect the memory usage and performance. For large datasets, adjusting the block size may help optimize computation efficiency.

---
