# mRNA Vaccine Quality Analysis (Reproducibility Study)

This repository explores mRNA vaccine quality control using the [Mana software toolkit](https://github.com/scchess/Mana).  
Mana was applied to analyze long-read Oxford Nanopore sequencing data for key metrics such as read length distribution, mapping rates, and poly(A) tail length.  

In addition to running Mana, I contributed a custom Python script (`analyze_mRNA.py`) that extends the workflow with further downstream analyses, visualizations, and statistics.  
This project demonstrates how computational tools can provide deeper insights into mRNA vaccine stability and integrity.

---
##  Project Tree
Mana/
├── README.md                  # Project overview
├── LICENSE                    # MIT license
├── .gitignore                 # Ignore temp/large files
│
├── data/                      # Data files
│   ├── raw/                   # Raw FASTQ/BAM or instructions
│   └── processed/             # Processed outputs
│
├── scripts/                   # Python scripts
│   ├── analyze_mRNA.py        # Main analysis script
│   └── helper_functions.py    # Utility functions
│
├── notebooks/                 # Jupyter notebooks
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_mana_analysis.ipynb
│   └── 03_visualizations.ipynb
│
├── results/                   # Outputs
│   ├── figures/               # Plots & images
│   └── tables/                # Summary tables
│
└── docs/                      # Supporting docs
├── final_presentation.pdf # BINF6310 presentation
├── reference_paper.pdf    # Nature Communications paper
└── reproducibility_notes.md

---

## Repository Structure
- `data/` → raw datasets  
- `scripts/` → analysis scripts (e.g., `analyze_mRNA.py`)  
- `notebooks/` → step-by-step Jupyter workflows  
- `results/` → figures and summary tables  
- `docs/` → supporting files (final presentation, reference paper)

---

##  Methods
- **Sequencing Platform**: Oxford Nanopore long-read sequencing  
- **Tools Used**:
  - [Mana](https://github.com/scchess/Mana) for automated QC
  - Custom Python scripts (`analyze_mRNA.py`) for mapping and poly(A) analysis
  - IGV for visual inspection of read alignments
- **Metrics Assessed**:
  - Sequence integrity (full-length transcripts vs truncations)
  - Mapping rate (alignment success to reference)
  - Read length distribution (fragmentation vs consistency)
  - Poly(A) tail length (stability & translational efficiency)

---

##  Results (Detailed Summary)

Our reproducibility analysis confirmed the findings of the original paper:

### 1. Read Length Distribution
- **Unmodified mRNA**:
  - Strong fragmentation observed.
  - Most reads fall between **100–400 nt**, with multiple small peaks.
  - Average read length: **142.61 nt**.
- **Modified mRNA (N1-methylpseudouridine substitution)**:
  - Clear, consistent peak around **1200–1400 nt**, representing full-length transcripts.
  - Average read length: **1007.54 nt**.
- **Interpretation**: Chemical modification dramatically improves transcript stability and integrity.

### 2. Poly(A) Tail Analysis
- Consistent primary peak at ~**125 nt** across replicates.  
- Individual sample averages:
  - S1: 124.75 nt  
  - S2: 125.90 nt  
  - S3: 124.44 nt  
- **Interpretation**: Highly reproducible poly(A) tail measurements indicate robust library preparation and sequencing accuracy.

### 3. Mapping Rate
- Modified mRNA: **~99.63%**  
- Unmodified mRNA: **~81.26%**  
- **Interpretation**: Higher mapping success in modified samples reflects better sequence fidelity and fewer truncated/degraded reads.

### 4. Insights
- Long-read nanopore sequencing is effective for **capturing full mRNA molecules**, including poly(A) tails.  
- Visualization tools like IGV + Mana make QC faster and more reproducible.  
- Modified mRNA shows **superior sequence integrity**, validating its role in mRNA vaccines.  

---

##  Significance
This project demonstrates:
- How long-read QC workflows (like VAX-seq + Mana) can replace fragmented traditional QC assays.  
- That reproducibility studies are essential to confirm **scalability and robustness** for clinical mRNA production.  
- Future improvements may involve error-correction algorithms and optimized nanopore chemistries.

---

##  References
1. Gunter H.M. et al. *mRNA vaccine quality analysis using RNA sequencing*. **Nature Communications** (2023). [Link](https://doi.org/10.1038/s41467-023-41354-y)  
2. [Mana software GitHub repository](https://github.com/scchess/Mana)

---

##  Contributors
- Pratham Donda (@PrathamD-11)  

