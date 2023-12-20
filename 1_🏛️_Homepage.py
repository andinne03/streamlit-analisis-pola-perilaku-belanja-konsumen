import streamlit as st 
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://images.unsplash.com/photo-1578916171728-46686eac8d58?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
}
[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

from PIL import Image
image = Image.open('C:\Streamlit\photo\judul.png')
st.image(image)

#st.markdown("<h1 style='text-align: center; color: black;'>Analisis Pola Perilaku Belanja Konsumen di Sebuah Supermarket dengan Menggunakan Algoritma Apriori</h1>", unsafe_allow_html=True)
st.sidebar.success("Selamat datang di halaman utama😆!")

