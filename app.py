
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

# --- FRAME A: HERO SECTION (RATA KIRI AGAR STREAMLIT TIDAK BINGUNG) ---

hero_html = """<div style="background-color: #2d5a27; padding: 25px; border-radius: 12px; color: white; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px; margin-bottom: 25px; font-family: sans-serif;">
<div style="flex: 1; min-width: 120px; font-size: 1.5rem; font-weight: bold; display: flex; align-items: center; gap: 8px;">🌿 TaniPintar</div>
<div style="flex: 2; min-width: 260px; text-align: center;">
<h1 style="color: white; margin: 0; font-size: 1.8rem; font-weight: 800; line-height: 1.3; border: none; background: none; padding: 0;">Ubah Kebun Anda<br>Menjadi Cerdas</h1>
</div>
<div style="flex: 1; min-width: 160px; text-align: right;">
<a href="https://wa.me/628xxxxxxxxxx" target="_blank" style="background-color: white; color: #2d5a27; padding: 10px 18px; border-radius: 8px; text-decoration: none; font-weight: bold; display: inline-block; font-size: 0.9rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">Konsultasi Gratis (WA)</a>
</div>
</div>"""
st.markdown(hero_html, unsafe_allow_html=True)

# --- FRAME B: SOLUSI PERTANIAN (Murni Flexbox HTML Rata Kiri) ---

# Teks Subjudul Utama
st.markdown("### **Satu sistem pintar untuk semua jenis pertanian.**")

frame_b_html = """<div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 20px; margin-top: 20px; margin-bottom: 35px; font-family: sans-serif;">
<div style="flex: 1; min-width: 280px; background-color: #f0f7f4; padding: 25px; border-radius: 12px; border-left: 5px solid #2d5a27; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
<div style="font-size: 2rem; margin-bottom: 10px;">🏢</div>
<h3 style="color: #2d5a27; margin: 0 0 15px 0; font-size: 1.3rem; font-weight: bold;">Pertanian Indoor & Hidroponik</h3>
<ul style="margin: 0; padding-left: 20px; color: #333; line-height: 1.6; font-size: 0.95rem;">
<li style="margin-bottom: 8px;"><b>Otomatisasi Nutrisi & pH:</b> Sensor pintar menjaga takaran pupuk selalu pas secara otomatis.</li>
<li style="margin-bottom: 8px;"><b>Kontrol Iklim Mikro:</b> Atur lampu grow led, suhu, dan kelembapan ruangan langsung via HP.</li>
<li><b>Notifikasi Air Kering:</b> Alarm instan di WhatsApp jika air tandon nutrisi mulai menipis.</li>
</ul>
</div>
<div style="flex: 1; min-width: 280px; background-color: #edf4f9; padding: 25px; border-radius: 12px; border-left: 5px solid #2e6f9e; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
<div style="font-size: 2rem; margin-bottom: 10px;">🚜</div>
<h3 style="color: #2e6f9e; margin: 0 0 15px 0; font-size: 1.3rem; font-weight: bold;">Lahan Terbuka (Outdoor)</h3>
<ul style="margin: 0; padding-left: 20px; color: #333; line-height: 1.6; font-size: 0.95rem;">
<li style="margin-bottom: 8px;"><b>Smart Drip Irrigation:</b> Penyiraman otomatis hanya aktif saat tanah mendeteksi kekeringan.</li>
<li style="margin-bottom: 8px;"><b>Prediksi Cuaca Lokal:</b> Sistem otomatis menunda penyiraman jika mendeteksi hari akan hujan.</li>
<li><b>Deteksi Kesehatan Tanah:</b> Pantau kadar NPK tanah secara real-time dari layar dasbor.</li>
</ul>
</div>
</div>"""
st.markdown(frame_b_html, unsafe_allow_html=True)

# 1. Sentuhan CSS Kustom untuk mempercantik Tabel dan Tab Streamlit
st.markdown("""<style>
/* Membuat tampilan tabel Streamlit menjadi lebih bersih dan modern */
table {
    width: 100% !important;
    border-collapse: collapse !important;
    font-family: sans-serif !important;
}
th {
    background-color: #2d5a27 !important;
    color: white !important;
    text-align: left !important;
    padding: 10px !important;
}
td {
    padding: 10px !important;
    border-bottom: 1px solid #ddd !important;
    font-size: 0.95rem !important;
}
/* Mewarnai teks tombol aktif */
div[data-testid="stMarkdownContainer"] p strong {
    color: #2d5a27;
}
</style>""", unsafe_allow_html=True)

# Judul Utama Frame C
st.markdown("## **Pilih Paket Sesuai Kebutuhan Anda**")
st.write("Mulai digitalisasi kebun Anda hari ini demi hasil panen yang berlipat ganda.")

# 2. Membuat Sistem Tab Bawaan Streamlit
tab1, tab2 = st.tabs(["🛒 Beli Langsung", "💬 Tanya Dulu"])

with tab1:
    st.markdown("### **Daftar Paket Tani Pintar**")
    
    # Membuat tabel harga menggunakan format Markdown standar
    tabel_harga = """
| Nama Paket | Target Pengguna | Fitur Utama |
| :--- | :--- | :--- |
| **Starter 🌱** | Hobi / Rumahan | 2 Sensor Kelembapan + Kontrol Pompa Air Otomatis via HP |
| **Pro 📈** | Kebun Komersil | Paket Starter + Sensor pH, Nutrisi Otomatis + Grafik Analisis |
| **Enterprise 🚜** | Industri / Lahan Luas | Kustomisasi Penuh + Sensor NPK Tanah + Integrasi Cuaca + Garansi 2 Tahun |
"""
    st.markdown(tabel_harga)
    
    st.write("") # Jarak kosong
    # Tombol aksi untuk melihat demo alat
    st.link_button("📺 Lihat Demo Alat (YouTube)", "https://youtube.com", use_container_width=True)

with tab2:
    st.markdown("### **Formulir Konsultasi Gratis**")
    st.write("Silakan isi data di bawah ini, tim ahli kami akan segera menghubungi Anda.")
    
    # Membuat formulir input interaktif
    with st.form(key="form_konsultasi"):
        nama = st.text_input("Nama Lengkap")
        kontak = st.text_input("Nomor WhatsApp / Email")
        luas_lahan = st.selectbox("Luas Lahan Pertanian", ["< 100 m² (Rumahan)", "100 - 1000 m²", "> 1000 m² (Skala Industri)"])
        pesan = st.text_area("Ceritakan kendala atau kebutuhan kebun Anda")
        
        submit_button = st.form_submit_button(label="Kirim Pengajuan Konsultasi")
        
        if submit_button:
            if nama and kontak:
                st.success(f"Terima kasih {nama}! Data Anda berhasil dikirim. Tim Tani Pintar akan segera menghubungi Anda melalui {kontak}.")
            else:
                st.warning("Mohon isi Nama dan Kontak Anda terlebih dahulu.")

# --- FRAME D: Social Proof ---
st.markdown('<div class="frame frame-d">', unsafe_allow_html=True)
st.header("Social Proof & Penutup")
tabs = st.tabs(["Pendapat Pakar", "Slide Presentasi", "Hubungi Kami"])
with tabs[0]: st.write("Testimoni Ahli...")
with tabs[1]: st.write("Download Materi...")
with tabs[2]: st.write("Kontak Kami...")
st.markdown('</div>', unsafe_allow_html=True)
