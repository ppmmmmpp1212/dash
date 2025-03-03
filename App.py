import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

st.set_page_config(page_icon="Screenshot 2025-02-20 153019.png", layout="wide")

# Menu horizontal
selected_dashboard = option_menu(
    menu_title=None,  
    options=["LinkAja TopUp", "RS Produktif Manfee", "Profit Loss 2025", "Chip Tracking"],
    icons=["1-circle", "2-circle", "3-circle", "4-circle"],  
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

# Garis pemisah
st.markdown("<hr style='border: 1px solid #ddd; margin: 10px 0;'>", unsafe_allow_html=True)

# Daftar URL untuk dashboard Looker Studio
dashboard_urls = {
    "LinkAja TopUp": "https://lookerstudio.google.com/embed/reporting/4dd368aa-68c0-48c3-9e07-c4cef769d6a9/page/p_k6il67mwnd",
    "RS Produktif Manfee": "https://lookerstudio.google.com/embed/reporting/da0a0f51-6869-44b1-9fa8-473a02f6aa8b/page/p_k6il67mwnd",
    "Profit Loss 2025": "https://lookerstudio.google.com/embed/reporting/a4824fc2-1744-4871-a858-aae4addb1370/page/p_mnvum4bgfd",
    "Chip Tracking": "https://m2p2dash.streamlit.app/"  # URL aplikasi Streamlit
}

# Pilih URL berdasarkan dashboard yang dipilih
selected_url = dashboard_urls[selected_dashboard]

# Layout kolom untuk menjaga konsistensi
col1, col2, col3 = st.columns([1, 22, 1])

with col2:
    if selected_dashboard == "Chip Tracking":
        # Tampilkan tautan untuk Chip Tracking
        st.markdown(
            f"""
            <h3 style='text-align: center;'>Chip Tracking</h3>
            <p style='text-align: center;'>Klik tautan berikut untuk mengakses aplikasi Chip Tracking:</p>
            <p style='text-align: center;'><a href='{selected_url}' target='_blank'>Buka MMPP Chip Tracking</a></p>
            """,
            unsafe_allow_html=True
        )
    else:
        # Tampilkan iframe untuk dashboard Looker Studio lainnya
        components.iframe(selected_url, width=1400, height=1000, scrolling=False)
