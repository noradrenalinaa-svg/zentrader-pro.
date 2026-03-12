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

    # Sezione Confronto migliorata
    st.markdown("<h2 style='text-align:center; font-family:Orbitron; font-size: 24px;'>OTTIENI UN VANTAGGIO STATISTICO</h2>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2, gap="large")
    with col_a:
        st.markdown("""
            <div style="padding:25px; border-left: 4px solid #ff4b4b; background: rgba(255,75,75,0.07); border-radius:0 15px 15px 0;">
                <h4 style="color:#ff4b4b; font-family:Orbitron;">❌ TRADING MANUALE</h4>
                <p style="color:#ccc; line-height: 1.6;">
                • Calcolo della size approssimativo o lento.<br>
                • Esposizione inconsapevole durante i dati macro.<br>
                • Violazione del drawdown massimo consentito.<br>
                • Operatività influenzata da ansia e stress.
                </p>
            </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("""
            <div style="padding:25px; border-left: 4px solid #00ff00; background: rgba(0,255,0,0.07); border-radius:0 15px 15px 0;">
                <h4 style="color:#00ff00; font-family:Orbitron;">✅ METODO ZENTRADER</h4>
                <p style="color:#ccc; line-height: 1.6;">
                • Algoritmo di calcolo istantaneo della size.<br>
                • AI Sentinel: blocco operativo durante le news.<br>
                • Gestione rigida del Drawdown al 2% (Prop Ready).<br>
                • Analisi oggettiva delle performance post-trade.
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Servizi rifiniti
    s1, s2, s3 = st.columns(3)
    with s1: 
        st.markdown('<div class="glass-card"><h3>🛡️ Prop Shield</h3><p>Proteggi i tuoi conti FTMO o MyFundedFX con il controllo automatico delle perdite giornaliere.</p></div>', unsafe_allow_html=True)
    with s2: 
        st.markdown('<div class="glass-card"><h3>⚡ Quantum Calc</h3><p>Calcola il lotto perfetto basandoti sulla volatilità ATR per ottimizzare il rischio/rendimento.</p></div>', unsafe_allow_html=True)
    with s3: 
        st.markdown('<div class="glass-card"><h3>🧠 AI Sentinel</h3><p>Analisi predittiva del calendario economico per evitare picchi di volatilità non pianificati.</p></div>', unsafe_allow_html=True)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Pricing
    _, p_col, _ = st.columns([1, 1, 1])
    with p_col:
        st.markdown("""
            <div style="background: linear-gradient(145deg, #ffd700, #ff8c00); padding: 40px; border-radius: 30px; text-align: center; color: black; box-shadow: 0 10px 30px rgba(255,215,0,0.2);">
                <h2 style="margin:0; font-family:Orbitron; font-size: 22px;">ELITE ACCESS</h2>
                <h1 style="font-size: 60px; margin:10px 0;">€49<span style="font-size:20px;">/mese</span></h1>
                <p style="font-weight:700; margin-bottom: 5px;">STRUMENTI PROFESSIONALI</p>
                <p style="font-size:13px;">Assicura la tua scalata verso il successo nelle Prop House.</p>
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
                st.session_state['user'] = u
                st.rerun()
            else: st.error("Credenziali non valide.")
        if st.button("← TORNA ALLA HOME"):
            st.session_state['page'] = 'Home'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- 5. TERMINALE (VERSIONE COMPLETA) ---
elif st.session_state['auth']:
    # [Qui rimane il codice del terminale che abbiamo già settato]
    st.sidebar.markdown("<h1 style='color:#ffd700; font-family:Orbitron;'>ZEN PRO</h1>", unsafe_allow_html=True)
    if st.sidebar.button("LOGOUT"):
        st.session_state['auth'] = False
        st.session_state['page'] = 'Home'
        st.rerun()
    
    st.markdown("<h2 style='font-family:Orbitron;'>DASHBOARD OPERATIVA</h2>", unsafe_allow_html=True)
    # [Aggiungi qui le colonne del calcolatore e di TradingView come nel codice precedente]
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
        st.components.v1.html("""<div style="height:550px; background:#111; border-radius:20px; display:flex; align-items:center; justify-content:center; color:#444;">[Grafico TradingView Attivo]</div>""", height=560)