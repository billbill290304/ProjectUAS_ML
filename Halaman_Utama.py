import streamlit as st

# Konfigurasi halaman utama
st.set_page_config(page_title="Project Billkaf", layout="wide")

# Judul Halaman
st.title("Selamat Datang di Aplikasi Prediksi Ikan")

# Deskripsi aplikasi
st.markdown("""
    Ini adalah aplikasi untuk memprediksi spesies ikan menggunakan **Model Machine Learning**.
    - **Silakan baca terlebih dahulu untuk keterangan dari sidebar di sebelah kiri bagian bawah.**
    - **Silakan pilih halaman yang ingin Anda kunjungi dari sidebar di sebelah kiri bagian atas.**
""")

# Sidebar Navigasi
st.sidebar.markdown("### Navigasi")
st.sidebar.markdown("- **Halaman Utama**: Berisi pengantar aplikasi.")
st.sidebar.markdown("- **Algoritma RF**: MemPrediksi Spesies Ikan dengan Random Forest.")
st.sidebar.markdown("- **Algoritma SVM**: Memprediksi Spesies Ikan dengan Support Vector Machine.")

# Footer
st.markdown("---")
st.markdown("Dirancang dan Dikembangkan oleh **Billkaf Syava Al Bana**")