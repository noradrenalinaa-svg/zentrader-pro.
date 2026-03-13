import streamlit as st
import pandas as pd
import numpy as np

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="ZenTrader AI", layout="wide", page_icon="💎")

# --- MONITORAGGIO (Analytics) ---
# Se ti iscrivi a Google Analytics o Umami, incolla qui il loro script.
# Per ora inseriamo un piccolo tracciatore invisibile.
st.markdown("""
<script async src="https://www.googletagmanager.com/gtag/js?id=TUO_ID_QUI"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'TUO_ID_QUI');
</script>
""", unsafe_allow_html=True)

# --- CSS INTEGRATO ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@400;700&display=swap');
    .stApp { background-color: #050505; color: #fff; }
    .main-title { font-family: 'Orbitron'; font-size: 70px; text-align: center; background: linear-gradient(90deg, #ffd700, #ff8c00); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0px;}
    .section-title { font-family: 'Orbitron'; color: #ffd700; text-align: center; margin-top: 50px; }
    .price-card { background: linear-gradient(145deg, #ffd700, #ff8c00); padding: 40px; border-radius: 30px; text-align: center; color: black; box-shadow: 0 10px 30px rgba(255,215,0,0.3); }
    .pay-btn { background-color: black; color: white !important; padding: 15px 30px; border-radius: 10px; text-decoration: none; display: block; margin: 20px auto; font-family: 'Orbitron'; font-weight: bold; width: 200px; }
    .tg-btn { color: black !important; text-decoration: underline; font-weight: bold; font-size: 14px; }
    .about-box { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); padding: 30px; border-radius: 20px; line-height: 1.6; }
</style>
""", unsafe_allow_html=True)

# --- LOGICA NAVIGAZIONE ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

# --- HOME PAGE ---
if not st.session_state['auth']:
    st.markdown('<h1 class="main-title">ZENTRADER AI</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888; letter-spacing: 2px;'>ALGORITHMIC TRADING TERMINAL</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Pulsante Accesso Rapido
    _, col_btn, _ = st.columns([1, 0.6, 1])
    with col_btn:
        with st.expander("🔑 ACCEDI AL TERMINALE"):
            u = st.text_input("User")
            p = st.text_input("Password", type="password")
            if st.button("ENTRA"):
                if u == "luca" and p == "zen2026":
                    st.session_state['auth'] = True
                    st.rerun()
                else:
                    st.error("Credenziali errate")

    st.markdown("---")

    # SEZIONE: CHI SIAMO
    st.markdown('<h2 class="section-title">CHI SIAMO</h2>', unsafe_allow_html=True)
    _, ab_col, _ = st.columns([0.2, 1, 0.2])
    with ab_col:
        st.markdown("""
        <div class="about-box">
            <p style="font-size: 18px; text-align: center;">
                <b>ZenTrader AI</b> nasce dall'esigenza di eliminare il nemico numero uno di ogni trader: <b>l'emotività</b>.<br><br>
                Siamo un team di sviluppatori e trader indipendenti specializzati nella protezione del capitale. 
                In un mercato dominato da algoritmi HFT, il trader retail deve dotarsi di strumenti che impongano disciplina. 
                La nostra missione è fornire un terminale che calcoli il rischio matematico al posto tuo e blocchi l'operatività 
                quando il tuo piano di trading è a rischio (Drawdown 2%).
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # SEZIONE PREZZI
    st.markdown('<h2 class="section-title">PIANI DI ACCESSO</h2>', unsafe_allow_html=True)
    _, p_col, _ = st.columns([1, 1, 1])
    with p_col:
        st.markdown("""
<div class="price-card">
    <h2 style="margin:0; font-family:Orbitron;">ELITE ACCESS</h2>
    <h1 style="font-size: 55px; margin:10px 0;">€49<span style="font-size:20px;">/mese</span></h1>
    <p><b>PRO SHIELD & DRAWDOWN 2%</b></p>
    <ul style="list-style:none; padding:0; text-align:left; font-size:14px; margin-bottom: 20px;">
        <li>✔️ Calcolo Size Istantaneo (Gold/Forex)</li>
        <li>✔️ AI News Sentinel (Real-time)</li>
        <li>✔️ Gestione Rischio Integrata</li>
    </ul>
    <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=noradrenalinaa@gmail.com&item_name=ZenTrader%20AI%20Elite&amount=49.00&currency_code=EUR" target="_blank" class="pay-btn">ACQUISTA ORA</a>
    <a href="https://t.me/ZenTraderIA" target="_blank" class="tg-btn">Contatta il Fondatore</a>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br><br><br><p style='text-align:center; color:#444; font-size:12px;'>© 2026 ZenTrader AI. All rights reserved.</p>", unsafe_allow_html=True)

# --- TERMINALE (Dopo il Login) ---
else:
    st.sidebar.title("💎 ZenTrader Pro")
    if st.sidebar.button("LOGOUT"):
        st.session_state['auth'] = False
        st.rerun()
    
    st.header("Dashboard Operativa")
    st.info(f"Benvenuto Luca. Protezione Drawdown attiva al 2%.")
    
    # Qui rimetteremo il calcolatore e il grafico nel prossimo step
    st.write("Configurazione terminale in corso...")