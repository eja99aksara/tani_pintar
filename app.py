import streamlit as st

# CSS kustom untuk menghias kontainer
st.markdown("""
    <style>
    .hero-container {
        background-color: #2d5a27;
        padding: 40px;
        border-radius: 10px;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- FRAME A: Hero Section ---
with st.container():
    # Menghubungkan kelas CSS ke dalam kontainer via HTML pembungkus
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col1:
        st.write("Logo")
    with col2:
        st.markdown("<h1 style='text-align: center; color: white;'>Ubah Kebun Anda Menjadi Cerdas. Lipat Gandakan Hasil Panen Tanpa Ribet.</h1>", unsafe_allow_html=True)
    with col3:
        st.button("Konsultasi Gratis (WA)")
        
    st.markdown('</div>', unsafe_allow_html=True)
    
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
