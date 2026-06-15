
import streamlit as st

# =================================================================
# 1. ATUR CSS KUSTOM (Untuk menghilangkan dekorasi bawaan jika ada)
# =================================================================
st.markdown("""
    <style>
    /* Menghilangkan padding bawaan blok markdown agar pas */
    .block-container {
        padding-top: 2rem !important;
    }
    </style>
""", unsafe_allow_html=True)


import streamlit as st

# --- FRAME A: HERO SECTION (Murni Flexbox HTML dieksekusi Python) ---

hero_html = """
<div style="
    background-color: #2d5a27; 
    padding: 30px 40px; 
    border-radius: 12px; 
    color: white; 
    display: flex; 
    justify-content: space-between; 
    align-items: center;
    flex-wrap: wrap;
    gap: 20px;
    margin-bottom: 30px;
    font-family: sans-serif;
">
    <div style="flex: 1; min-width: 100px; font-size: 1.5rem; font-weight: bold; display: flex; align-items: center; gap: 8px;">
        🌿 TaniPintar
    </div>
    
    <div style="flex: 3; min-width: 250px; text-align: center;">
        <h1 style="color: white; margin: 0; font-size: 2.2rem; font-weight: 800; line-height: 1.2; border: none;">
            Ubah Kebun Anda<br>Menjadi Cerdas
        </h1>
    </div>
    
    <div style="flex: 1; min-width: 180px; text-align: right;">
        <a href="https://wa.me/628xxxxxxxxxx" target="_blank" style="
            background-color: white; 
            color: #2d5a27; 
            padding: 12px 20px; 
            border-radius: 8px; 
            text-decoration: none; 
            font-weight: bold;
            display: inline-block;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        ">
            Konsultasi Gratis (WA)
        </a>
    </div>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)

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
