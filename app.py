import streamlit as st

# =================================================================
# 1. ATUR CSS KUSTOM (Mewarnai kontainer berdasarkan KEY)
# =================================================================
st.markdown("""
    <style>
    /* Mencari container Streamlit yang memiliki key="hero" */
    [data-testid="stElementContainer"]:has(div[id="hero"]) {
        background-color: #2d5a27 !important;
        padding: 35px !important;
        border-radius: 12px !important;
        color: white !important;
        margin-bottom: 25px;
    }
    
    /* Memastikan teks judul h1 di dalam container hero berwarna putih */
    [data-testid="stElementContainer"]:has(div[id="hero"]) h1 {
        color: white !important;
        font-size: 2rem !important;
        font-weight: bold !important;
    }
    
    /* Membuat tombol di dalam hero mengikuti tema */
    [data-testid="stElementContainer"]:has(div[id="hero"]) button {
        background-color: #ffffff !important;
        color: #2d5a27 !important;
        border: none !important;
        font-weight: bold !important;
    }
    </style>
""", unsafe_allow_html=True)


# =================================================================
# 2. STRUKTUR FRAME A: HERO SECTION (Murni Streamlit)
# =================================================================
# Kita buat container murni Streamlit dan beri key="hero"
with st.container(key="hero"):
    # Trik jangkar kecil agar CSS di atas bisa mendeteksi kontainer ini
    st.markdown('<div id="hero"></div>', unsafe_allow_html=True)
    
    # Membuat 3 kolom di dalam kontainer
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col1:
        st.write("### **Logo**")
        
    with col2:
        # Menggunakan heading standar Streamlit agar lebih stabil
        st.markdown("<h1 style='text-align: center; margin: 0;'>Ubah Kebun Anda Menjadi Cerdas</h1>", unsafe_allow_html=True)
        
    with col3:
        # Tombol bawaan Streamlit
        st.button("Konsultasi Gratis (WA)", key="tombol_wa")
    
# --- FRAME B: Solusi Pertanian ---
st.markdown('<div class="frame frame-b">', unsafe_allow_html=True)
st.subheader("Satu sistem pintar untuk semua jenis pertanian.")
col_in, col_out = st.columns(2)
with col_in:
    st.info("### Pertanian Indoor & Hidroponik")
with col_out:
    st.success("### Lahan Terbuka (Outdoor)")
st.markdown('</div>', unsafe_allow_html=True)

# --- FRAME C: Produk & Harga ---
st.markdown('<div class="frame frame-c">', unsafe_allow_html=True)
st.header("Produk & Harga")
tab1, tab2 = st.tabs(["Beli Langsung", "Tanya Dulu"])
with tab1:
    st.write("Tabel Harga: [Starter] [Pro - Best Seller] [Enterprise]")
with tab2:
    st.write("Silahkan isi form untuk konsultasi")
st.button("Lihat Demo Alat")
st.markdown('</div>', unsafe_allow_html=True)

# --- FRAME D: Social Proof ---
st.markdown('<div class="frame frame-d">', unsafe_allow_html=True)
st.header("Social Proof & Penutup")
tabs = st.tabs(["Pendapat Pakar", "Slide Presentasi", "Hubungi Kami"])
with tabs[0]: st.write("Testimoni Ahli...")
with tabs[1]: st.write("Download Materi...")
with tabs[2]: st.write("Kontak Kami...")
st.markdown('</div>', unsafe_allow_html=True)
