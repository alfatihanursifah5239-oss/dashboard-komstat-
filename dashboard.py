import pandas as pd
import plotly.express as px
import streamlit as st

# ========================
# LOAD DATA
# ========================
data = pd.read_csv("/content/data_bersih.csv")   
st.title("Dashboard Interaktif Eksplorasi Data Anak")
st.markdown("### Oleh: Alfatiha Nursifah Irawan")

# ========================
# FILTER (Opsional)
# ========================
provinsi_filter = st.selectbox("Pilih Provinsi:", ["Semua"] + sorted(data["Provinsi(B1R1)"].unique().tolist()))

if provinsi_filter != "Semua":
    data = data[data["Provinsi(B1R1)"] == provinsi_filter]

# ========================
# 1. BAR CHART PROVINSI
# ========================
st.subheader("Distribusi Responden per Provinsi")
prov = data["Provinsi(B1R1)"].value_counts().reset_index()
prov.columns = ["Provinsi", "Jumlah"]
fig1 = px.bar(prov, x="Provinsi", y="Jumlah", title="Jumlah Responden per Provinsi")
st.plotly_chart(fig1)

# ========================
# 2. PIE CHART KATEGORI UMUR
# ========================
st.subheader("Distribusi Kategori Umur")

# Pastikan kategori umur sudah ada
data["Kategori_Umur"] = pd.cut(
    data["Umur(Bulan)(B4K7BLN)"],
    bins=[0, 12, 36, 60],
    labels=["Bayi", "Batita", "Balita"]
)

umur = data["Kategori_Umur"].value_counts().reset_index()
umur.columns = ["Kategori Umur", "Jumlah"]
fig2 = px.pie(umur, names="Kategori Umur", values="Jumlah", title="Kategori Umur Anak")
st.plotly_chart(fig2)

# ========================
# 3. BAR CHART BERAT LAHIR (BINNING)
# ========================
st.subheader("Klasifikasi Berat Lahir")

data["Kategori_Berat_Lahir"] = pd.cut(
    data["BeratBadansaatDilahirkan(I05A)"],
    bins=3,
    labels=["Rendah", "Sedang", "Tinggi"],
    include_lowest=True
)
bl = data["Kategori_Berat_Lahir"].value_counts().reset_index()
bl.columns = ["Kategori Berat Lahir", "Jumlah"]
fig3 = px.bar(bl, x="Kategori Berat Lahir", y="Jumlah", title="Kategori Berat Lahir")
st.plotly_chart(fig3)

# ========================
# 4. DONUT CHART JENIS KELAMIN
# ========================
st.subheader("Jenis Kelamin")

jk = data["JenisKelamin(B4K4)"].value_counts().reset_index()
jk.columns = ["Jenis Kelamin", "Jumlah"]
fig4 = px.pie(jk, names="Jenis Kelamin", values="Jumlah", hole=0.4, title="Distribusi Jenis Kelamin")
st.plotly_chart(fig4)

# ========================
# 5. HISTOGRAM TINGGI BADAN
# ========================
st.subheader("Distribusi Tinggi Badan Anak")
fig5 = px.histogram(data, x="TinggiBadan(cm)(J02B)", nbins=40, title="Histogram Tinggi Badan")
st.plotly_chart(fig5)

# ========================
# 6. HISTOGRAM BERAT BADAN
# ========================
st.subheader("Distribusi Berat Badan Anak")
fig6 = px.histogram(data, x="BeratBadan(kg)(J01C)", nbins=40, title="Histogram Berat Badan")
st.plotly_chart(fig6)

st.success("Dashboard berhasil ditampilkan ✨")
