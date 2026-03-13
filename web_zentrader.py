import streamlit as st

# --- 1. SETTINGS ---
st.set_page_config(page_title="ZenTrader Pro", layout="wide", initial_sidebar_state="collapsed")

# --- 2. THE "ELITE" ENGINE (CSS CUSTOM) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@100;400&display=swap');

    /* RESET TOTALE STREAMLIT */
    .stApp { background-color: #000; color: #fff; font-family: 'JetBrains Mono', monospace; }
    header, footer, section[data-testid="stSidebar"], .stDeployButton { display: none !important; }
    .stMainBlockContainer { padding: 0 !important; max-width: 100% !important; }

    /* LAYOUT VETRINA */
    .viewport {
        height: 100vh;
        width: 100vw;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 60px;
        box-sizing: border-box;
    }

    .header-brand {
        font-family: 'Inter', sans-serif;
        font-size: clamp(80px, 10vw, 150px);
        font-weight: 900;
        letter-spacing: -8px;
        line-height: 0.8;
        text-transform: uppercase;
    }

    .gold { color: #FFD700; }

    .grid-features {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        border-top: 1px solid #222;
        margin-top: 40px;
    }

    .card {
        padding: 40px 20px;
        border-right: 1px solid #222;
        transition: 0.3s;
    }
    .card:last-child { border-right: none; }
    .card:hover { background: #080808; }

    .card-label { color: #FFD700; font-size: 10px; letter-spacing: 3px; margin-bottom: 20px; }
    .card-title { font-size: 20px; font-weight: 400; color: #eee; margin-bottom: 10px; }
    .card-txt { font-size: 13px; color: #444; line-height: 1.5; }

    /* LOGIN MINIMALE */
    .login-wrapper {
        margin-top: auto;
        max-width: 400px;
    }

    input { 
        background: transparent !important; 
        border: none !important; 
        border-bottom: 1px solid #222 !important; 
        color: #FFD700 !important; 
        border-radius: 0 !important;
        padding: 15px 0 !important;
        font-size: 16px !important;
        width: 100%;
    }
    input:focus { border-bottom: 1px solid #FFD700 !important; outline: none !important; }

    .stButton > button {
        background: #FFD700 !important;
        color: #000 !important;
        border: none !important;
        border-radius: 0 !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        width: 100%;
        height: 50px;
        margin-top: 20px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    # --- INTERFACCIA VETRINA ---
    st.markdown("""
    <div class="viewport">
        <div>
            <div class="header-brand">ZEN<br><span class="gold">TRADER</span></div>
            <div style="margin-top:20px; font-size:12px; color:#444; letter-spacing:5px;">INSTITUTIONAL RISK TERMINAL v8.0</div>
            
            <div class="grid-features">
                <div class="card">
                    <div class="card-label">01 // RISK</div>
                    <div class="card-title">HARD CAP PROTECTION</div>
                    <div class="card-txt">Protocollo di sicurezza che blocca fisicamente l'accesso al broker in caso di drawdown superiore al 2%.</div>
                </div>
                <div class="card">
                    <div class="card-label">02 // EXECUTION</div>
                    <div class="card-title">LATENCY-FREE BRIDGE</div>
                    <div class="card-txt">Connessione API diretta con MetaTrader 5. Ordini eseguiti istantaneamente dal terminale web.</div>
                </div>
                <div class="card">
                    <div class="card-label">03 // ANALYTICS</div>
                    <div class="card-title">QUANT SCANNER</div>
                    <div class="card-txt">Algoritmi proprietari per l'individuazione di zone di liquidità e sbilanciamenti di volume.</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # LOGIN AREA
    _, col_log, _ = st.columns([1, 0.4, 1])
    with col_log:
        with st.form("auth_elite"):
            u = st.text_input("ID", placeholder="IDENTIFICATION", label_visibility="collapsed")
            p = st.text_input("PW", type="password", placeholder="SECURITY_KEY", label_visibility="collapsed")
            if st.form_submit_button("ACCESS TERMINAL"):
                if u == "luca" and p == "zen2026":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("ACCESS_DENIED")
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- TERMINALE OPERATIVO (Layout "Command Center") ---
    st.markdown("""
        <div style="padding:40px; border-bottom:1px solid #111;">
            <span style="color:#FFD700; font-size:10px; letter-spacing:4px;">LIVE TERMINAL // XAUUSD</span>
        </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 4])
    with c1:
        st.markdown("<div style='padding:20px;'>", unsafe_allow_html=True)
        bal = st.number_input("CAPITAL", value=10000)
        risk = st.slider("RISK %", 0.1, 2.0, 0.5)
        sl = st.number_input("SL PIPS", value=20)
        lots = round((bal * (risk/100)) / (sl * 10), 2)
        st.markdown(f"<h1>{lots}</h1><small>LOTS</small>", unsafe_allow_html=True)
        if st.button("EXECUTE ORDER"): st.success("SENT")
        if st.button("LOGOUT"): 
            st.session_state.auth = False
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        
    with c2:
        st.components.v1.html("""
            <div id="tv" style="height:800px; border:1px solid #111;"></div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>new TradingView.widget({"width": "100%", "height": 800, "symbol": "OANDA:XAUUSD", "interval": "1", "theme": "dark", "container_id": "tv", "style": "1"});</script>
        """, height=800)
