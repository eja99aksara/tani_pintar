import streamlit as st

# =================================================================
# CONFIGURASI HALAMAN & CSS GLOBAL
# =================================================================
st.set_page_config(page_title="Tani Pintar - Agrotech Digital", page_icon="🌿", layout="centered")

st.markdown("""<style>
/* Menghilangkan padding bawaan Streamlit */
.block-container { padding-top: 2rem !important; padding-bottom: 0rem !important; }
/* Style Kustom untuk Tabel di Frame C */
table { width: 100% !important; border-collapse: collapse !important; font-family: sans-serif !important; }
th { background-color: #2d5a27 !important; color: white !important; padding: 10px !important; text-align: left !important; }
td { padding: 10px !important; border-bottom: 1px solid #ddd !important; font-size: 0.95rem !important; }
</style>""", unsafe_allow_html=True)

# 🔗 CONFIGURASI LINK UTAMA (Silakan ganti dengan link asli Anda nanti)
nomor_admin_wa = "https://wa.me/628xxxxxxxxxx"
link_youtube_demo = "https://youtube.com" 
link_toko_online = "https://tokopedia.com" # Masukkan link Tokopedia/Shopee Anda di sini

# =================================================================
# --- FRAME A: HERO SECTION (Latar Lahan Pertanian Subur HD)     ---
# =================================================================
# Menggunakan gambar hamparan lahan pertanian subur beresolusi tinggi dengan overlay gelap 55%
hero_html = f"""<div style="background-image: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)), url('https://images.unsplash.com/photo-1500937386664-56d1dfef3854?q=80&w=1200&auto=format&fit=crop'); background-size: cover; background-position: center; padding: 30px 20px; border-radius: 12px; color: white; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px; margin-bottom: 30px; font-family: sans-serif;">
<div style="flex: 1; min-width: 120px; font-size: 1.5rem; font-weight: bold; display: flex; align-items: center; gap: 8px; text-shadow: 1px 1px 4px rgba(0,0,0,0.6);">🌿 TaniPintar</div>
<div style="flex: 2; min-width: 260px; text-align: center;">
<h1 style="color: white; margin: 0; font-size: 1.8rem; font-weight: 800; line-height: 1.3; border: none; background: none; padding: 0; text-shadow: 2px 2px 6px rgba(0,0,0,0.7);">Ubah Kebun Anda<br>Menjadi Cerdas</h1>
</div>
<div style="flex: 1; min-width: 140px; text-align: right;">
<!-- Ukuran kotak tombol WA diperkecil menggunakan padding mini dan font-size lebih padat -->
<a href="{nomor_admin_wa}" target="_blank" style="background-color: #2d5a27; color: white; padding: 6px 12px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.78rem; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.4);">Konsultasi Gratis (WA)</a>
</div>
</div>"""

st.markdown(hero_html, unsafe_allow_html=True)


# =================================================================
# --- FRAME B: SOLUSI PERTANIAN (Latar Komparasi Greenhouse/Lahan)---
# =================================================================
st.markdown("### **Satu sistem pintar untuk semua jenis pertanian.**")

# Menggunakan gambar lanskap perpaduan greenhouse modern dan lahan pertanian terbuka di latar belakang belakangnya dengan overlay putih 85%
frame_b_html = """<div style="background-image: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)), url('https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?q=80&w=1200&auto=format&fit=crop'); background-size: cover; background-position: center; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 20px; padding: 20px; border-radius: 12px; margin-top: 15px; margin-bottom: 40px; font-family: sans-serif;">
<div style="flex: 1; min-width: 280px; background-color: rgba(240, 247, 244, 0.9); padding: 25px; border-radius: 12px; border-left: 5px solid #2d5a27; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
<div style="font-size: 2rem; margin-bottom: 10px;">🏢</div>
<h3 style="color: #2d5a27; margin: 0 0 15px 0; font-size: 1.25rem; font-weight: bold;">Pertanian Indoor & Hidroponik</h3>
<ul style="margin: 0; padding-left: 20px; color: #333; line-height: 1.6; font-size: 0.95rem;">
<li style="margin-bottom: 8px;"><b>Otomatisasi Nutrisi & pH:</b> Sensor menjaga takaran pupuk selalu pas otomatis.</li>
<li style="margin-bottom: 8px;"><b>Kontrol Iklim Mikro:</b> Atur lampu grow led dan kelembapan via HP.</li>
<li><b>Notifikasi Air Kering:</b> Alarm instan WhatsApp jika air tandon menipis.</li>
</ul>
</div>
<div style="flex: 1; min-width: 280px; background-color: rgba(237, 244, 249, 0.9); padding: 25px; border-radius: 12px; border-left: 5px solid #2e6f9e; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
<div style="font-size: 2rem; margin-bottom: 10px;">🚜</div>
<h3 style="color: #2e6f9e; margin: 0 0 15px 0; font-size: 1.25rem; font-weight: bold;">Lahan Terbuka (Outdoor)</h3>
<ul style="margin: 0; padding-left: 20px; color: #333; line-height: 1.6; font-size: 0.95rem;">
<li style="margin-bottom: 8px;"><b>Smart Drip Irrigation:</b> Penyiraman otomatis aktif hanya saat tanah kering.</li>
<li style="margin-bottom: 8px;"><b>Prediksi Cuaca Lokal:</b> Sistem menunda siram otomatis jika akan hujan.</li>
<li><b>Deteksi Kesehatan Tanah:</b> Pantau kadar NPK tanah real-time dari dasbor.</li>
</ul>
</div>
</div>"""

st.markdown(frame_b_html, unsafe_allow_html=True)


# =================================================================
# --- FRAME C: PRODUK & HARGA (Perbaikan Indentasi Kolom Tombol) ---
# =================================================================

# Trik kontainer abu-abu untuk memisahkan section harga
st.markdown("""<div style="background-image: linear-gradient(rgba(248,249,250,0.8), rgba(248,249,250,0.8)), url('https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&auto=format&fit=crop'); background-size: cover; background-position: center; padding: 25px; border-radius: 12px; margin-bottom: 30px; font-family: sans-serif;">
<h2 style="margin-top: 0; color: #333; font-weight: bold; text-shadow: 1px 1px 2px rgba(255,255,255,0.8);">Pilih Paket Sesuai Kebutuhan Anda</h2>
<p style="color: #446; margin-bottom: 5px; font-weight: 500;">Mulai digitalisasi kebun Anda hari ini demi hasil panen yang berlipat ganda.</p>
</div>""", unsafe_allow_html=True)

# Inisialisasi Tab
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
    
    # Membagi tombol menjadi 2 kolom berdampingan dengan indentasi 4 spasi
    kolom_kiri, kolom_kanan = st.columns(2)
    
    with kolom_kiri:
        st.link_button("🛍️ Toko Online Official", link_toko_online, use_container_width=True)
        
    with kolom_kanan:
        st.link_button("📺 Lihat Demo Alat (YouTube)", link_youtube_demo, use_container_width=True)
        
    # Tombol utama kembali sejajar di bawah blok kolom
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
    st.markdown("<p style='text-align: center; color: #666;'>Atau ingin respon lebih cepat?</p>", unsafe_allow_html=True)
    st.link_button("💬 Chat Admin Langsung via WhatsApp", nomor_admin_wa, use_container_width=True)


# =================================================================
# --- FRAME D: SOCIAL PROOF & PENUTUP (Latar Mobile Dashboard)   ---
# =================================================================
st.write("")
st.markdown("## **Didukung oleh Para Pakar Pertanian**")

# Menggunakan gambar UI dashboard software teknologi modern dengan overlay putih tipis 88%
frame_d_html = """<div style="background-image: linear-gradient(rgba(255,255,255,0.88), rgba(255,255,255,0.88)), url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1200&auto=format&fit=crop'); background-size: cover; background-position: center; padding: 20px; border-radius: 12px; font-family: sans-serif; margin-top: 15px; margin-bottom: 30px;">
<div style="background-color: rgba(255,255,255,0.95); padding: 25px; border-radius: 12px; border-left: 5px solid #2d5a27; margin-bottom: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<p style="font-style: italic; color: #444; font-size: 1rem; line-height: 1.6; margin: 0 0 15px 0;">
"Implementasi teknologi IoT dan otomatisasi pada kebun terbukti meningkatkan efisiensi penggunaan pupuk hingga 30% dan mempercepat masa panen secara stabil. Tani Pintar memberikan solusi nyata yang mudah dipahami oleh petani kita."
</p>
<b style="color: #2d5a27; font-size: 0.95rem;">Dr. Ir. Hermawan, M.Sc.</b><br>
<span style="color: #777; font-size: 0.85rem;">Pakar Agronomi & Teknologi Pertanian</span>
</div>
</div>"""

st.markdown(frame_d_html, unsafe_allow_html=True)


# =================================================================
# --- FRAME E: PUSTAKA & BERITA TANI PINTAR (TERBARU!)           ---
# =================================================================
st.markdown("## **Pusat Informasi & Aktivitas Lapangan**")

tab_pustaka, tab_berita = st.tabs(["📚 Download Pustaka", "📰 Berita Tani Pintar"])

with tab_pustaka:
    st.markdown("### **E-Library & Modul Edukasi Gratis**")
    st.write("Silakan unduh dokumen panduan riset agronomi dan brosur alat untuk dipelajari secara offline.")
    
    # Grid sederhana untuk brosur pustaka
    st.markdown("""<div style="background-color: #f4f6f4; padding: 20px; border-radius: 12px; text-align: center; margin-bottom: 20px; font-family: sans-serif;">
<h4 style="margin: 0 0 10px 0; color: #2d5a27;">1. Panduan Budidaya Hidroponik Skala Industri</h4>
<p style="margin: 0 0 15px 0; color: #666; font-size: 0.9rem;">Buku saku manajemen pH air dan takaran PPM nutrisi AB Mix otomatis.</p>
<a href="https://google.com" target="_blank" style="background-color: #2d5a27; color: white; padding: 8px 18px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85rem; display: inline-block;">📥 Download E-Book (PDF)</a>
</div>
<div style="background-color: #f4f6f4; padding: 20px; border-radius: 12px; text-align: center; font-family: sans-serif;">
<h4 style="margin: 0 0 10px 0; color: #2d5a27;">2. Katalog Produk & Spesifikasi Hardware Hardware IoT</h4>
<p style="margin: 0 0 15px 0; color: #666; font-size: 0.9rem;">Brosur cetak mengenai data sheet sensor NPK, pompa dosing, dan ketahanan aki.</p>
<a href="https://google.com" target="_blank" style="background-color: #2d5a27; color: white; padding: 8px 18px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85rem; display: inline-block;">📥 Download Brosur Alat (PDF)</a>
</div>""", unsafe_allow_html=True)

with tab_berita:
    st.markdown("### **Dokumentasi Instalasi Lapangan**")
    st.write("Pantau aktivitas terbaru tim teknisi Tani Pintar saat merakit sistem cerdas langsung dari lahan para mitra kami.")
    
    # Berita Aktivitas Lapangan
    st.markdown("""<div style="font-family: sans-serif;">
<!-- Berita 1 -->
<div style="border-bottom: 1px solid #eee; padding: 15px 0; margin-bottom: 10px;">
<span style="color: #2d5a27; font-size: 0.8rem; font-weight: bold;">📅 JUNI 2026</span>
<h4 style="margin: 5px 0; color: #333;">Instalasi Paket Enterprise 5 Hektar Lahan Terbuka di Subang</h4>
<p style="margin: 5px 0; color: #666; font-size: 0.9rem; line-height: 1.5;">Tim teknisi sukses mengintegrasikan 12 titik sensor NPK tanah nirkabel dan stasiun cuaca mini (Weather Station) untuk otomatisasi pengairan tetes tanaman melon premium.</p>
</div>
<!-- Berita 2 -->
<div style="border-bottom: 1px solid #eee; padding: 15px 0; margin-bottom: 10px;">
<span style="color: #2d5a27; font-size: 0.8rem; font-weight: bold;">📅 MEI 2026</span>
<h4 style="margin: 5px 0; color: #333;">Modernisasi Greenhouse Hidroponik Selada di Lembang</h4>
<p style="margin: 5px 0; color: #666; font-size: 0.9rem; line-height: 1.5;">Pemasangan sistem takaran pompa nutrisi dosing otomatis berbasis pembacaan pH & EC secara real-time. Pemilik kini bisa memantau kondisi tandon penuh dari luar kota via aplikasi smartphone.</p>
</div>
</div>""", unsafe_allow_html=True)


# =================================================================
# --- FOOTER HALAMAN (Tetap Kokoh di Paling Bawah)               ---
# =================================================================
st.write("")
st.markdown("""<div style="background-color: #2d5a27; color: white; padding: 25px 20px; border-radius: 12px; text-align: center; font-size: 0.85rem; line-height: 1.8; font-family: sans-serif; margin-top: 30px;">
<b style="font-size: 1rem;">PT Agrotech Digital Indonesia</b><br>
📍 Jl. Kawasan Industri Pertanian Modern No. 45, Indonesia<br>
📞 WhatsApp: +62 8xx-xxxx-xxxx | ✉️ Email: info@tanipintar.com<br>
<hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.2); margin: 15px 0;">
© 2026 Tani Pintar. Hak Cipta Dilindungi Undang-Undang.
</div>""", unsafe_allow_html=True)
