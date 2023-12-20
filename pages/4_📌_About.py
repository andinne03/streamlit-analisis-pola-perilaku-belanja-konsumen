import streamlit as st

st.sidebar.success("Selamat datang di halaman about😆!")
# Data pertanyaan dan jawaban
data_qa = {
    "Apa tujuan dari app ini?": [
        "Identifikasi Pola Pembelian Bersama : Algoritma Apriori membantu mengidentifikasi kombinasi produk yang sering dibeli bersama-sama oleh pelanggan.",
        "Penentuan Penempatan Produk : Dengan mengetahui item yang sering dibeli bersama, bisnis dapat menentukan penempatan produk di dalam toko fisik atau tata letak di situs web e-commerce untuk meningkatkan visibilitas dan peluang penjualan.",
        "Penyesuaian Strategi Harga : Analisis pola pembelian konsumen dapat membantu dalam menetapkan strategi harga yang efektif. Jika dua atau lebih produk sering dibeli bersama-sama, pemberian diskon atau penawaran paket untuk kombinasi produk tersebut dapat mendorong penjualan.",
        "Peningkatan Cross-selling dan Up-selling : Dengan mengetahui pola pembelian pelanggan, bisnis dapat meningkatkan cross-selling (menawarkan produk tambahan yang relevan) dan up-selling (menawarkan produk yang lebih mahal atau versi yang ditingkatkan) untuk meningkatkan nilai transaksi.",   
        "Optimasi Stok dan Persediaan : Dengan memahami pola pembelian pelanggan, bisnis dapat mengelola stok dan persediaan dengan lebih efisien, menghindari kelebihan persediaan atau kekurangan stok yang dapat menghambat penjualan."
    ],
    "Apa itu Algoritma Apriori?": [
        "Algoritma Apriori adalah salah satu algoritma pada data mining untuk mencari frequent item/itemset pada transaksional database. Algoritma apriori banyak digunakan pada data transaksi atau biasa disebut market basket, misalnya sebuah swalayan memiliki market basket, dengan adanya algoritma apriori, pemilik swalayan dapat mengetahui pola pembelian seorang konsumen. ",
    ],
    "Apa saja komponen penting pada Algoritma Apriori?": [
        "Support : menunjukkan popularitas rata-rata produk atau item dalam database.",
        "Confidence : mengacu pada kemungkinan seorang pelanggan membeli dua atau lebih item secara bersamaan.",
        "Lift : menentukan sejauh mana hubungan antara dua itemset bersifat asosiatif (lebih sering muncul bersama) daripada bersifat independen. Jika lift > 1, itu menunjukkan adanya asosiasi yang positif."
    ],
    "Apakah user bisa bertanya menggunakan Bahasa Indonesia di Chatbot?": [
        "Tidak bisa, Chatbot hanya bisa menerima permintaan dari user yang menggunakan Bahasa Inggris.",
    ],
    "Apakah di Chatbot bisa menampilkan gambar?": [
        "Bisa, tetapi hanya untuk beberapa pertanyaan saja (pertanyaan sudah ditentukan dan tertera pada sidebar halaman 🤖Chatbot).",
    ]
}

# Sidebar dengan daftar pertanyaan
selected_question = st.sidebar.radio("Pilih Pertanyaan:", list(data_qa.keys()))

# Menampilkan pertanyaan dan jawaban
st.title("Frequently Asked Questions (FAQ)")
st.write(f"**Pertanyaan:** {selected_question}")

# Mengecek apakah pertanyaan sudah dipilih
if selected_question in data_qa:
    # Tombol untuk menampilkan jawaban
    if st.button("Tampilkan Jawaban"):
        st.write("**Jawaban:**")
        # Menampilkan jawaban dengan format Markdown
        for answer_point in data_qa[selected_question]:
            st.markdown(f"- {answer_point}")
