# Scanpy scRNA-seq Analysis (GSE171524)

This repository contains Python code for analyzing single-cell RNA-seq data using **Scanpy**. The workflow focuses on preprocessing, quality control, dimensionality reduction, clustering, and downstream analysis of publicly available GEO data.

---

## 📌 Project Overview

The goal of this project is to demonstrate a reproducible Scanpy-based scRNA-seq analysis workflow. The repository is designed to be lightweight and reproducible by separating **code** from **large raw data files**.

Key steps include:

* Loading raw count matrices
* Quality control (cell and gene filtering)
* Normalization and log-transformation
* Identification of highly variable genes
* Dimensionality reduction (PCA, UMAP)
* Clustering and visualization

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
