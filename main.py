import streamlit as st

st.title('hitung luas persegi panjang')

panjang = st.number_input("masukkan panjang :",0)
lebar = st.number_input("masukkan lebar :",0)
hitung = st.button("hitung luas :")

if hitung :
    luas = panjang * lebar
    #st.write("maka luas persegi panjang adalah :", luas)
    st.success(f"luas persegi panjang adalah : {luas}")