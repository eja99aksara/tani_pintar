import streamlit as st

# =================================================================
# CONFIGURASI HALAMAN & CSS GLOBAL (Termasuk Trik Transparansi Tab)
# =================================================================
st.set_page_config(page_title="Tani Pintar - Agrotech Digital", page_icon="🌿", layout="centered")

st.markdown("""<style>
/* Menghilangkan padding bawaan Streamlit */
.block-container { padding-top: 2rem !important; padding-bottom: 0rem !important; }

/* Style Kustom untuk Tabel di Frame C agar transparan */
table { width: 100% !important; border-collapse: collapse !important; font-family: sans-serif !important; }
th { background-color: rgba(45, 90, 39, 0.85) !important; color: white !important; padding: 10px !important; text-align: left !important; }
td { padding: 10px !important; border-bottom: 1px solid rgba(0,0,0,0.1) !important; font-size: 0.95rem !important; background-color: rgba(255,255,255,0.6) !important; }

/* Trik Transparansi Tab Streamlit (Frame C & E) */
div[data-testid="stTabs"] {
    background-color: rgba(255, 255, 255, 0.5) !important; 
    padding: 15px; 
    border-radius: 12px;
    backdrop-filter: blur(8px);
}
div[role="tabpanel"] {
    background-color: transparent !important;
}
</style>""", unsafe_allow_html=True)

# 🔗 CONFIGURASI LINK UTAMA
nomor_admin_wa = "https://wa.me/628xxxxxxxxxx"
link_youtube_demo = "https://youtube.com" 
link_toko_online = "https://tokopedia.com" 

# =================================================================
# --- FRAME A: HERO SECTION (Menggunakan Gambar Sawah Data)      ---
# =================================================================
# Menggunakan file: 1781366738720.png sebagai background utama pembuka
hero_html = f"""<div style="background-image: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)), url('https://raw.githubusercontent.com/agrotechdigital/app/main/1781366738720.png'); background-size: cover; background-position: center; background-repeat: no-repeat; min-height: 220px; padding: 40px 20px; border-radius: 12px; color: white; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px; margin-bottom: 30px; font-family: sans-serif;">
<div style="flex: 1; min-width: 120px; font-size: 1.6rem; font-weight: bold; display: flex; align-items: center; gap: 8px; text-shadow: 1px 1px 4px rgba(0,0,0,0.6);">🌿 TaniPintar</div>
<div style="flex: 2; min-width: 260px; text-align: center;">
<h1 style="color: white; margin: 0; font-size: 2rem; font-weight: 800; line-height: 1.3; border: none; background: none; padding: 0; text-shadow: 2px 2px 6px rgba(0,0,0,0.7);">Ubah Kebun Anda<br>Menjadi Cerdas</h1>
</div>
<div style="flex: 1; min-width: 140px; text-align: right;">
<a href="{nomor_admin_wa}" target="_blank" style="background-color: #2d5a27; color: white; padding: 10px 16px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85rem; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.4);">Konsultasi Gratis (WA)</a>
</div>
</div>"""

st.markdown(hero_html, unsafe_allow_html=True)


# =================================================================
# --- FRAME B: SOLUSI PERTANIAN (Menggunakan Infografis Solusi)   ---
# =================================================================
st.markdown("### **Satu sistem pintar untuk semua jenis pertanian.**")

# Menggunakan 1781366663615.png & 1781366599354.png sebagai banner infografis di dalam kartu
frame_b_html = """<div style="background-color: #f7f9f6; padding: 15px; border-radius: 12px; margin-bottom: 40px; font-family: sans-serif;">
    <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
        <div style="flex: 1; min-width: 280px; background-color: rgba(255, 255, 255, 0.95); padding: 20px; border-radius: 12px; border-top: 5px solid #2d5a27; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <img src="https://raw.githubusercontent.com/agrotechdigital/app/main/1781366663615.png" style="width: 100%; border-radius: 8px; margin-bottom: 15px;" alt="Infografis Indoor">
            <h3 style="color: #2d5a27; margin: 0 0 10px 0; font-size: 1.25rem; font-weight: bold;">Pertanian Indoor & Hidroponik</h3>
            <ul style="margin: 0; padding-left: 20px; color: #333; line-height: 1.6; font-size: 0.95rem;">
                <li style="margin-bottom: 6px;"><b>Otomatisasi Nutrisi & pH:</b> Menjaga takaran pupuk selalu pas.</li>
                <li style="margin-bottom: 6px;"><b>Kontrol Iklim Mikro:</b> Atur lampu grow led via smartphone.</li>
                <li><b>Notifikasi Air Kering:</b> Alarm instan WhatsApp jika tandon menipis.</li>
            </ul>
        </div>
        <div style="flex: 1; min-width: 280px; background-color: rgba(255, 255, 255, 0.95); padding: 20px; border-radius: 12px; border-top: 5px solid #2e6f9e; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <img src="https://raw.githubusercontent.com/agrotechdigital/app/main/1781366599354.png" style="width: 100%; border-radius: 8px; margin-bottom: 15px;" alt="Infografis Outdoor">
            <h3 style="color: #2e6f9e; margin: 0 0 10px 0; font-size: 1.25rem; font-weight: bold;">Lahan Terbuka (Outdoor)</h3>
            <ul style="margin: 0; padding-left: 20px; color: #333; line-height: 1.6; font-size: 0.95rem;">
                <li style="margin-bottom: 6px;"><b>Smart Drip Irrigation:</b> Penyiraman otomatis saat tanah kering.</li>
                <li style="margin-bottom: 6px;"><b>Prediksi Cuaca Lokal:</b> Sistem menunda siram jika akan hujan.</li>
                <li><b>Deteksi Kesehatan Tanah:</b> Pantau kadar NPK tanah real-time.</li>
            </ul>
        </div>
    </div>
</div>"""

st.markdown(frame_b_html, unsafe_allow_html=True)


# =================================================================
# --- FRAME C: PRODUK & HARGA (Menggunakan Gambar IoT Hardware)   ---
# =================================================================
# Menggunakan smart-farming-soil-sensor-... sebagai background agar nuansa hardware IoT sangat terasa
st.markdown("""<div style="background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('https://raw.githubusercontent.com/agrotechdigital/app/main/smart-farming-soil-sensor-digital-monitoring-greenhouse-modern-scene-featuring-iot-emitting-data-visualizations-to-445872804.jpg'); background-size: cover; background-position: center; background-repeat: no-repeat; padding: 40px 25px; border-radius: 12px; margin-bottom: 15px; font-family: sans-serif;">
<h2 style="margin-top: 0; color: white; font-weight: bold; text-shadow: 2px 2px 5px rgba(0,0,0,0.8);">Pilih Paket Sesuai Kebutuhan Anda</h2>
<p style="color: #fff; margin-bottom: 0; font-weight: 500; text-shadow: 1px 1px 4px rgba(0,0,0,0.7);">Mulai digitalisasi kebun Anda hari ini demi hasil panen yang berlipat ganda.</p>
</div>""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🛒 Beli Langsung", "💬 Tanya Dulu"])

with tab1:
    st.markdown("### **Daftar Paket Tani Pintar**")
    tabel_harga = """
| Nama Paket | Target Pengguna | Fitur Utama |
| :--- | :--- | :--- |
| **Starter 🌱** | Hobi / Rumahan | 2 Sensor Kelembapan + Kontrol Pompa Air Otomatis via HP |
| **Pro 📈** | Kebun Komersil | Paket Starter + Sensor pH, Nutrisi Otomatis + Grafik Analisis |
| **Enterprise 🚜** | Industri / Lahan Luas | Kustomisasi Penuh + Sensor NPK Tanah + Integrasi Cuaca + Garansi 2 Tahun |
"""
    st.markdown(tabel_harga)
    st.write("") 
    
    kolom_kiri, kolom_kanan = st.columns(2)
    with kolom_kiri:
        st.link_button("🛍️ Toko Online Official", link_toko_online, use_container_width=True)
    with kolom_kanan:
        st.link_button("📺 Lihat Demo Alat (YouTube)", link_youtube_demo, use_container_width=True)
        
    st.link_button("🟢 Hubungi Admin untuk Pemesanan Paket (WA)", nomor_admin_wa, use_container_width=True)

with tab2:
    st.markdown("### **Formulir Konsultasi Gratis**")
    st.write("Silakan isi data di bawah ini, tim ahli kami akan segera menghubungi Anda.")
    
    with st.form(key="form_konsultasi"):
        nama = st.text_input("Nama Lengkap")
        kontak = st.text_input("Nomor WhatsApp / Email")
        luas_lahan = st.selectbox("Luas Lahan Pertanian", ["< 100 m² (Rumahan)", "100 - 1000 m²", "> 1000 m² (Skala Industri)"])
        pesan = st.text_area("Ceritakan kendala atau kebutuhan kebun Anda")
        submit_button = st.form_submit_button(label="Kirim Pengajuan Konsultasi")
        if submit_button:
            if nama and kontak:
                st.success(f"Terima kasih {nama}! Data berhasil dikirim. Tim kami akan menghubungi Anda di {kontak}.")
            else:
                st.warning("Mohon isi Nama dan Kontak Anda terlebih dahulu.")
    st.write("")
    st.markdown("<p style='text-align: center; color: #111; font-weight: bold;'>Atau ingin respon lebih cepat?</p>", unsafe_allow_html=True)
    st.link_button("💬 Chat Admin Langsung via WhatsApp", nomor_admin_wa, use_container_width=True)


# =================================================================
# --- FRAME D: SOCIAL PROOF & PENUTUP (Menggunakan Petani Drone)  ---
# =================================================================
st.write("")
st.markdown("## **Didukung oleh Para Pakar Pertanian**")

# Menggunakan farmer-using-vr-drones-... sebagai background yang mengelilingi quote pakar
frame_d_html = """<div style="background-image: linear-gradient(rgba(0,0,0,0.25), rgba(0,0,0,0.25)), url('https://raw.githubusercontent.com/agrotechdigital/app/main/farmer-using-vr-drones-smart-farming.jpg'); background-size: cover; background-position: center; background-repeat: no-repeat; padding: 40px 15px; border-radius: 12px; font-family: sans-serif; margin-top: 15px; margin-bottom: 30px;">
<div style="background-color: rgba(255,255,255,0.9); padding: 25px; border-radius: 12px; border-left: 5px solid #2d5a27; box-shadow: 0 4px 15px rgba(0,0,0,0.15); backdrop-filter: blur(4px);">
<p style="font-style: italic; color: #111; font-size: 1rem; line-height: 1.6; margin: 0 0 15px 0;">
"Implementasi teknologi IoT dan otomatisasi pada kebun terbukti meningkatkan efisiensi penggunaan pupuk hingga 30% dan mempercepat masa panen secara stabil. Tani Pintar memberikan solusi nyata yang mudah dipahami oleh petani kita."
</p>
<b style="color: #2d5a27; font-size: 0.95rem;">Dr. Ir. Hermawan, M.Sc.</b><br>
<span style="color: #444; font-size: 0.85rem;">Pakar Agronomi & Teknologi Pertanian</span>
</div>
</div>"""

st.markdown(frame_d_html, unsafe_allow_html=True)


# =================================================================
# --- FRAME E: PUSTAKA & BERITA TANI PINTAR (Menggunakan Vertical Plant) ---
# =================================================================
st.write("")
st.markdown("## **Pusat Informasi & Aktivitas Lapangan**")

# Menyisipkan gambar 1781370872828.png tepat sebelum tab informasi sebagai pembuka visual
st.markdown("""<img src="https://raw.githubusercontent.com/agrotechdigital/app/main/1781370872828.png" style="width: 100%; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);" alt="Dokumentasi Lab">""", unsafe_allow_html=True)

tab_pustaka, tab_berita = st.tabs(["📚 Download Pustaka", "📰 Berita Tani Pintar"])

with tab_pustaka:
    st.markdown("### **E-Library & Modul Edukasi Gratis**")
    st.write("Silakan unduh dokumen panduan riset agronomi dan brosur alat untuk dipelajari secara offline.")
    
    st.markdown("""<div style="background-color: rgba(255,255,255,0.6); padding: 20px; border-radius: 12px; text-align: center; margin-bottom: 20px; font-family: sans-serif; border: 1px solid rgba(0,0,0,0.05);">
<h4 style="margin: 0 0 10px 0; color: #2d5a27;">1. Panduan Budidaya Hidroponik Skala Industri</h4>
<p style="margin: 0 0 15px 0; color: #232323; font-size: 0.9rem;">Buku saku manajemen pH air dan takaran PPM nutrisi AB Mix otomatis.</p>
<a href="https://google.com" target="_blank" style="background-color: #2d5a27; color: white; padding: 8px 18px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85rem; display: inline-block;">📥 Download E-Book (PDF)</a>
</div>
<div style="background-color: rgba(255,255,255,0.6); padding: 20px; border-radius: 12px; text-align: center; font-family: sans-serif; border: 1px solid rgba(0,0,0,0.05);">
<h4 style="margin: 0 0 10px 0; color: #2d5a27;">2. Katalog Produk & Spesifikasi Hardware Hardware IoT</h4>
<p style="margin: 0 0 15px 0; color: #232323; font-size: 0.9rem;">Brosur cetak mengenai data sheet sensor NPK, pompa dosing, dan ketahanan aki.</p>
<a href="https://google.com" target="_blank" style="background-color: #2d5a27; color: white; padding: 8px 18px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85rem; display: inline-block;">📥 Download Brosur Alat (PDF)</a>
</div>""", unsafe_allow_html=True)

with tab_berita:
    st.markdown("### **Dokumentasi Instalasi Lapangan**")
    st.write("Pantau aktivitas terbaru tim teknisi Tani Pintar saat merakit sistem cerdas langsung dari lahan para mitra kami.")
    
    st.markdown("""<div style="font-family: sans-serif;">
<div style="border-bottom: 1px solid rgba(0,0,0,0.1); padding: 15px 0; margin-bottom: 10px;">
<span style="color: #2d5a27; font-size: 0.8rem; font-weight: bold;">📅 JUNI 2026</span>
<h4 style="margin: 5px 0; color: #111;">Instalasi Paket Enterprise 5 Hektar Lahan Terbuka di Subang</h4>
<p style="margin: 5px 0; color: #333; font-size: 0.9rem; line-height: 1.5;">Tim teknisi sukses mengintegrasikan 12 titik sensor NPK tanah nirkabel dan stasiun cuaca mini untuk otomatisasi pengairan tetes tanaman melon premium.</p>
</div>
<div style="border-bottom: 1px solid rgba(0,0,0,0.1); padding: 15px 0; margin-bottom: 10px;">
<span style="color: #2d5a27; font-size: 0.8rem; font-weight: bold;">📅 MEI 2026</span>
<h4 style="margin: 5px 0; color: #111;">Modernisasi Greenhouse Hidroponik Selada di Lembang</h4>
<p style="margin: 5px 0; color: #333; font-size: 0.9rem; line-height: 1.5;">Pemasangan sistem takaran pompa nutrisi dosing otomatis berbasis pembacaan pH & EC secara real-time. Pemantauan via aplikasi smartphone.</p>
</div>
</div>""", unsafe_allow_html=True)


# =================================================================
# --- FOOTER HALAMAN                                             ---
# =================================================================
st.write("")
st.markdown("""<div style="background-color: #2d5a27; color: white; padding: 25px 20px; border-radius: 12px; text-align: center; font-size: 0.85rem; line-height: 1.8; font-family: sans-serif; margin-top: 30px;">
<b style="font-size: 1rem;">PT Agrotech Digital Indonesia</b><br>
📍 Jl. Kawasan Industri Pertanian Modern No. 45, Indonesia<br>
📞 WhatsApp: +62 8xx-xxxx-xxxx | ✉️ Email: info@tanipintar.com<br>
<hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.2); margin: 15px 0;">
© 2026 Tani Pintar. Hak Cipta Dilindungi Undang-Undang.
</div>""", unsafe_allow_html=True)
