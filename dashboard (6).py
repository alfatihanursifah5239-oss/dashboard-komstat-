import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard Analisis Data Anak")
st.write("Dibuat oleh: Alfatiha Nursifah Irawan 💛")

# Load dataset
data = pd.read_excel("data_bersih.xlsx")

# 1. Distribusi Provinsi
st.subheader("Distribusi Provinsi")
prov = data["Provinsi(B1R1)"].value_counts().reset_index()
prov.columns = ["Provinsi", "Jumlah"]
fig_prov = px.bar(prov, x="Provinsi", y="Jumlah", title="Distribusi Anak per Provinsi")
st.plotly_chart(fig_prov)

# 2. Kategori Umur
st.subheader("Kategori Umur (Bayi - Batita - Balita)")
data["Kategori_Umur"] = pd.cut(
    data["Umur(Bulan)(B4K7BLN)"],
    bins=[-1, 12, 36, 59],
    labels=["Bayi", "Batita", "Balita"]
)
umur = data["Kategori_Umur"].value_counts().reset_index()
fig_umur = px.pie(umur, names="index", values="Kategori_Umur",
                  title="Persentase Kategori Umur")
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
