# 🧠 NeurIPS 2025 Tutorial  
## From Tuning to Guarantees: Statistically Valid Hyperparameter Selection  

This repository contains all code and notebooks for the **NeurIPS 2025 tutorial** by  
**Amirmohammad Farzaneh** King’s College London.  

The tutorial introduces a rigorous and practical framework for **statistically valid hyperparameter selection**, covering:
- Learn-Then-Test (LTT)  
- Quantile LTT (QLTT)  
- Pareto Testing (PT)  
- Reliability-Graph-based PT (RG-PT)  
- Adaptive LTT (aLTT)  
- Autoevaluation via Prediction-Powered Inference (R-AutoEval)  

All notebooks are runnable on **Google Colab** with zero setup.  

---

## 🚀 Quick Start on Google Colab  

| Notebook | Launch in Colab |
|-----------|-----------------|
| 00_Quickstart.ipynb | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amirfar76/neurips25-valid-hparam-selection/blob/main/notebooks/00_Quickstart.ipynb) |
| A_LTT_average_risk.ipynb | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amirfar76/neurips25-valid-hparam-selection/blob/main/notebooks/A_LTT_average_risk.ipynb) |
| A_LTT_from_CSV.ipynb | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amirfar76/neurips25-valid-hparam-selection/blob/main/notebooks/A_LTT_from_CSV.ipynb) |
| B_QLTT_quantile_risk.ipynb | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amirfar76/neurips25-valid-hparam-selection/blob/main/notebooks/B_QLTT_quantile_risk.ipynb) |
| B_QLTT_from_CSV.ipynb | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amirfar76/neurips25-valid-hparam-selection/blob/main/notebooks/B_QLTT_from_CSV.ipynb) |
| C_PT_multi_objective.ipynb | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amirfar76/neurips25-valid-hparam-selection/blob/main/notebooks/C_PT_multi_objective.ipynb) |
| D_RGPT_graph_structured_FDR.ipynb | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amirfar76/neurips25-valid-hparam-selection/blob/main/notebooks/D_RGPT_graph_structured_FDR.ipynb) |
| E_aLTT_adaptive_e_values.ipynb | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amirfar76/neurips25-valid-hparam-selection/blob/main/notebooks/E_aLTT_adaptive_e_values.ipynb) |
| F_RAutoEval_PPI.ipynb | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amirfar76/neurips25-valid-hparam-selection/blob/main/notebooks/F_RAutoEval_PPI.ipynb) |

---

## 🧩 Repository Structure  

```
neurips25-valid-hparam-selection/
│
├── notebooks/                # Tutorial notebooks (A–F)
├── utils/                    # Utility functions (testing, synthetic data, CSV I/O)
├── data/                     # Example CSVs for binary & real-valued losses
├── figures/                  # (optional) Output figures
├── requirements.txt          # Dependencies for Binder / local use
├── LICENSE
└── README.md
```

---

## 📊 Input Format (CSV for all methods)

All methods accept data in a **uniform CSV format**.  

Each **row = one hyperparameter**  
Each **column = losses across calibration points**

Example:

| hyperparam_id | loss_1 | loss_2 | loss_3 | ... |
|---------------|--------|--------|--------|-----|
| λ₁ | 0 | 1 | 0 | ... |
| λ₂ | 1 | 0 | 1 | ... |
| λ₃ | 0 | 0 | 0 | ... |

- For binary losses, LTT uses an **exact Binomial** p-value.  
- For real-valued losses in [0, 1], it uses **Hoeffding’s bound**.  
- QLTT tests quantile risk based on exceedance counts.  

---

## 💻 Local Setup (optional)

```bash
git clone https://github.com/amirfar76/neurips25-valid-hparam-selection.git
cd neurips25-valid-hparam-selection
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

---

## 🧮 Colab Setup Snippet (if you clone manually in Colab)

```python
# Runtime setup
%pip -q install numpy scipy pandas scikit-learn statsmodels networkx matplotlib

# Optionally fetch sample CSVs from the repo
import os, urllib.request
base = "https://raw.githubusercontent.com/amirfar76/neurips25-valid-hparam-selection/main/data/"
for fname in ["sample_binary_losses.csv", "sample_real_losses.csv"]:
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(f"data/{fname}"):
        urllib.request.urlretrieve(base + fname, f"data/{fname}")
```

---

## 🧠 How to Use During the Tutorial

1. Click any **“Open in Colab”** badge above.  
2. Run the setup cell to install dependencies.  
3. Either:
   - Upload your own CSV file, or  
   - Use the provided examples in `/data/`.  
4. Set `csv_path` to your file.  
5. Run all cells — the notebook outputs statistically valid selections (FWER or FDR controlled).

---

## 📚 References  
- Angelopoulos & Bates, *Learn-Then-Test* (NeurIPS 2021)  
- Farzaneh et al., *Quantile Learn-Then-Test* (2024)  
- Laufer-Goldshtein, Fisch, Barzilay & Jaakkola, “Efficiently Controlling Multiple Risks with Pareto Testing,” ICLR 2023.  
- Farzaneh & Simeone, *Multi-Objective Hyperparameter Selection via Hypothesis Testing on Reliability Graphs* (NeurIPS 2025)  
- Zecchin et al., *Adaptive Learn-Then-Test* (2024)  
- Angelopoulos et al., *Prediction-Powered Inference* (2023)

---

## 🧾 License  
Released under the **MIT License**.  
You are free to use, modify, and cite with attribution.

---

**Maintainer:**  
[Amirmohammad Farzaneh](https://amirfar76.github.io)  
King’s College London
