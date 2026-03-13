import streamlit as st
import time

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="ZenTrader AI", layout="wide", page_icon="💎")

# --- 2. CSS PREMIUM ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@300;400;700&display=swap');
    .stApp { background-color: #050505; color: #fff; }
    .main-title { font-family: 'Orbitron'; font-size: clamp(30px, 5vw, 60px); text-align: center; background: linear-gradient(90deg, #ffd700, #ff8c00); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .stButton > button { background: rgba(255, 255, 255, 0.05) !important; color: #ffd700 !important; border: 1px solid #ffd700 !important; border-radius: 50px !important; padding: 10px 40px !important; float: right; }
    .terminal-card { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 215, 0, 0.2); border-radius: 20px; padding: 20px; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DI ACCESSO ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

# --- 4. SE NON È AUTENTICATO (HOME) ---
if not st.session_state['auth']:
    st.markdown('<h1 class="main-title">ZENTRADER AI</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666;'>PROTECTION ACTIVE - 2% DRAWDOWN LIMIT</p>", unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1.2, 1, 0.8])
    with col_btn:
        if 'show_login' not in st.session_state: st.session_state.show_login = False
        if st.button("ACCEDI AL TERMINALE"):
            st.session_state.show_login = not st.session_state.show_login

    if st.session_state.show_login:
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

# --- 5. SE È AUTENTICATO (TERMINALE) ---
else:
    st.sidebar.title("ZEN PRO")
    if st.sidebar.button("LOGOUT"):
        st.session_state['auth'] = False
        st.rerun()

    st.markdown("## 💎 TERMINALE OPERATIVO")
    
    col_1, col_2 = st.columns([1, 2])
    
    with col_1:
        st.markdown('<div class="terminal-card">', unsafe_allow_html=True)
        st.subheader("Calcolatore")
        asset = st.selectbox("Asset", ["XAUUSD", "EURUSD", "NAS100"])
        balance = st.number_input("Equità ($)", value=10000)
        risk = st.slider("Rischio %", 0.1, 2.0, 0.5)
        sl = st.number_input("Stop Loss (Pips)", value=20)
        
        lotti = round((balance * (risk/100)) / (sl * 10), 2)
        st.metric("Lotti Suggeriti", lotti)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_2:
        st.components.v1.html("""
            <div id="tv-chart" style="height:500px;"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script>
            new TradingView.widget({
              "width": "100%", "height": 500, "symbol": "FX:EURUSD",
              "interval": "15", "theme": "dark", "style": "1", "locale": "it"
            });
            </script>
        """, height=500)
