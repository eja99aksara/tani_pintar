import streamlit as st
import base64
import os

# =================================================================
# FUNGSI PEMBANTU UNTUK GAMBAR LOKAL (BASE64)
# =================================================================
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
    return ""

# Membaca seluruh 7 aset gambar Anda
bg_hero = get_base64_image("1781366738720.png")
img_indoor = get_base64_image("1781366663615.png")
img_outdoor = get_base64_image("1781366599354.png")
bg_paket = get_base64_image("smart-farming-soil-sensor-digital-monitoring-greenhouse-modern-scene-featuring-iot-emitting-data-visualizations-to-445872804.jpg")
bg_proof = get_base64_image("farmer-using-vr-drones-smart-farming.jpg")
img_banner_pustaka = get_base64_image("1781370872828.png")
img_robot = get_base64_image("smart-robotic-farmer-spraying-fertilizer-vegetable-green-plants.jpg")

# =================================================================
# CONFIGURASI CSS GLOBAL
# =================================================================
st.set_page_config(page_title="Tani Pintar - Agrotech Digital", page_icon="🌿", layout="centered")

st.markdown("""<style>
.block-container { padding-top: 2rem !important; padding-bottom: 0rem !important; }
table { width: 100% !important; border-collapse: collapse !important; font-family: sans-serif !important; }
th { background-color: rgba(45, 90, 39, 0.85) !important; color: white !important; padding: 10px !important; text-align: left !important; }
td { padding: 10px !important; border-bottom: 1px solid rgba(0,0,0,0.1) !important; font-size: 0.95rem !important; background-color: rgba(255,255,255,0.6) !important; }

div[data-testid="stTabs"] {
    background-color: rgba(255, 255, 255, 0.65) !important; 
    padding: 15px; 
    border-radius: 12px;
    backdrop-filter: blur(8px);
}
div[role="tabpanel"] { background-color: transparent !important; }
</style>""", unsafe_allow_html=True)

nomor_admin_wa = "https://wa.me/628xxxxxxxxxx"
link_youtube_demo = "https://youtube.com" 
link_toko_online = "https://tokopedia.com" 

# =================================================================
# --- FRAME A: HERO SECTION (Menghapus Kotak Buram, Efek Jernih Maksimal) ---
# =================================================================
hero_html = f"""<div style="background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('{bg_hero}'); background-size: cover; background-position: center; background-repeat: no-repeat; padding: 40px 20px; border-radius: 12px; color: white; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 12px; margin-bottom: 30px; font-family: sans-serif;">
    <div style="font-size: 1.1rem; font-weight: bold; letter-spacing: 1px; margin-bottom: 2px; color: #ffffff; text-shadow: 2px 2px 5px rgba(0,0,0,0.7);">🌿 TaniPintar</div>
    <h1 style="color: white; margin: 0 0 10px 0; font-size: 1.6rem; font-weight: 800; line-height: 1.2; text-shadow: 2px 2px 6px rgba(0,0,0,0.8); border: none; background: none; padding: 0;">Ubah Kebun Anda<br>Menjadi Cerdas</h1>
    <a href="{nomor_admin_wa}" target="_blank" style="background-color: #2d5a27; color: white; padding: 6px 16px; border-radius: 20px; text-decoration: none; font-weight: bold; font-size: 0.75rem; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.2);">Konsultasi Gratis (WA)</a>
</div>"""

st.markdown(hero_html, unsafe_allow_html=True)

# =================================================================
# --- FRAME B: SOLUSI PERTANIAN (Menggunakan Gambar 2 & 3)
# =================================================================
st.markdown("## **Satu sistem pintar untuk semua jenis pertanian.**")

frame_b_html = f"""<div style="background-color: #f7f9f6; padding: 15px; border-radius: 12px; margin-bottom: 40px; font-family: sans-serif;">
    <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
        <div style="flex: 1; min-width: 280px; background-color: rgba(255, 255, 255, 0.95); padding: 20px; border-radius: 12px; border-top: 5px solid #2d5a27; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <img src="{img_indoor}" style="width: 100%; border-radius: 8px; margin-bottom: 15px;" alt="Indoor">
            <h3 style="color: #2d5a27; margin: 0 0 10px 0; font-size: 1.25rem; font-weight: bold;">Pertanian Indoor & Hidroponik</h3>
            <ul style="margin: 0; padding-left: 20px; color: #333; line-height: 1.6; font-size: 0.95rem;">
                <li style="margin-bottom: 6px;"><b>Otomatisasi Nutrisi & pH:</b> Sensor menjaga takaran selalu pas.</li>
                <li style="margin-bottom: 6px;"><b>Kontrol Iklim Mikro:</b> Atur lampu grow led via HP.</li>
                <li><b>Notifikasi Air Kering:</b> Alarm instan WhatsApp jika tandon menipis.</li>
            </ul>
        </div>
        <div style="flex: 1; min-width: 280px; background-color: rgba(255, 255, 255, 0.95); padding: 20px; border-radius: 12px; border-top: 5px solid #2e6f9e; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <img src="{img_outdoor}" style="width: 100%; border-radius: 8px; margin-bottom: 15px;" alt="Outdoor">
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
# --- FRAME C: PRODUK & HARGA
# =================================================================
st.markdown(f"""<div style="background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('{bg_paket}'); background-size: cover; background-position: center; background-repeat: no-repeat; padding: 40px 25px; border-radius: 12px; margin-bottom: 15px; font-family: sans-serif;">
<h2 style="margin-top: 0; color: white; font-weight: bold; text-shadow: 2px 2px 5px rgba(0,0,0,0.8); border: none; background: none; padding: 0;">Pilih Paket Sesuai Kebutuhan Anda</h2>
<p style="color: #fff; margin-bottom: 0; font-weight: 500; text-shadow: 1px 1px 4px rgba(0,0,0,0.7);">Mulai digitalisasi kebun Anda hari ini demi hasil panen yang berlipat ganda.</p>
</div>""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🛒 Beli Langsung", "💬 Tanya Dulu"])
with tab1:
    st.markdown("### **Daftar Paket Tani Pintar**")
    st.markdown("""
| Nama Paket | Target Pengguna | Fitur Utama |
| :--- | :--- | :--- |
| **Starter 🌱** | Hobi / Rumahan | 2 Sensor Kelembapan + Kontrol Pompa Air via HP |
| **Pro 📈** | Kebun Komersil | Paket Starter + Sensor pH & Nutrisi Otomatis |
| **Enterprise 🚜** | Industri / Lahan Luas | Kustomisasi Penuh + Sensor NPK Tanah |
""")
    col1, col2 = st.columns(2)
    with col1: st.link_button("🛍️ Toko Online Official", link_toko_online, use_container_width=True)
    with col2: st.link_button("📺 Lihat Demo Alat (YouTube)", link_youtube_demo, use_container_width=True)
    st.link_button("🟢 Hubungi Admin untuk Pemesanan Paket (WA)", nomor_admin_wa, use_container_width=True)

with tab2:
    st.markdown("### **Formulir Konsultasi Gratis**")
    with st.form(key="form_konsultasi"):
        nama = st.text_input("Nama Lengkap")
        kontak = st.text_input("Nomor WhatsApp")
        luas_lahan = st.selectbox("Luas Lahan", ["< 100 m²", "100 - 1000 m²", "> 1000 m²"])
        pesan = st.text_area("Ceritakan kendala kebun Anda")
        if st.form_submit_button(label="Kirim Pengajuan"):
            st.success(f"Terima kasih {nama}! Data berhasil dikirim.")

# =================================================================
# --- FRAME D: SOCIAL PROOF (Mengikuti Gaya Jernih Tanpa Kotak Buram) ---
# =================================================================
st.write("")
st.markdown("## **Social Proof & Penutup**")

frame_d_html = f"""<div style="background-image: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)), url('{bg_proof}'); background-size: cover; background-position: center; background-repeat: no-repeat; padding: 40px 25px; border-radius: 12px; font-family: sans-serif; margin-bottom: 30px; text-align: center;">
    <p style="font-style: italic; color: #ffffff; font-size: 0.85rem; line-height: 1.6; margin: 0 0 15px 0; text-shadow: 2px 2px 5px rgba(0,0,0,0.8); font-weight: 500;">
    "Implementasi teknologi IoT dan otomatisasi pada kebun terbukti meningkatkan efisiensi penggunaan pupuk hingga 30% dan mempercepat masa panen secara stabil."
    </p>
    <b style="color: #ffffff; font-size: 0.85rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">Dr. Ir. Hermawan, M.Sc.</b><br>
    <span style="color: #e0e0e0; font-size: 0.75rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">Pakar Agronomi & Teknologi Pertanian</span>
</div>"""

st.markdown(frame_d_html, unsafe_allow_html=True)

# =================================================================
# --- FRAME E: PUSTAKA & DOKUMENTASI (Menggunakan Gambar 6 & 7)
# =================================================================
st.markdown("## **Pelajari Lebih Lanjut Sistem Tani Pintar**")

# Menggunakan gambar laboratorium vertikal sebagai banner atas pustaka
st.markdown(f"""<img src="{img_banner_pustaka}" style="width: 100%; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);" alt="Dokumentasi Lab">""", unsafe_allow_html=True)

tab_pustaka, tab_berita = st.tabs(["📚 Download Pustaka", "📰 Berita Tani Pintar"])
with tab_pustaka:
    st.markdown(f"""<div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 12px; text-align: center; font-family: sans-serif; border: 1px solid rgba(0,0,0,0.05);">
<h4 style="margin: 0 0 10px 0; color: #2d5a27;">Katalog Produk & Spesifikasi Hardware IoT</h4>
<p style="margin: 0 0 15px 0; color: #232323; font-size: 0.9rem;">Unduh brosur digital lengkap mengenai skema rangkaian alat kami.</p>
<a href="https://google.com" target="_blank" style="background-color: #2d5a27; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85rem; display: inline-block;">📥 Download Brosur Alat (PDF)</a>
</div>""", unsafe_allow_html=True)

with tab_berita:
    st.markdown("### **Riset & Pengembangan Masa Depan**")
    # Memasang gambar ke-7 (Robot Sprayer) di dalam tab berita aktivitas
    st.markdown(f"""<img src="{img_robot}" style="width: 100%; border-radius: 8px; margin-bottom: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" alt="Robot Sprayer">""", unsafe_allow_html=True)
    st.markdown("""<div style="font-family: sans-serif; background-color: rgba(255,255,255,0.5); padding: 15px; border-radius: 12px;">
<span style="color: #2d5a27; font-size: 0.8rem; font-weight: bold;">📅 BERITA BARU</span>
<h4 style="margin: 5px 0; color: #111;">Uji Coba Drone & Robot Penyemprot Pupuk Otomatis</h4>
<p style="margin: 5px 0; color: #333; font-size: 0.9rem;">Tim R&D Tani Pintar memulai tahap uji coba purwarupa robot navigasi pelacak hama tanaman untuk akurasi dosis pemupukan cair skala besar.</p>
</div>""", unsafe_allow_html=True)

# =================================================================
# --- FOOTER HALAMAN
# =================================================================
st.write("")
st.markdown("""<div style="background-color: #2d5a27; color: white; padding: 25px 20px; border-radius: 12px; text-align: center; font-size: 0.85rem; line-height: 1.8; font-family: sans-serif; margin-top: 30px;">
<b style="font-size: 1rem;">PT Agrotech Digital Indonesia</b><br>
📍 Jl. Kawasan Industri Pertanian Modern No. 45, Indonesia<br>
© 2026 Tani Pintar. Hak Cipta Dilindungi Undang-Undang.
</div>""", unsafe_allow_html=True)
