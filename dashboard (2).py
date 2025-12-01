import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard Interaktif Data Anak")
st.write("Dibuat oleh: Alfatiha Nursifah Irawan 💛")

data = pd.read_csv("data_bersih.csv")  
# Distribusi Provinsi
st.subheader("Distribusi Provinsi")
prov = data["Provinsi(B1R1)"].value_counts().reset_index()
prov.columns = ["Provinsi", "Jumlah"]
fig_prov = px.bar(prov, x="Provinsi", y="Jumlah", title="Distribusi Provinsi")
st.plotly_chart(fig_prov)

# Kategori Umur
st.subheader("Kategori Umur")
data["Kategori_Umur"] = pd.cut(
    data["Umur(Bulan)(B4K7BLN)"],
    bins=[-1,12,36,59],
    labels=["Bayi","Batita","Balita"]
)
umur_count = data["Kategori_Umur"].value_counts()
fig_umur = px.pie(names=umur_count.index, values=umur_count.values, title="Kategori Umur")
st.plotly_chart(fig_umur)

# Jenis Kelamin
st.subheader("Jenis Kelamin")
jk = data["JenisKelamin(B4K4)"].value_counts()
fig_jk = px.bar(x=jk.index, y=jk.values, title="Distribusi Jenis Kelamin")
st.plotly_chart(fig_jk)

# Histogram Berat Badan
st.subheader("Histogram Berat Badan")
fig_bb = px.histogram(data, x="BeratBadan(kg)(J01C)", title="Histogram Berat Badan")
st.plotly_chart(fig_bb)

# Histogram Tinggi Badan
st.subheader("Histogram Tinggi Badan")
fig_tb = px.histogram(data, x="TinggiBadan(cm)(J02B)", title="Histogram Tinggi Badan")
st.plotly_chart(fig_tb)
