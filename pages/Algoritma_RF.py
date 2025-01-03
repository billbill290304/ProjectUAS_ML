import streamlit as st
import joblib

# Judul
st.set_page_config(page_title="RF Billkaf", layout="wide")
st.title("🎣 Prediksi Spesies Ikan dengan Random Forest")

# Sidebar untuk input
st.sidebar.header("🔢 Masukkan Parameter")
length = st.sidebar.number_input("📍 Panjang (cm):", min_value=0.0, format="%.2f")
weight = st.sidebar.number_input("⚖️ Berat (kg):", min_value=0.0, format="%.2f")
ratio  = st.sidebar.number_input("🖐 Rasio Berat-Panjang:", min_value=0.0, format="%.2f")

# Menampilkan informasi tentang aplikasi
st.markdown("""
    Aplikasi ini memprediksi spesies ikan berdasarkan parameter berikut:
    - **Panjang**: Panjang ikan dalam sentimeter.
    - **Berat**: Berat ikan dalam kilogram.
    - **Rasio Berat-Panjang**: Rasio antara berat dan panjang.

    **Klik tombol di bawah ini untuk mendapatkan prediksi!**
""")

# Tombol prediksi
if st.button("🔍 Prediksi Spesies"):
    # Memuat model, scaler, dan label encoder
    random_model = joblib.load('Supervised Random Forest/Random_Scaler_Model.pkl')
    scaler       = joblib.load('Supervised Random Forest/Random_Scaler.pkl')

    # Scaling data input
    scaled_input = scaler.transform([[length, weight, ratio]])

    # Melakukan prediksi
    prediction = random_model.predict(scaled_input)
    
    # Menampilkan hasil
    st.success(f'Spesies yang Diprediksi: **{prediction[0]}**')

    # Dictionary untuk mencocokkan spesies dengan nama file gambar
    species_to_image = {
        "Anabas testudineus"    : "img/1.jpg",
        "Coilia dussumieri"     : "img/2.jpg",
        "Otolithoides biauritus": "img/3.jpg",
        "Otolithoides pama"     : "img/4.jpg",
        "Pethia conchonius"     : "img/5.jpg",
        "Polynemus paradiseus"  : "img/6.jpg",
        "Puntius lateristriga"  : "img/7.jpg",
        "Setipinna taty"        : "img/8.jpg",
        "Sillaginopsis panijus" : "img/9.jpg"
    }

    # Menampilkan gambar jika ada spesies yang cocok
    species = prediction[0]
    if species in species_to_image:
        image_file = species_to_image[species]
        st.image(image_file, caption=f'Gambar Ikan dari Species {species}', use_column_width=True)

# Tambahkan footer
st.markdown("---")
st.markdown("Dirancang dan Dikembangkan oleh Billkaf Syava Al Bana")
