import streamlit as st
import pandas as pd
import sqlite3
import numpy as np
from datetime import datetime

# --- 1. CONFIGURAZIONE ESTETICA (DESIGN PREMIUM & CENTRATURA) ---
st.set_page_config(page_title="ZenTrader AI | Professional Trading Systems", layout="wide", page_icon="💎")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@300;400;600;700&display=swap');
    
    .stApp { background-color: #050505; color: #fff; }

    /* Header Centrato Landing */
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

    /* Bottoni Centrati e Gradienti */
    div.stButton { text-align: center; }
    div.stButton > button {
        background: linear-gradient(45deg, #ffd700, #ff8c00) !important;
        color: #000 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        padding: 16px 45px !important;
        border-radius: 12px !important;
        border: none !important;
        display: inline-block;
        box-shadow: 0 4px 15px rgba(255, 140, 0, 0.3);
        transition: 0.3s;
    }

    /* Glass Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        height: 100%;
    }
    .glass-card h3 { color: #ffd700; font-family: 'Orbitron', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGICA DATABASE ---
def init_db():
    conn = sqlite3.connect('zentrader_pro.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS trades (user TEXT, data TEXT, asset TEXT, lotti REAL, rischio REAL)')
    conn.commit()
    conn.close()

init_db()

# --- 3. NAVIGAZIONE ---
if 'page' not in st.session_state: st.session_state['page'] = 'Home'
if 'auth' not in st.session_state: st.session_state['auth'] = False

# --- 4. VISTA: LANDING PAGE PROFESSIONALE ---
if st.session_state['page'] == 'Home' and not st.session_state['auth']:
    st.markdown("""
        <div class="hero-container">
            <h1 class="main-title">ZENTRADER AI</h1>
            <p class="sub-title">L'unico Terminale che protegge il tuo capitale dalla tua emotività.</p>
        </div>
    """, unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 0.6, 1])
    with col_btn:
        if st.button("PROVA IL TERMINALE →"):
            st.session_state['page'] = 'Login'
            st.rerun()

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Confronto Trader Comune vs Zen
    st.markdown("<h2 style='text-align:center; font-family:Orbitron;'>IL TUO BORDO STATISTICO</h2>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2, gap="large")
    with col_a:
        st.markdown("""
            <div style="padding:25px; border-left: 4px solid #ff4b4b; background: rgba(255,75,75,0.07); border-radius:0 15px 15px 0;">
                <h4 style="color:#ff4b4b; font-family:Orbitron;">❌ TRADER COMUNE</h4>
                <p style="color:#ccc;">• Calcolo lotti manuale e impreciso.<br>• Entra a mercato durante news macro.<br>• Brucia il conto superando il drawdown.<br>• Decide in preda all'ansia o all'avidità.</p>
            </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("""
            <div style="padding:25px; border-left: 4px solid #00ff00; background: rgba(0,255,0,0.07); border-radius:0 15px 15px 0;">
                <h4 style="color:#00ff00; font-family:Orbitron;">✅ TRADER ZEN</h4>
                <p style="color:#ccc;">• Esecuzione matematica in 0.4 secondi.<br>• AI Sentinel blocca l'accesso nei dati macro.<br>• Drawdown rigido al 2% (Prop Ready).<br>• Analisi psicologica post-trade inclusa.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Servizi
    s1, s2, s3 = st.columns(3)
    with s1: st.markdown('<div class="glass-card"><h3>📊 Prop Shield</h3><p>Protezione automatica del limite giornaliero per FTMO e MyFundedFX.</p></div>', unsafe_allow_html=True)
    with s2: st.markdown('<div class="glass-card"><h3>🚀 Quantum Calc</h3><p>Calcolo lotti ATR-based per ottimizzare il rischio sulla volatilità reale.</p></div>', unsafe_allow_html=True)
    with s3: st.markdown('<div class="glass-card"><h3>📜 Audit Report</h3><p>Analisi mensile della tua psicologia operativa in formato PDF.</p></div>', unsafe_allow_html=True)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Pricing
    _, p_col, _ = st.columns([1, 1, 1])
    with p_col:
        st.markdown("""
            <div style="background: linear-gradient(145deg, #ffd700, #ff8c00); padding: 40px; border-radius: 30px; text-align: center; color: black;">
                <h2 style="margin:0; font-family:Orbitron;">ELITE PLAN</h2>
                <h1 style="font-size: 60px; margin:10px 0;">€49<span style="font-size:20px;">/mese</span></h1>
                <p style="font-weight:bold;">TUTTI I SERVIZI INCLUSI</p>
                <p style="font-size:12px; margin-top:10px;">Attiva il tuo vantaggio competitivo oggi.</p>
            </div>
        """, unsafe_allow_html=True)

# --- 5. VISTA: LOGIN ---
elif st.session_state['page'] == 'Login' and not st.session_state['auth']:
    st.markdown("<br><br><h2 style='text-align:center; font-family:Orbitron;'>SECURITY ACCESS</h2>", unsafe_allow_html=True)
    _, col_box, _ = st.columns([1, 0.7, 1])
    with col_box:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        u = st.text_input("User ID")
        p = st.text_input("Access Key", type="password")
        if st.button("VERIFY"):
            if u == "luca" and p == "zen2026":
                st.session_state['auth'] = True
                st.session_state['user'] = u
                st.rerun()
            else: st.error("Accesso Negato.")
        if st.button("← BACK"):
            st.session_state['page'] = 'Home'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- 6. VISTA: TERMINALE OPERATIVO ---
elif st.session_state['auth']:
    st.sidebar.markdown("<h1 style='color:#ffd700; font-family:Orbitron;'>ZEN PRO</h1>", unsafe_allow_html=True)
    nav = st.sidebar.radio("SISTEMA", ["Terminal", "Storico"])
    if st.sidebar.button("LOGOUT"):
        st.session_state['auth'] = False
        st.session_state['page'] = 'Home'
        st.rerun()

    if nav == "Terminal":
        st.markdown("""<div style="background:rgba(255,215,0,0.1); padding:10px; border-radius:10px; text-align:center; border:1px solid #ffd700; margin-bottom:20px; font-family:Orbitron; font-size:12px; color:#ffd700;">LIVE FEED: XAUUSD 2154.20 | EURUSD 1.0942 | BTCUSD 68420.10</div>""", unsafe_allow_html=True)
        
        col_exec, col_chart = st.columns([1, 2.5], gap="medium")
        
        with col_exec:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            asset = st.selectbox("Asset", ["XAUUSD", "EURUSD", "NAS100", "BTCUSD"])
            cap = st.number_input("Equity (€)", value=10000)
            sl = st.number_input("SL (Pips)", value=15)
            risk = st.slider("Risk %", 0.1, 2.0, 1.0)
            
            size = round((cap * (risk/100)) / (sl * 10), 2)
            st.markdown(f"<p style='color:#888; font-size:12px;'>LOTTAGGIO CALCOLATO</p><h1 style='color:#ffd700;'>{size}</h1>", unsafe_allow_html=True)
            if st.button("EXECUTE"): st.toast("Ordine Inviato!", icon="🚀")
            st.markdown('</div>', unsafe_allow_html=True)

        with col_chart:
            tv_map = {"XAUUSD": "OANDA:XAUUSD", "EURUSD": "FX:EURUSD", "NAS100": "CAPITALCOM:US100", "BTCUSD": "BINANCE:BTCUSDT"}
            st.components.v1.html(f"""
                <div id="tv" style="height: 550px;"></div>
                <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
                <script type="text/javascript">
                new TradingView.widget({{"width": "100%", "height": 550, "symbol": "{tv_map[asset]}", "interval": "15", "theme": "dark", "style": "1", "locale": "it", "container_id": "tv"}});
                </script>
            """, height=560)