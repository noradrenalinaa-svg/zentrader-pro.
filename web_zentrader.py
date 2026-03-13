import streamlit as st
import time

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="ZenTrader AI", layout="wide", page_icon="💎")

# --- CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Inter:wght@400;700&display=swap');
    .stApp { background-color: #050505; color: #fff; }
    .main-title { font-family: 'Orbitron'; font-size: 50px; text-align: center; color: #ffd700; }
    .stButton > button { background: #ffd700 !important; color: black !important; border-radius: 50px !important; float: right; }
    .terminal-card { background: rgba(255, 255, 255, 0.03); border: 1px solid #ffd70033; border-radius: 20px; padding: 20px; }
</style>
""", unsafe_allow_html=True)

# --- LOGICA ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown('<h1 class="main-title">ZENTRADER AI</h1>', unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1.2, 1, 0.8])
    with col_btn:
        if st.button("ACCEDI AL TERMINALE"):
            st.session_state['show_login'] = True

    if st.session_state.get('show_login'):
        _, col_login, _ = st.columns([1, 1.5, 1])
        with col_login:
            u = st.text_input("User ID")
            p = st.text_input("Access Key", type="password")
            if st.button("SBLOCCA"):
                if u == "luca" and p == "zen2026":
                    st.session_state['auth'] = True
                    st.rerun()
                else:
                    st.error("Credenziali errate")
else:
    st.sidebar.title("ZEN PRO")
    if st.sidebar.button("LOGOUT"):
        st.session_state['auth'] = False
        st.rerun()

    st.markdown("## 💎 TERMINALE OPERATIVO")
    c1, c2 = st.columns([1, 2])
    with c1:
        st.markdown('<div class="terminal-card">', unsafe_allow_html=True)
        balance = st.number_input("Equità ($)", value=10000)
        risk = st.slider("Rischio %", 0.1, 2.0, 0.5)
        sl = st.number_input("Stop Loss (Pips)", value=20)
        lotti = round((balance * (risk/100)) / (sl * 10), 2)
        st.metric("LOTTI SUGGERITI", lotti)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.components.v1.html("""
            <div id="tv-chart" style="height:500px;"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script>new TradingView.widget({"width": "100%", "height": 500, "symbol": "OANDA:XAUUSD", "interval": "15", "theme": "dark", "style": "1", "locale": "it"});</script>
        """, height=500)
