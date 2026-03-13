import streamlit as st

# --- 1. SETUP MAC-STYLE ---
st.set_page_config(page_title="ZenTrader Pro", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@100;400&display=swap');

    /* RESET TOTALE E CANCELLAZIONE STILI STREAMLIT */
    .stApp { background-color: #000 !important; color: #fff; font-family: 'JetBrains Mono', monospace; }
    header, footer, section[data-testid="stSidebar"], .stDeployButton { display: none !important; }
    .stMainBlockContainer { padding: 0 !important; max-width: 100% !important; }

    /* LAYOUT CENTRALE */
    .main-wrapper {
        height: 100vh;
        width: 100vw;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: #000;
        padding: 40px;
    }

    /* BRANDING MINIMALISTA */
    .brand-title {
        font-family: 'Inter', sans-serif;
        font-size: 100px;
        font-weight: 900;
        letter-spacing: -8px;
        line-height: 0.8;
        margin-bottom: 5px;
        text-transform: uppercase;
    }
    .brand-title span { color: #FFD700; }
    .brand-sub { font-size: 10px; letter-spacing: 8px; color: #333; margin-bottom: 80px; }

    /* LA TUA GRIGLIA (STILE RAZOR-SHARP) */
    .grid-features {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        width: 100%;
        max-width: 1200px;
        border-top: 1px solid #111;
        border-bottom: 1px solid #111;
    }

    .card {
        padding: 60px 40px;
        border-right: 1px solid #111;
        background: transparent;
        transition: 0.2s;
    }
    .card:last-child { border-right: none; }
    .card:hover { background: #050505; }

    .card-label { color: #FFD700; font-size: 10px; letter-spacing: 3px; margin-bottom: 30px; font-weight: 400; }
    .card-title { font-size: 18px; font-weight: 400; color: #fff; margin-bottom: 12px; letter-spacing: -1px; }
    .card-txt { font-size: 13px; color: #444; line-height: 1.6; font-weight: 100; }

    /* LOGIN INTEGRATO */
    .stTextInput input {
        background: transparent !important;
        border: none !important;
        border-bottom: 1px solid #111 !important;
        color: #FFD700 !important;
        border-radius: 0 !important;
        text-align: center !important;
        font-size: 16px !important;
        padding: 15px 0 !important;
    }
    .stTextInput input:focus { border-bottom: 1px solid #FFD700 !important; box-shadow: none !important; }

    .stButton > button {
        background: #fff !important;
        color: #000 !important;
        border-radius: 0 !important;
        font-weight: 900 !important;
        border: none !important;
        height: 45px;
        width: 100%;
        margin-top: 40px;
        letter-spacing: 1px;
        transition: 0.2s;
    }
    .stButton > button:hover { background: #FFD700 !important; }
</style>
""", unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    # --- INTERFACCIA VETRINA ---
    st.markdown("""
    <div class="main-wrapper">
        <div class="brand-title">ZEN<span>TRADER</span></div>
        <div class="brand-sub">PRIVATE TERMINAL 2026</div>
        
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

    # LOGIN AREA (PULITA)
    _, col_log, _ = st.columns([1, 0.4, 1])
    with col_log:
        with st.form("gate"):
            u = st.text_input("ID", placeholder="IDENTIFICATION", label_visibility="collapsed")
            p = st.text_input("PW", type="password", placeholder="PASSWORD", label_visibility="collapsed")
            if st.form_submit_button("AUTH"):
                if u == "luca" and p == "zen2026":
                    st.session_state.auth = True
                    st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- TERMINALE (ESTETICA RAZOR) ---
    st.markdown("<div style='padding:40px; border-bottom:1px solid #111;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='letter-spacing:-2px; margin:0;'>BRIDGE.<span style='color:#FFD700;'>LIVE</span></h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    c1, c2 = st.columns([1, 4])
    with c1:
        st.markdown("<div style='padding:20px;'>", unsafe_allow_html=True)
        bal = st.number_input("CAPITAL", value=10000)
        risk = st.slider("RISK %", 0.1, 2.0, 0.5)
        sl = st.number_input("SL PIPS", value=20)
        lots = round((bal * (risk/100)) / (sl * 10), 2)
        st.markdown(f"<div style='border:1px solid #111; padding:30px; margin-top:20px; text-align:center;'><small style='color:#333;'>LOTS</small><h1 style='color:#FFD700;'>{lots}</h1></div>", unsafe_allow_html=True)
        if st.button("EXIT"): 
            st.session_state.auth = False
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.components.v1.html("""
            <div style="height:750px; border-left:1px solid #111;">
                <div id="tv"></div>
            </div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>new TradingView.widget({"width": "100%", "height": 750, "symbol": "OANDA:XAUUSD", "interval": "1", "theme": "dark", "container_id": "tv"});</script>
        """, height=750)
