# 🌍 Clustering Global Development Indicators

An interactive K-Means clustering app that groups 150+ countries by development level using World Development Indicators — deployed with Streamlit.

---

## 🔍 Project Overview

Performed EDA and preprocessing on a 2,704-row × 25-column World Development Indicators dataset covering GDP, life expectancy, infant mortality, internet usage, and health expenditure across 150+ countries. Applied K-Means clustering and PCA to identify meaningful development tiers.

---

## ⚙️ Features

- K-Means clustering with adjustable K (2–6) via sidebar slider
- PCA visualization reducing 15+ features to 2 components
- Captures 65–75% variance in 2 principal components
- Identifies 3 development tiers — Developed, Developing, Underdeveloped
- Country-wise cluster assignment table
- Cluster-wise summary statistics
- Interactive Streamlit dashboard

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Scikit-learn | K-Means, PCA, StandardScaler |
| Pandas / NumPy | Data processing |
| Matplotlib / Seaborn | Visualizations |
| Streamlit | App deployment |
| openpyxl | Excel file handling |

---

## 📂 Project Structure

```
├── app.py                                    # Streamlit application
├── EDA_task.ipynb                            # Exploratory data analysis
├── World_development_mesurement.xlsx         # Dataset
├── Cluster_Global_development_Group_4.pptx  # Project presentation
├── requirements.txt                          # Dependencies
└── README.md
```

---

## 🚀 Run Locally

```bash
git clone https://github.com/Shivaniac007/global-development-clustering
cd global-development-clustering
pip install -r requirements.txt
streamlit run app.py
```

---

## 📊 Results

- Optimal K of **3** selected using Elbow Method
- **3 meaningful clusters** identified — Developed, Developing, Underdeveloped
- PCA reduced 15+ features to 2 components capturing **65–75% variance**
- 150+ countries clustered across 25 development indicators

---

## 💡 What I Learned

- Unsupervised ML workflow end-to-end
- Choosing optimal K using the Elbow Method
- Dimensionality reduction trade-offs with PCA
- Making clustering results interpretable for non-technical audiences

---

## 👩‍💻 Author

**Shivani Channagoudra**
[LinkedIn](https://www.linkedin.com/in/shivani-channagoudra) | [GitHub](https://github.com/Shivaniac007)
