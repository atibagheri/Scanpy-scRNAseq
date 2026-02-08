# Scanpy scRNA-seq Analysis (GSE171524)

This repository contains Python code for analyzing single-cell RNA-seq data using **Scanpy**. The workflow focuses on preprocessing, quality control, dimensionality reduction, clustering, and downstream analysis of publicly available GEO data.

---

## 📌 Project Overview

The goal of this project is to demonstrate a reproducible Scanpy-based scRNA-seq analysis workflow. The repository is designed to be lightweight and reproducible by separating **code** from **large raw data files**.

Key steps include:

**Key steps include:**

- **Loading raw count matrices**  
  Import the scRNA-seq data (e.g., `.h5ad` or `.mtx` files) into an `AnnData` object for analysis.

- **Quality control (cell and gene filtering)**  
  Remove low-quality cells and genes with low expression to improve downstream analysis.

- **Normalization and log-transformation**  
  Normalize counts to account for sequencing depth and transform to log scale for comparability.

- **Identification of highly variable genes**  
  Select genes that capture the most biological variation, which improves dimensionality reduction and clustering.

- **Dimensionality reduction (PCA, UMAP)**  
  Reduce the dataset’s complexity using principal component analysis (PCA) and visualize cells in 2D space using UMAP.

- **Clustering and visualization**  
  Group cells into clusters based on transcriptional similarity and visualize results using UMAP or t-SNE plots.

- **Integration**  
  Combine multiple datasets or batches to correct for batch effects and allow joint analysis of different samples.

- **Analysis**  
  Explore biological patterns in clusters, cell types, or conditions using various downstream analyses.

- **Counting cells**  
  Quantify the number of cells per cluster or per condition for summary statistics and comparison.

- **Differential expression (DE) analysis**  
  Identify genes that are significantly up- or down-regulated between clusters, conditions, or cell types.

- **Gene Ontology (GO) enrichment**  
  Perform functional enrichment analysis on DE genes to interpret their biological significance.

- **Scoring gene signatures**  
  Calculate signature scores for predefined gene sets to assess pathway activity or cell states across clusters.

---

## 📊 Data Source

The scRNA-seq data used in this project are publicly available from **NCBI GEO**:

* **Accession:** GSE171524
* **Link:** [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE171524](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE171524)

⚠️ **Note:** Raw data files (~400 MB) are **not included** in this repository due to GitHub file size limits.

---

## 📥 Downloading the Data

A helper script is provided to download the raw data directly from GEO.

```bash
python scripts/download_data.py
```

This will:

1. Create a `data/` directory
2. Download the GEO supplementary files
3. (Optionally) extract compressed archives

The `data/` directory is ignored by git.

---

## 📁 Repository Structure

```
Scanpy-scRNAseq/
├── scripts/
│   └── download_data.py
├── data/              # raw data (not tracked)
├── single_cell_analysis.py
├── README.md
├── requirements.txt
└── 
```

---

## 🧪 Requirements

* Python >= 3.9
* scanpy
* scvi-tools
* anndata
* numpy
* pandas
* matplotlib
* seaborn

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

After downloading the data, run:

```bash
python single_cell_analysis.py
```

Or explore the analysis interactively (if using notebooks).

---

## 🔁 Reproducibility Notes

* Large raw datasets are intentionally excluded from version control
* All data sources are publicly available
* Scripts are written to be modular and reproducible

This structure follows best practices for bioinformatics and scRNA-seq projects.

---

## 👤 Author

**Atefeh Bagheri**
PhD candidates | Computational Biology / Bioinformatics

---

## 📄 License

This project is for research and educational purposes. Please cite the original GEO dataset if reusing the data.
