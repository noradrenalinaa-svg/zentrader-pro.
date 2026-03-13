import streamlit as st

# --- 1. CONFIGURAZIONE RADICALE ---
st.set_page_config(page_title="ZenTrader Pro", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@100;400;800&display=swap');

    /* KILL STREAMLIT UI */
    .stApp { background-color: #000 !important; color: #fff; font-family: 'JetBrains Mono', monospace; }
    header, footer, section[data-testid="stSidebar"], .stDeployButton { display: none !important; }
    .stMainBlockContainer { padding: 0 !important; max-width: 100% !important; }

    /* VIEWPORT */
    .container {
        height: 100vh;
        width: 100vw;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: #000;
        padding: 60px;
    }

    /* TITOLO BRUTALISTA */
    .brand { font-size: 120px; font-weight: 800; letter-spacing: -10px; margin-bottom: 5px; text-transform: uppercase; line-height: 0.8; }
    .brand span { color: #FFD700; }

    /* LA TUA GRIGLIA - STILIZZATA PRO */
    .grid-features {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        width: 100%;
        max-width: 1200px;
        border: 1px solid #111;
        margin-top: 80px;
    }

    .card {
        padding: 50px 30px;
        border-right: 1px solid #111;
        transition: 0.3s ease;
    }
    .card:last-child { border-right: none; }
    .card:hover { background: #050505; border-bottom: 2px solid #FFD700; }

    .card-label { color: #333; font-size: 10px; letter-spacing: 5px; margin-bottom: 30px; }
    .card-title { font-size: 20px; font-weight: 400; color: #fff; margin-bottom: 15px; letter-spacing: -1px; }
    .card-txt { font-size: 13px; color: #444; line-height: 1.6; font-weight: 100; }

    /* INPUT LOGIN - ULTRA CLEAN */
    .stTextInput input {
        background: transparent !important;
        border: none !important;
        border-bottom: 1px solid #222 !important;
        color: #FFD700 !important;
        border-radius: 0 !important;
        text-align: center !important;
        font-size: 18px !important;
        transition: 0.3s;
    }
    .stTextInput input:focus { border-bottom: 1px solid #FFD700 !important; }

    .stButton > button {
        background: #FFD700 !important;
        color: #000 !important;
        border-radius: 0 !important;
        font-weight: 800 !important;
        border: none !important;
        height: 50px;
        width: 100%;
        margin-top: 40px;
        letter-spacing: 2px;
    }
</style>
""", unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    # --- INTERFACCIA VETRINA ---
    st.markdown("""
    <div class="container">
        <div class="brand">ZEN<span>TRADER</span></div>
        <p style="color:#222; letter-spacing:10px; font-size:11px;">QUANTUM RISK ARCHITECTURE</p>
        
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
    _, col_form, _ = st.columns([1, 0.5, 1])
    with col_form:
        with st.form("access_gate"):
            u = st.text_input("ID", placeholder="IDENTIFICATION", label_visibility="collapsed")
            p = st.text_input("PW", type="password", placeholder="PASSWORD", label_visibility="collapsed")
            if st.form_submit_button("SBLOCCA TERMINALE"):
                if u == "luca" and p == "zen2026":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("ACCESS_DENIED")
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- TERMINALE LIVE ---
    st.markdown("<div style='padding:40px; display:flex; justify-content:space-between; align-items:center;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='letter-spacing:-2px;'>TERMINAL <span style='color:#FFD700;'>LIVE</span></h2>", unsafe_allow_html=True)
    if st.button("LOGOUT"):
        st.session_state.auth = False
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    c1, c2 = st.columns([1, 4])
    with c1:
        st.markdown("<div style='padding:20px; border:1px solid #111;'>", unsafe_allow_html=True)
        bal = st.number_input("Equity", value=10000)
        risk = st.slider("Risk %", 0.1, 2.0, 0.5)
        sl = st.number_input("SL Pips", value=20)
        lotti = round((bal * (risk/100)) / (sl * 10), 2)
        st.markdown(f"<p style='color:#444; font-size:10px; margin-top:20px;'>LOTS</p><h1 style='color:#FFD700; margin:0;'>{lotti}</h1>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.components.v1.html("""
            <div style="height:750px; border:1px solid #111;">
                <div id="tv"></div>
            </div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>new TradingView.widget({"width": "100%", "height": 750, "symbol": "OANDA:XAUUSD", "interval": "1", "theme": "dark", "container_id": "tv"});</script>
        """, height=750)
