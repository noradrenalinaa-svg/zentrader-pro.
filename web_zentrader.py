import streamlit as st
import pandas as pd
import sqlite3
import numpy as np
from datetime import datetime

# --- 1. CONFIGURAZIONE ESTETICA E DESIGN (CENTRATURA E COLORI ORIGINALI) ---
st.set_page_config(page_title="ZenTrader AI | Pro Terminal", layout="wide", page_icon="💎")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@400;600&display=swap');
    
    .stApp { background-color: #050505; color: #fff; }

    /* Header Centrato Landing */
    .hero-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 80px 0 20px 0;
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
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(255, 215, 0, 0.5);
    }

    /* Glass Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
    }
    .glass-card h3 { color: #ffd700; }
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

# --- 4. LANDING PAGE ---
if st.session_state['page'] == 'Home' and not st.session_state['auth']:
    st.markdown("""
        <div class="hero-container">
            <h1 class="main-title">ZENTRADER AI</h1>
            <p class="sub-title">Domina il rischio. Scala il tuo capitale.</p>
        </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 0.5, 1])
    with c2:
        if st.button("ACCEDI AL TERMINALE"):
            st.session_state['page'] = 'Login'
            st.rerun()

    st.markdown("<br><br><br>", unsafe_allow_html=True)
    f1, f2, f3 = st.columns(3, gap="large")
    with f1: st.markdown('<div class="glass-card"><h3>🛡️ Protezione 2%</h3><p>Drawdown sotto controllo per ogni Prop Challenge.</p></div>', unsafe_allow_html=True)
    with f2: st.markdown('<div class="glass-card"><h3>⚡ Speed Bridge</h3><p>Calcolo lotti istantaneo sincronizzato con SL.</p></div>', unsafe_allow_html=True)
    with f3: st.markdown('<div class="glass-card"><h3>🧠 AI Sentinel</h3><p>Analisi news macroeconomiche real-time.</p></div>', unsafe_allow_html=True)

# --- 5. LOGIN PAGE ---
elif st.session_state['page'] == 'Login' and not st.session_state['auth']:
    st.markdown("<br><br><h2 style='text-align:center; font-family:Orbitron;'>SECURITY ACCESS</h2>", unsafe_allow_html=True)
    _, col_box, _ = st.columns([1, 0.8, 1])
    with col_box:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("VERIFICA"):
            if u == "luca" and p == "zen2026":
                st.session_state['auth'] = True
                st.session_state['user'] = u
                st.rerun()
            else:
                st.error("Credenziali errate.")
        if st.button("TORNA ALLA HOME"):
            st.session_state['page'] = 'Home'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- 6. TERMINALE OPERATIVO (AUTH) ---
elif st.session_state['auth']:
    st.sidebar.title("💎 ZenTrader Pro")
    nav = st.sidebar.radio("MENU", ["Terminal", "Storico Trade"])
    if st.sidebar.button("LOGOUT"):
        st.session_state['auth'] = False
        st.session_state['page'] = 'Home'
        st.rerun()

    if nav == "Terminal":
        # Barra dei prezzi superiore
        st.markdown("""
            <div style="background: rgba(255,255,255,0.03); padding: 10px; border-radius: 10px; border: 1px solid #333; margin-bottom: 20px;">
                <p style="margin:0; text-align:center; font-family:Orbitron; font-size: 13px; color: #ffd700;">
                    LIVE: XAUUSD 2154.20 | EURUSD 1.0942 | BTCUSD 68420.10 | NAS100 18240.55
                </p>
            </div>
        """, unsafe_allow_html=True)

        col_calc, col_chart = st.columns([1, 2.5], gap="medium")

        with col_calc:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.subheader("🛠️ EXECUTION")
            asset = st.selectbox("Asset", ["XAUUSD", "EURUSD", "NAS100", "BTCUSD"])
            
            # Mapping simboli per TradingView
            tv_map = {"XAUUSD": "OANDA:XAUUSD", "EURUSD": "FX:EURUSD", "NAS100": "CAPITALCOM:US100", "BTCUSD": "BINANCE:BTCUSDT"}
            
            capitale = st.number_input("Equità (€)", value=10000)
            sl_pips = st.number_input("Stop Loss (Pips)", value=10)
            rischio = st.slider("Rischio %", 0.1, 2.0, 1.0)
            
            size = round((capitale * (rischio/100)) / (sl_pips * 10), 2)
            st.markdown(f"<h1 style='color:#ffd700;'>{size}</h1><p style='color:#888;'>LOTTI</p>", unsafe_allow_html=True)
            
            if st.button("ESEGUI ORDINE"):
                st.toast("Ordine inviato!", icon="🚀")
            st.markdown('</div>', unsafe_allow_html=True)

        with col_chart:
            # INTEGRATION TRADINGVIEW
            st.components.v1.html(f"""
                <div id="tv_chart" style="height: 550px;"></div>
                <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
                <script type="text/javascript">
                new TradingView.widget({{
                  "width": "100%", "height": 550, "symbol": "{tv_map[asset]}",
                  "interval": "15", "timezone": "Europe/Rome", "theme": "dark",
                  "style": "1", "locale": "it", "enable_publishing": false,
                  "container_id": "tv_chart"
                }});
                </script>
            """, height=560)
