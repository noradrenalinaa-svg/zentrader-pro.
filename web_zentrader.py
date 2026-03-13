import streamlit as st
import pandas as pd
import sqlite3
import numpy as np
from datetime import datetime

# --- 1. CONFIGURAZIONE ESTETICA PREMIUM ---
st.set_page_config(page_title="ZenTrader AI | Professional Trading Terminal", layout="wide", page_icon="💎")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@300;400;600;700&display=swap');
    
    .stApp { background-color: #050505; color: #fff; }

    .hero-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 60px 0 20px 0;
        width: 100%;
    }

    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 85px;
        font-weight: 900;
        background: linear-gradient(90deg, #ffd700, #ff8c00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        letter-spacing: -3px;
    }

    .sub-title {
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        color: #888;
        letter-spacing: 3px;
        margin-bottom: 40px;
        text-transform: uppercase;
        font-weight: 600;
    }

    div.stButton { text-align: center; }
    div.stButton > button {
        background: linear-gradient(45deg, #ffd700, #ff8c00) !important;
        color: #000 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        padding: 16px 45px !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(255, 140, 0, 0.3);
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        height: 100%;
    }
    .glass-card h3 { color: #ffd700; font-family: 'Orbitron', sans-serif; font-size: 20px; }

    .testimonial-card {
        background: rgba(255, 255, 255, 0.02);
        border-radius: 15px;
        padding: 25px;
        border-top: 2px solid #ff8c00;
        font-style: italic;
        color: #ddd;
        height: 100%;
    }

    .buy-button {
        background-color: #000;
        color: #fff !important;
        padding: 18px;
        border-radius: 12px;
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        text-decoration: none;
        display: block;
        margin-top: 20px;
        transition: 0.3s;
        border: 1px solid #000;
        text-align: center;
    }
    .buy-button:hover {
        background-color: #222