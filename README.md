## BLUPF90 Porcine SNP60 Example

### Dataset

This repository provides a working example of using **BLUPF90** with the public dataset from:

Cleveland, M.A., Hickey, J.M., & Forni, S. (2012).  
*A Common Dataset for Genomic Analysis of Livestock Populations.*  
G3: Genes, Genomes, Genetics, 2(4), 429–435.  
https://doi.org/10.1534/g3.111.001453

The dataset (**PorcineSNP60**) includes:

- `pedigree.txt` — pedigree file (ID, SIRE, DAM)  
- `phenotypes.txt` — five anonymized continuous traits (t1–t5)  
- `genotypes.txt` — PorcineSNP60 SNP genotypes  
- `ebvs.txt` — example EBVs and accuracies  

**Note:** Traits t1–t5 are anonymized in the original paper. They are continuous quantitative traits with varying heritability, but the exact biological meaning is not disclosed.

---

## Theory of Variance Component Estimation (VCE)

**Variance Component Estimation (VCE)** partitions the total variance of a trait into its components, helping us quantify the contribution of genetic vs. environmental effects. This is central to animal breeding and quantitative genetics.

### Why VCE is Important
1. **Genetic Analysis** – quantifies the genetic contribution to traits.  
2. **Heritability Estimation** – provides estimates of \( h^2 \).  
3. **Selection Decisions** – informs breeding strategies by identifying traits with stronger genetic control.  

### How VCE Works
- Based on the **mixed linear model (LMM)** framework.  
- Uses both fixed and random effects.  
- Solves systems of equations using REML (Restricted Maximum Likelihood), as implemented in `airemlf90`.  

### Output of VCE
- Additive genetic variance (\( \sigma^2_G \))  
- Residual variance (\( \sigma^2_E \))  
- Total phenotypic variance (\( \sigma^2_P \))  
- Heritability (\( h^2 \))  

---

## Calculating Heritability

Heritability (\( h^2 \)) is defined as:

$$
h^2 = \frac{\sigma^2_G}{\sigma^2_P}
$$

Where:

- \( \sigma^2_G \): additive genetic variance  
- \( \sigma^2_P \): total phenotypic variance  

The phenotypic variance can be decomposed as:

$$
\sigma^2_P = \sigma^2_G + \sigma^2_E
$$

with \( \sigma^2_E \) being the residual (environmental + unexplained) variance.

---

### Example Calculation

Suppose the `airemlf90` output contains:

```plaintext
Additive genetic variance: 0.25
Residual variance: 0.15
Total phenotypic variance: 0.40

