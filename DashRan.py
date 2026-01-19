import streamlit as st
from pathlib import Path
import base64

# ====================================
# KONFIGURASI DASAR
# ====================================
LOGO_PATH = "Logo_BMKG.png"
EBOOK_PATH = "Pedoman QC Ranika.pdf"

st.set_page_config(
    page_title="Dashboard Ebook BMKG",
    layout="wide",
)

st.markdown(
    """
    <style>
    .block-container { padding-top: 0.6rem !important; }
    header { margin-top: 0 !important; }
    .header-wrap { margin-top: 0 !important; padding-top: 0.4rem !important; }
    </style>
    """,
    unsafe_allow_html=True
)

if "show_pdf" not in st.session_state:
    st.session_state.show_pdf = False


# ====================================
# FUNGSI BANTU
# ====================================
def load_pdf_base64(pdf_path: str) -> str:
    pdf_file = Path(pdf_path)
    if not pdf_file.exists():
        return ""
    with open(pdf_file, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


# ====================================
# CSS
# ====================================
st.markdown(
    """
    <style>
    .bmkg-title-main {
        font-weight: 700;
        font-size: 2.05rem;
        letter-spacing: 0.03em;
        margin-bottom: 0.1rem;
    }
    .bmkg-title-sub { font-size: 1.9rem; }

    .home-btn button {
        background-color: #0F8549;
        color: white;
        border-radius: 999px;
        padding: 0.25rem 1.2rem;
        border: none;
        font-weight: 600;
    }

    .file-card {
        border-radius: 0.75rem;
        padding: 1rem;
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }

    .materi-card {
        background-color: #f5f7fb;
        border-radius: 20px;
        padding: 1.5rem 1.8rem;
        margin-top: 0.5rem;
    }
    .materi-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }
    .materi-title-main {
        font-weight: 700;
        font-size: 1.05rem;
        letter-spacing: 0.03em;
    }
    .materi-body {
        font-size: 0.95rem;
        line-height: 1.6;
        text-align: justify;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ====================================
# HEADER
# ====================================
home_clicked = False

with st.container():
    col_left, col_menu = st.columns([5, 1])

    with col_left:
        logo_col, text_col = st.columns([1, 10])
        with logo_col:
            if Path(LOGO_PATH).exists():
                st.image(LOGO_PATH, width=90)
        with text_col:
            st.markdown(
                """
                <div class="bmkg-title-main">
                    BADAN METEOROLOGI, KLIMATOLOGI, DAN GEOFISIKA
                </div>
                <div class="bmkg-title-sub">
                    DEPUTI BIDANG KLIMATOLOGI
                </div>
                """,
                unsafe_allow_html=True,
            )

    with col_menu:
        home_clicked = st.button("Beranda")

if home_clicked:
    st.session_state.show_pdf = False

st.markdown("---")


# ====================================
# JUDUL HALAMAN
# ====================================
st.markdown(
    """
    ### Dashboard Tim Kerja Informasi Pencemaran Udara
    #### Pedoman Quality Control Particulate Matter 2.5 (PM2.5)
    """
)


# ====================================
# KONTEN UTAMA
# ====================================
left, right = st.columns([2.5, 1.5])

# =======================
# MATERI POKOK
# =======================
ringkasan = """
Materi pokok dalam Pedoman Quality Control (QC) Alat dan Data PM2.5 memuat ketentuan
teknis dan operasional sebagai acuan standar pelaksanaan pengendalian mutu alat dan
data pemantauan partikulat halus (PM2.5) di lingkungan BMKG.
"""

materi_lengkap = """
Pedoman ini disusun untuk menjamin keandalan, konsistensi, dan kredibilitas data PM2.5 yang digunakan dalam penyusunan informasi kualitas udara nasional, melalui penguatan sistem pengendalian mutu yang terintegrasi dalam tata kelola data kualitas udara. Ruang lingkup pengendalian mutu meliputi dua komponen utama, yaitu Quality Control (QC) alat pemantau PM2.5 otomatis dan Quality Control (QC) data PM2.5 hasil pengamatan, yang dilaksanakan secara berjenjang, sistematis, dan terstandar. 

Pedoman ini mengatur struktur organisasi, peran, serta tanggung jawab unit kerja di lingkungan BMKG, khususnya Bidang Informasi Kualitas Udara dan UPT, dalam melaksanakan QC alat dan data secara rutin. Selain itu, diatur pula metodologi QC alat PM2.5, termasuk ketentuan pemeriksaan, pengoperasian, pemeliharaan, dan kalibrasi instrumen BAM 1020 melalui kegiatan QC harian, mingguan, bulanan, dan tahunan untuk menjamin kinerja alat sesuai standar. Dalam aspek QC data, pedoman ini menetapkan prosedur pengelolaan dan pengendalian mutu data melalui sistem flagging, identifikasi error instrumen, deteksi outlier, serta penentuan status data valid dan invalid.

Pedoman ini juga menetapkan kriteria statistik validitas data jam-an, harian, dan bulanan, termasuk persyaratan minimal tingkat kelengkapan data sebesar 65%. Seluruh kegiatan QC wajib didukung dengan pencatatan dan dokumentasi yang tertib, dapat ditelusuri (traceable), serta mengacu pada Standard Operating Procedures (SOP) sebagai bagian dari sistem manajemen mutu dan audit Quality Assurance (QA). Dengan demikian, pedoman ini menjadi acuan internal dalam pelaksanaan QC alat dan data PM2.5 serta mendukung integrasi data berkualitas ke dalam Database Kualitas Udara Nasional dan penyajian informasi kualitas udara yang kredibel bagi pemangku kepentingan dan masyarakat."""

with left:
    st.markdown(
        """
        <div class="materi-card">
            <div class="materi-header">
                <div class="materi-title-main">🔖 MATERI POKOK</div>
                <div><b>Abstrak</b></div>
            </div>
            <div class="materi-body">
        """,
        unsafe_allow_html=True,
    )

    st.markdown(ringkasan)

    with st.expander("Materi Lengkap"):
        st.markdown(materi_lengkap)

    st.markdown("</div></div>", unsafe_allow_html=True)


# =======================
# FILE EBOOK
# =======================
with right:
    st.markdown("#### File Ebook")
    st.markdown('<div class="file-card">', unsafe_allow_html=True)

    pdf_file = Path(EBOOK_PATH)
    st.markdown(f"**{pdf_file.name if pdf_file.exists() else 'ebook.pdf'}**")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("👁️ Preview"):
            st.session_state.show_pdf = True

    with col2:
        if pdf_file.exists():
            with open(pdf_file, "rb") as f:
                st.download_button(
                    "⬇️ Download",
                    f,
                    file_name=pdf_file.name,
                    mime="application/pdf",
                    use_container_width=True,
                )

    st.markdown("</div>", unsafe_allow_html=True)


# ====================================
# PREVIEW PDF
# ====================================

# if st.session_state.show_pdf:
 #   st.markdown("### Preview Ebook")
  #  pdf64 = load_pdf_base64(EBOOK_PATH)
 #   if pdf64:
   #     st.markdown(
     #       f"""
    #       <iframe src="data:application/pdf;base64,{pdf64}"
   #        width="100%" height="650"></iframe>
          
  #          """,
 #           unsafe_allow_html=True,
#        )

with open(EBOOK_PATH, "rb") as f:
    pdf_bytes = f.read()

b64 = base64.b64encode(pdf_bytes).decode()

st.markdown(
    f"""
    <a href="data:application/pdf;base64,{b64}" target="_blank">
        📖 Open Ebook Preview
    </a>
    """,
    unsafe_allow_html=True,
)




