import streamlit as st
import pandas as pd
import sqlite3
import numpy as np
from datetime import datetime

# --- 1. CONFIGURAZIONE ESTETICA ---
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
        display: inline-block;
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
        padding: 20px;
        border-top: 2px solid #ff8c00;
        font-style: italic;
        color: #ddd;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. NAVIGAZIONE ---
if 'page' not in st.session_state: st.session_state['page'] = 'Home'
if 'auth' not in st.session_state: st.session_state['auth'] = False

# --- 3. VISTA: LANDING PAGE ---
if st.session_state['page'] == 'Home' and not st.session_state['auth']:
    st.markdown("""
        <div class="hero-container">
            <h1 class="main-title">ZENTRADER AI</h1>
            <p class="sub-title">Il terminale avanzato che protegge il tuo capitale dall'emotività.</p>
        </div>
    """, unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 0.6, 1])
    with col_btn:
        if st.button("PROVA IL TERMINALE →"):
            st.session_state['page'] = 'Login'
            st.rerun()

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Confronto
    st.markdown("<h2 style='text-align:center; font-family:Orbitron; font-size: 24px;'>OTTIENI UN VANTAGGIO STATISTICO</h2>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2, gap="large")
    with col_a:
        st.markdown("""<div style="padding:25px; border-left: 4px solid #ff4b4b; background: rgba(255,75,75,0.07); border-radius:0 15px 15px 0;"><h4 style="color:#ff4b4b; font-family:Orbitron;">❌ TRADING MANUALE</h4><p style="color:#ccc;">• Calcolo size lento e impreciso.<br>• Esposizione rischiosa durante le news.<br>• Violazione del drawdown massimo.<br>• Stress decisionale costante.</p></div>""", unsafe_allow_html=True)
    with col_b:
        st.markdown("""<div style="padding:25px; border-left: 4px solid #00ff00; background: rgba(0,255,0,0.07); border-radius:0 15px 15px 0;"><h4 style="color:#00ff00; font-family:Orbitron;">✅ METODO ZENTRADER</h4><p style="color:#ccc;">• Calcolo istantaneo della size.<br>• Blocco operativo durante i dati macro.<br>• Drawdown rigido al 2% (Prop Ready).<br>• Analisi oggettiva post-sessione.</p></div>""", unsafe_allow_html=True)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # TESTIMONIANZE
    st.markdown("<h2 style='text-align:center; font-family:Orbitron; font-size: 24px;'>COSA DICONO I NOSTRI TRADER</h2>", unsafe_allow_html=True)
    t1, t2, t3 = st.columns(3)
    with t1:
        st.markdown("""<div class="testimonial-card">"Finalmente ho superato la mia prima sfida da 100k. Senza il blocco del drawdown avrei bruciato tutto al terzo giorno. ZenTrader è una garanzia."<br><br><b>- Marco R. (Prop Trader)</b></div>""", unsafe_allow_html=True)
    with t2:
        st.markdown("""<div class="testimonial-card">"Lo Speed Bridge per il calcolo dei lotti sull'oro è impressionante. Risparmio secondi preziosi che prima mi facevano perdere l'entry migliore."<br><br><b>- Alessandro V. (Scalper)</b></div>""", unsafe_allow_html=True)
    with t3:
        st.markdown("""<div class="testimonial-card">"L'AI Sentinel mi ha salvato da tre news ad alto impatto questo mese. Un software che si paga da solo in una singola operazione."<br><br><b>- Elena S. (Swing Trader)</b></div>""", unsafe_allow_html=True)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Pricing
    _, p_col, _ = st.columns([1, 1, 1])
    with p_col:
        st.markdown("""
            <div style="background: linear-gradient(145deg, #ffd700, #ff8c00); padding: 40px; border-radius: 30px; text-align: center; color: black; box-shadow: 0 10px 30px rgba(255,215,0,0.2);">
                <h2 style="margin:0; font-family:Orbitron; font-size: 22px;">ELITE ACCESS</h2>
                <h1 style="font-size: 60px; margin:10px 0;">€49<span style="font-size:20px;">/mese</span></h1>
                <p style="font-weight:700;">STRUMENTI PROFESSIONALI</p>
                <p style="font-size:13px;">Prendi il controllo della tua carriera nel trading.</p>
            </div>
        """, unsafe_allow_html=True)

# --- 4. VISTA: LOGIN ---
elif st.session_state['page'] == 'Login' and not st.session_state['auth']:
    st.markdown("<br><br><h2 style='text-align:center; font-family:Orbitron;'>ACCESSO RISERVATO</h2>", unsafe_allow_html=True)
    _, col_box, _ = st.columns([1, 0.7, 1])
    with col_box:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        u = st.text_input("User ID")
        p = st.text_input("Access Key", type="password")
        if st.button("ENTRA"):
            if u == "luca" and p == "zen2026":
                st.session_state['auth'] = True
                st.rerun()
            else: st.error("Credenziali non valide.")
        if st.button("← TORNA ALLA HOME"):
            st.session_state['page'] = 'Home'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- 5. TERMINALE (VERSIONE COMPLETA) ---
elif st.session_state['auth']:
    st.sidebar.markdown("<h1 style='color:#ffd700; font-family:Orbitron;'>ZEN PRO</h1>", unsafe_allow_html=True)
    if st.sidebar.button("LOGOUT"):
        st.session_state['auth'] = False
        st.session_state['page'] = 'Home'
        st.rerun()
    
    st.markdown("<h2 style='font-family:Orbitron;'>DASHBOARD OPERATIVA</h2>", unsafe_allow_html=True)
    c_exec, c_chart = st.columns([1, 2.5])
    with c_exec:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        asset = st.selectbox("Seleziona Asset", ["XAUUSD", "EURUSD", "NAS100", "BTCUSD"])
        cap = st.number_input("Equità (€)", value=10000)
        sl = st.number_input("Stop Loss (Pips)", value=15)
        risk = st.slider("Rischio %", 0.1, 2.0, 1.0)
        size = round((cap * (risk/100)) / (sl * 10), 2)
        st.markdown(f"<p style='color:#888;'>LOTTAGGIO CALCOLATO</p><h1 style='color:#ffd700;'>{size}</h1>", unsafe_allow_html=True)
        st.button("ESEGUI")
        st.markdown('</div>', unsafe_allow_html=True)
    with c_chart:
        tv_map = {"XAUUSD": "OANDA:XAUUSD", "EURUSD": "FX:EURUSD", "NAS100": "CAPITALCOM:US100", "BTCUSD": "BINANCE:BTCUSDT"}
        st.components.v1.html(f"""
            <div id="tv" style="height: 550px;"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script type="text/javascript">
            new TradingView.widget({{"width": "100%", "height": 550, "symbol": "{tv_map[asset]}", "interval": "15", "theme": "dark", "style": "1", "locale": "it", "container_id": "tv"}});
            </script>
        """, height=560)