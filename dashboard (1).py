import streamlit as st
import pandas as pd
import plotly.express as px

# Judul Dashboard
st.title("Dashboard Interaktif - Data Anak")
st.write("Dibuat oleh: Alfatiha Nursifah Irawan")

# Load Data
data = pd.read_csv("/content/data_bersih.csv")

# ------------------------------
# 1. DISTRIBUSI PROVINSI
# ------------------------------
st.subheader("Distribusi Provinsi")
prov = data["Provinsi(B1R1)"].value_counts().reset_index()
prov.columns = ["Provinsi", "Jumlah"]

fig_prov = px.bar(
    prov,
    x="Provinsi",
    y="Jumlah",
    color="Provinsi",
    title="Distribusi Anak berdasarkan Provinsi",
)
st.plotly_chart(fig_prov)

# ------------------------------
# 2. KATEGORI UMUR (Bayi/Batita/Balita)
# ------------------------------
st.subheader("Kategori Umur Anak")

data["Kategori_Umur"] = pd.cut(
    data["Umur(Bulan)(B4K7BLN)"],
    bins=[-1, 12, 36, 59],
    labels=["Bayi", "Batita", "Balita"]
)

umur_count = data["Kategori_Umur"].value_counts().reset_index()
umur_count.columns = ["Kategori", "Jumlah"]

fig_umur = px.pie(
    umur_count,
    names="Kategori",
    values="Jumlah",
    title="Persentase Kategori Usia Anak"
)
st.plotly_chart(fig_umur)

# ------------------------------
# 3. DISTRIBUSI JENIS KELAMIN
# ------------------------------
st.subheader("Distribusi Jenis Kelamin")

jk = data["JenisKelamin(B4K4)"].value_counts().reset_index()
jk.columns = ["Jenis Kelamin", "Jumlah"]

fig_jk = px.bar(
    jk,
    x="Jenis Kelamin",
    y="Jumlah",
    color="Jenis Kelamin",
    title="Distribusi Jenis Kelamin Anak"
)
st.plotly_chart(fig_jk)

# ------------------------------
# 4. HISTOGRAM BERAT BADAN
# ------------------------------
st.subheader("Histogram Berat Badan Anak")

fig_bb = px.histogram(
    data,
    x="BeratBadan(kg)(J01C)",
    nbins=30,
    title="Histogram Berat Badan"
)
st.plotly_chart(fig_bb)

# ------------------------------
# 5. HISTOGRAM TINGGI BADAN
# ------------------------------
st.subheader("Histogram Tinggi Badan Anak")

fig_tb = px.histogram(
    data,
    x="TinggiBadan(cm)(J02B)",
    nbins=30,
    title="Histogram Tinggi Badan"
)
st.plotly_chart(fig_tb)

# ------------------------------
# 6. TABEL RINGKASAN DATA
# ------------------------------
st.subheader("Ringkasan Data")
st.dataframe(data.head())
