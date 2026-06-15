
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
