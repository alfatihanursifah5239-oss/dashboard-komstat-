import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard Analisis Data Anak")
st.write("Dibuat oleh: Alfatiha Nursifah Irawan")

# --- Load Data ---
data = pd.read_csv("data_bersih.csv", sep=";", decimal=",")

# --- Tampilkan Data ---
st.subheader("Data Bersih")
st.dataframe(data)

# 1. Distribusi Provinsi
st.subheader("Distribusi Provinsi")
prov = data["Provinsi(B1R1)"].value_counts().reset_index()
prov.columns = ["Provinsi", "Jumlah"]
fig_prov = px.bar(prov, x="Provinsi", y="Jumlah", title="Distribusi Anak per Provinsi")
st.plotly_chart(fig_prov)

# 2. KATEGORI UMUR
st.subheader("Persentase Kategori Umur")
umur = data["Kategori_Umur"].value_counts().reset_index()
umur.columns = ["Kategori", "Jumlah"]  # rename biar jelas
fig_umur = px.pie(
    umur,
    names="Kategori",
    values="Jumlah",
    title="Persentase Kategori Umur"
)
st.plotly_chart(fig_umur)

# 3. Jenis Kelamin
st.subheader("Distribusi Jenis Kelamin")
jk = data["JenisKelamin(B4K4)"].value_counts().reset_index()
fig_jk = px.bar(jk, x="index", y="JenisKelamin(B4K4)", 
                labels={"index": "Jenis Kelamin", "JenisKelamin(B4K4)": "Jumlah"},
                title="Distribusi Jenis Kelamin")
st.plotly_chart(fig_jk)

# 4. Histogram Berat Badan
st.subheader("Histogram Berat Badan")
fig_bb = px.histogram(data, x="BeratBadan(kg)(J01C)", nbins=30,
                      title="Distribusi Berat Badan Anak")
st.plotly_chart(fig_bb)

# 5. Histogram Tinggi Badan
st.subheader("Histogram Tinggi Badan")
fig_tb = px.histogram(data, x="TinggiBadan(cm)(J02B)", nbins=30,
                      title="Distribusi Tinggi Badan Anak")
st.plotly_chart(fig_tb)
