import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


# ==============================
# 1. App Title
# ==============================
st.set_page_config(page_title="Global Development Clustering", layout="wide")

st.title("🌍 Global Development Clustering")
st.write(
    "This web application groups countries based on global development "
    "indicators using K-Means clustering."
)


# ==============================
# 2. Load Dataset
# ==============================
df = pd.read_excel("World_development_mesurement.xlsx")


# ==============================
# 3. Dataset Preview
# ==============================
st.subheader("📊 Dataset Preview")
st.dataframe(df.head())


# ==============================
# 4. Data Preprocessing
# ==============================
num_cols = df.select_dtypes(include=['int64', 'float64']).columns

X = df[num_cols].fillna(df[num_cols].mean())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# ==============================
# 5. Select Number of Clusters
# ==============================
st.sidebar.header("⚙️ Clustering Settings")
k = st.sidebar.slider("Number of Clusters (K)", 2, 6, 3)


# ==============================
# 6. Apply K-Means
# ==============================
kmeans = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)


# ==============================
# 7. PCA for Visualization
# ==============================
pca = PCA(n_components=2)
pca_data = pca.fit_transform(X_scaled)

pca_df = pd.DataFrame(pca_data, columns=['PC1', 'PC2'])
pca_df['Cluster'] = df['Cluster']


# ==============================
# 8. Cluster Visualization
# ==============================
st.subheader("📈 Cluster Visualization")

fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(
    x='PC1',
    y='PC2',
    hue='Cluster',
    data=pca_df,
    palette='Set2',
    ax=ax
)

ax.set_title("K-Means Clusters (PCA Projection)")
ax.set_xlabel("Principal Component 1")
ax.set_ylabel("Principal Component 2")

st.pyplot(fig)


# ==============================
# 9. Cluster Summary
# ==============================
st.subheader("📌 Cluster-wise Summary")
st.dataframe(df.groupby('Cluster')[num_cols].mean())


# ==============================
# 10. Country-wise Clusters
# ==============================
st.subheader("🌐 Country-wise Cluster Assignment")
st.dataframe(df[['Country', 'Cluster']])


st.success("Deployment completed successfully 🚀")
