import streamlit as st
import pandas as pd
import plotly.express as px

# Judul dashboard
st.title("Dashboard Interaktif Data Anak")

# Load data 
data = pd.read_csv("data_bersih.csv")

# ---- 1. Distribusi Provinsi ----
st.subheader("Distribusi Provinsi")
prov = data["Provinsi(B1R1)"].value_counts().reset_index()
prov.columns = ["Provinsi", "Jumlah"]
fig_prov = px.bar(
    prov,
    x="Provinsi",
    y="Jumlah",
    title="Distribusi Provinsi"
)
st.plotly_chart(fig_prov)

# ---- 2. Kategori Umur ----
st.subheader("Kategori Umur Anak")
data["Kategori_Umur"] = pd.cut(
    data["Umur(Bulan)(B4K7BLN)"],
    bins=[-1,12,36,59],
    labels=["Bayi","Batita","Balita"]
)
umur_count = data["Kategori_Umur"].value_counts()
fig_umur = px.pie(
    values=umur_count.values,
    names=umur_count.index,
    title="Kategori Umur Anak"
)
st.plotly_chart(fig_umur)

# ---- 3. Jenis Kelamin ----
st.subheader("Distribusi Jenis Kelamin")
jk = data["JenisKelamin(B4K4)"].value_counts()
fig_jk = px.bar(
    x=jk.index,
    y=jk.values,
    title="Distribusi Jenis Kelamin",
    labels={"x":"Jenis Kelamin", "y":"Jumlah"}
)
st.plotly_chart(fig_jk)

# ---- 4. Histogram Berat Badan ----
st.subheader("Histogram Berat Badan")
fig_bb = px.histogram(
    data,
    x="BeratBadan(kg)(J01C)",
    nbins=30,
    title="Histogram Berat Badan Anak"
)
st.plotly_chart(fig_bb)

# ---- 5. Histogram Tinggi Badan ----
st.subheader("Histogram Tinggi Badan")
fig_tb = px.histogram(
    data,
    x="TinggiBadan(cm)(J02B)",
    nbins=30,
    title="Histogram Tinggi Badan Anak"
)
st.plotly_chart(fig_tb)
