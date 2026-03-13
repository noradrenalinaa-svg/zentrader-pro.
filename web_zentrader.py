import streamlit as st

# --- 1. SETUP ---
st.set_page_config(page_title="ZenTrader Pro", layout="wide")

# --- 2. CSS RADICALE (Elimina l'estetica Streamlit) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@100;400;800&display=swap');

    /* Reset totale dell'app */
    .stApp { background-color: #000 !important; color: #fff; font-family: 'JetBrains Mono', monospace; }
    header, footer, section[data-testid="stSidebar"], .stDeployButton { display: none !important; }
    .stMainBlockContainer { padding: 0 !important; max-width: 100% !important; }

    /* LAYOUT DELLA VETRINA */
    .main-viewport {
        height: 100vh;
        width: 100vw;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: #000;
        padding: 40px;
    }

    .brand-header {
        text-align: center;
        margin-bottom: 80px;
    }

    .brand-header h1 {
        font-size: clamp(60px, 8vw, 120px);
        font-weight: 800;
        letter-spacing: -6px;
        line-height: 0.8;
        margin: 0;
        text-transform: uppercase;
    }

    .brand-header span { color: #FFD700; }

    /* GRID FEATURES CUSTOM - PIÙ LARGA E PULITA */
    .grid-features {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        width: 100%;
        max-width: 1400px;
        border: 1px solid #111;
        background: #000;
    }

    .card {
        padding: 60px 40px;
        border-right: 1px solid #111;
        transition: all 0.4s ease;
    }
    
    .card:last-child { border-right: none; }
    
    .card:hover { background: #050505; border-bottom: 2px solid #FFD700; }

    .card-label { 
        color: #333; 
        font-size: 11px; 
        letter-spacing: 4px; 
        margin-bottom: 30px; 
        font-weight: 400;
    }

    .card-title { 
        font-size: 22px; 
        font-weight: 400; 
        color: #fff; 
        margin-bottom: 15px; 
        letter-spacing: -1px;
    }

    .card-txt { 
        font-size: 14px; 
        color: #555; 
        line-height: 1.7; 
        font-weight: 100;
    }

    /* LOGIN MINIMALE IN FONDO */
    .login-box {
        margin-top: 60px;
        width: 100%;
        max-width: 350px;
    }

    /* Override input e bottoni per eliminare lo stile "giocattolo" */
    input {
        background: transparent !important;
        border: none !important;
        border-bottom: 1px solid #222 !important;
        color: #FFD700 !important;
        border-radius: 0 !important;
        padding: 15px 0 !important;
        text-align: center !important;
    }
    
    .stButton > button {
        background: #FFD700 !important;
        color: #000 !important;
        border-radius: 0 !important;
        font-weight: 800 !important;
        letter-spacing: 2px;
        border: none !important;
        height: 50px;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DI STATO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    # --- VETRINA ---
    st.markdown("""
    <div class="main-viewport">
        <div class="brand-header">
            <h1>ZEN<span>TRADER</span></h1>
            <p style="letter-spacing: 8px; color: #222; font-size: 12px; margin-top: 10px;">QUANTUM RISK ARCHITECTURE</p>
        </div>
        
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
    """, unsafe_allow_html=True)

    # LOGIN FORM
    _, col_center, _ = st.columns([1, 0.4, 1])
    with col_center:
        with st.form("gate"):
            u = st.text_input("ID", placeholder="IDENTIFICATION", label_visibility="collapsed")
            p = st.text_input("PW", type="password", placeholder="PASSWORD", label_visibility="collapsed")
            if st.form_submit_button("SBLOCCA TERMINALE"):
                if u == "luca" and p == "zen2026":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("ACCESS_DENIED")
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- TERMINALE (Dopo il Login) ---
    st.markdown("<div style='padding:40px;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='letter-spacing:-1px;'>TERMINALE <span style='color:#FFD700;'>LIVE</span></h3>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 4])
    with c1:
        st.markdown("---")
        bal = st.number_input("Equity", value=10000)
        risk = st.slider("Risk %", 0.1, 2.0, 0.5)
        sl = st.number_input("SL Pips", value=20)
        lotti = round((bal * (risk/100)) / (sl * 10), 2)
        st.markdown(f"<div style='border:1px solid #222; padding:20px; text-align:center;'><h1>{lotti}</h1><small>LOTTI</small></div>", unsafe_allow_html=True)
        if st.button("LOGOUT"):
            st.session_state.auth = False
            st.rerun()
    with c2:
        st.components.v1.html("""
            <div style="height:700px; border:1px solid #111;">
                <div id="tv"></div>
            </div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>new TradingView.widget({"width": "100%", "height": 700, "symbol": "OANDA:XAUUSD", "interval": "1", "theme": "dark", "container_id": "tv"});</script>
        """, height=700)
    st.markdown("</div>", unsafe_allow_html=True)
