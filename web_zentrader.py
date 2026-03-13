
       
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
    .terminal-card { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 215, 0, 0.2); border-radius: 20px; padding: 25px; }
    .price-card { background: linear-gradient(145deg, #ffd700, #ff8c00); padding: 40px; border-radius: 30px; color: black; text-align: center; }
    .review-card { background: rgba(255, 255, 255, 0.02); padding: 20px; border-radius: 15px; border-left: 3px solid #ffd700; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DI ACCESSO ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

# --- 4. SEZIONE HOME (PRIMA DEL LOGIN) ---
if not st.session_state['auth']:
    st.markdown('<h1 class="main-title">ZENTRADER AI</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; letter-spacing: 3px;'>ELIMINATE EMOTIONS. MAXIMIZE DISCIPLINE.</p>", unsafe_allow_html=True)
    
    # TASTO ACCESSO A DESTRA
    _, col_btn, col_spacer = st.columns([1.2, 1, 0.8])
    with col_btn:
        if 'show_login' not in st.session_state: st.session_state.show_login = False
        if st.button("ACCEDI AL TERMINALE"):
            st.session_state.show_login = not st.session_state.show_login

    if st.session_state.show_login:
        _, col_login, _ = st.columns([1, 1.5, 1])
        with col_login:
            st.markdown('<div style="background: rgba(255,255,255,0.03); padding:20px; border-radius:15px; margin-top:50px; clear:both;">', unsafe_allow_html=True)
            u = st.text_input("User ID")
            p = st.text_input("Access Key", type="password")
            if st.button("SBLOCCA"):
                if u == "luca" and p == "zen2026":
                    st.session_state['auth'] = True
                    st.rerun()
                else: st.error("Credenziali errate")
            st.markdown('</div>', unsafe_allow_html=True)

    # RECENSIONI E PREZZI (Per non lasciare la home vuota)
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="review-card">"Drawdown al 2% salvavita."<br><b>- Marco T.</b></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="review-card">"Size perfette in 1 secondo."<br><b>- Andrea L.</b></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="review-card">"Elite trading tool."<br><b>- Giulia R.</b></div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    _, p_col, _ = st.columns([1, 1, 1])
    with p_col:
        st.markdown('<div class="price-card"><h2>€49/mese</h2><p>Rinnovo Automatico</p><a href="https://paypal.me/tuolink" style="color:black; font-weight:bold;">ATTIVA ORA</a></div>', unsafe_allow_html=True)

    # FAQ
    with st.expander("Abbonamento?"): st.write("Rinnovo automatico ogni 30gg via PayPal.")
    with st.expander("Asset?"): st.write("Oro, Forex, Indici, Crypto.")

# --- 5. SEZIONE TERMINALE (DOPO IL LOGIN) ---
else:
    st.sidebar.markdown("<h2 style='color:#ffd700; font-family:Orbitron;'>ZEN PRO</h2>", unsafe_allow_html=True)
    if st.sidebar.button("LOGOUT"):
        st.session_state['auth'] = False
        st.rerun()

    st.markdown("<h2 style='font-family:Orbitron; color:#ffd700;'>OPERATIONAL TERMINAL</h2>", unsafe_allow_html=True)
    
    col_1, col_2 = st.columns([1, 2.2])
    
    with col_1:
        st.markdown('<div class="terminal-card">', unsafe_allow_html=True)
        st.markdown("### 📊 Calcolatore Size")
        asset = st.selectbox("Asset", ["XAUUSD (Gold)", "EURUSD", "NAS100", "BTCUSD"])
        balance = st.number_input("Equità Conto ($)", value=10000)
        risk = st.slider("Rischio %", 0.1, 2.0, 0.5)
        sl_pips = st.number_input("Stop Loss (Pips)", value=20)
        
        # Calcolo Lotti
        risk_cash = balance * (risk / 100)
        lotti = round(risk_cash / (sl_pips * 10), 2)
        
        st.divider()
        st.metric("LOTTI DA APRIRE", lotti)
        st.info("Esegui l'ordine su MT4/MT5 con questa size.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_2:
        # Mappa simboli TradingView
        tv_sym = {"XAUUSD (Gold)": "OANDA:XAUUSD", "EURUSD": "FX:EURUSD", "NAS100": "CAPITALCOM:US100", "BTCUSD": "BINANCE:BTCUSDT"}
        
        st.components.v1.html(f"""
            <div id="tv-chart" style="height:600px;"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script>
            new TradingView.widget({{
              "width": "100%", "height": 600, "symbol": "{tv_sym[asset]}",
              "interval": "15", "theme": "dark", "style": "1", "locale": "it", "enable_publishing": false
            }});
            </script>
        """, height=600)

    st.caption("ZenTrader Sentinel v2.8 - Protezione 2% Drawdown Attiva.")
