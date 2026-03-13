import streamlit as st
import pandas as pd
import numpy as np

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="ZenTrader AI", layout="wide", page_icon="💎")

# --- CSS INTEGRATO ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@400;700&display=swap');
    .stApp { background-color: #050505; color: #fff; }
    .main-title { font-family: 'Orbitron'; font-size: 70px; text-align: center; background: linear-gradient(90deg, #ffd700, #ff8c00); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .price-card { background: linear-gradient(145deg, #ffd700, #ff8c00); padding: 40px; border-radius: 30px; text-align: center; color: black; }
    .pay-btn { background-color: black; color: white !important; padding: 15px 30px; border-radius: 10px; text-decoration: none; display: block; margin: 20px auto; font-family: 'Orbitron'; font-weight: bold; width: 200px; }
    .tg-btn { color: black !important; text-decoration: underline; font-weight: bold; font-size: 14px; }
</style>
""", unsafe_allow_html=True)

# --- LOGICA NAVIGAZIONE ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

# --- HOME PAGE ---
if not st.session_state['auth']:
    st.markdown('<h1 class="main-title">ZENTRADER AI</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888;'>TERMINALE PROFESSIONALE ANTI-EMOTIVITÀ</p>", unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 0.6, 1])
    with col_btn:
        if st.button("PROVA IL TERMINALE →"):
            # Simuliamo il login per ora per farti testare il resto
            st.info("Usa le credenziali: luca / zen2026")
            u = st.text_input("User")
            p = st.text_input("Password", type="password")
            if st.button("ACCEDI"):
                if u == "luca" and p == "zen2026":
                    st.session_state['auth'] = True
                    st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # SEZIONE PREZZI - IL CUORE DEL PROBLEMA
    _, p_col, _ = st.columns([1, 1, 1])
    with p_col:
        st.markdown("""
<div class="price-card">
    <h2 style="margin:0; font-family:Orbitron;">ELITE ACCESS</h2>
    <h1 style="font-size: 55px; margin:10px 0;">€49<span style="font-size:20px;">/mese</span></h1>
    <p><b>PRO SHIELD & DRAWDOWN 2%</b></p>
    <ul style="list-style:none; padding:0; text-align:left; font-size:14px;">
        <li>✔️ Calcolo Size Istantaneo</li>
        <li>✔️ AI News Sentinel</li>
        <li>✔️ No Trading Emotivo</li>
    </ul>
    <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=noradrenalinaa@gmail.com&item_name=ZenTrader%20AI%20Elite&amount=49.00&currency_code=EUR" target="_blank" class="pay-btn">PAGA ORA</a>
    <a href="https://t.me/ZenTraderIA" target="_blank" class="tg-btn">Contatta il Supporto</a>
</div>
""", unsafe_allow_html=True)

# --- TERMINALE ---
else:
    st.title("Dashboard ZenTrader")
    if st.button("LOGOUT"):
        st.session_state['auth'] = False
        st.rerun()
    st.write("Benvenuto Luca. Il terminale è attivo.")