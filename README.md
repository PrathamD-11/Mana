# mRNA Vaccine Quality Analysis (Reproducibility Study)

This repository reproduces and extends analyses from  
**"mRNA vaccine quality analysis using RNA sequencing" (Gunter et al., Nature Communications, 2023)**  
and builds upon the [Mana software toolkit](https://github.com/scchess/Mana).

It was developed as part of the **BINF6310 Final Project at Northeastern University**.

---

## 📂 Repository Structure
- `data/` → raw and processed datasets  
- `scripts/` → analysis scripts (e.g., `analyze_mRNA.py`)  
- `notebooks/` → step-by-step Jupyter workflows  
- `results/` → figures and summary tables  
- `docs/` → supporting files (final presentation, reference paper)

---

## 🔬 Methods
- Long-read sequencing data processed with Oxford Nanopore workflows  
- Quality assessment using Mana  
- Custom Python scripts for:
  - mapping rate calculation  
  - read length distribution  
  - poly(A) tail analysis  
- Visualization in Python (`matplotlib`, `seaborn`) and IGV  

---

## 📊 Results (Summary)
- **Read Length Distribution**:  
  - Modified mRNA → long, consistent peak (~1200–1400 nt)  
  - Unmodified mRNA → fragmented, shorter peaks (0–400 nt)  

- **Poly(A) Tail Length**: ~125 nt, highly reproducible across replicates  

- **Mapping Rate**:  
  - Modified mRNA → ~99.6%  
  - Unmodified mRNA → ~81.3%  

See `results/figures/` for plots and visualizations.  

---

## 📖 References
1. Gunter H.M. et al. *mRNA vaccine quality analysis using RNA sequencing*. **Nature Communications** (2023). [Link](https://doi.org/10.1038/s41467-023-41354-y)  
2. [Mana software GitHub repository](https://github.com/scchess/Mana)

---

## 👩‍💻 Contributors
- Pratham Donda (@PrathamD-11)  
- Group 5 members, BINF6310 (Northeastern University)
