import streamlit as st

# --- 1. CONFIGURAZIONE ---
st.set_page_config(page_title="ZenTrader Pro", layout="wide")

# --- 2. CSS "THE VAULT" (Apple-Style, No compromise) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@100;400&display=swap');

    /* Reset Streamlit */
    .stApp { background-color: #000 !important; font-family: 'JetBrains Mono', monospace; }
    header, footer, section[data-testid="stSidebar"], .stDeployButton { display: none !important; }
    .stMainBlockContainer { padding: 0 !important; max-width: 100% !important; }

    /* Landing Wrapper */
    .viewport {
        height: 100vh;
        width: 100vw;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: #000;
        padding: 40px;
        box-sizing: border-box;
    }

    /* Branding */
    .brand-title {
        font-family: 'Inter', sans-serif;
        font-size: 110px;
        font-weight: 900;
        letter-spacing: -9px;
        line-height: 0.8;
        margin-bottom: 5px;
        text-transform: uppercase;
    }
    .brand-title span { color: #FFD700; }
    .brand-sub { font-size: 11px; letter-spacing: 10px; color: #333; margin-bottom: 80px; }

    /* LA TUA GRIGLIA - FORZATA CSS */
    .grid-features {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        width: 100%;
        max-width: 1200px;
        border-top: 1px solid #111;
        border-bottom: 1px solid #111;
        background: #000;
    }

    .card {
        padding: 60px 40px;
        border-right: 1px solid #111;
        background: transparent;
        transition: 0.2s ease-in-out;
    }
    .card:last-child { border-right: none; }
    .card:hover { background: #050505; }

    .card-label { color: #FFD700; font-size: 10px; letter-spacing: 3px; margin-bottom: 25px; font-weight: 400; }
    .card-title { font-size: 18px; font-weight: 400; color: #fff; margin-bottom: 15px; letter-spacing: -1px; font-family: 'Inter', sans-serif; }
    .card-txt { font-size: 13px; color: #555; line-height: 1.6; font-weight: 100; }

    /* Form Login Clean */
    .stTextInput input {
        background: transparent !important;
        border: none !important;
        border-bottom: 1px solid #111 !important;
        color: #FFD700 !important;
        border-radius: 0 !important;
        text-align: center !important;
        font-size: 16px !important;
        padding: 10px 0 !important;
        margin-top: 40px;
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
        margin-top: 30px;
        letter-spacing: 2px;
    }
</style>
""", unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    # --- VETRINA ---
    st.markdown(f"""
    <div class="viewport">
        <div class="brand-title">ZEN<span>TRADER</span></div>
        <div class="brand-sub">QUANTUM INTERFACE 2026</div>
        
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

    # Login Field
    _, col, _ = st.columns([1, 0.4, 1])
    with col:
        with st.form("gate"):
            u = st.text_input("ID", placeholder="IDENTIFICATION", label_visibility="collapsed")
            p = st.text_input("PW", type="password", placeholder="PASSWORD", label_visibility="collapsed")
            if st.form_submit_button("SBLOCCA TERMINALE"):
                if u == "luca" and p == "zen2026":
                    st.session_state.auth = True
                    st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- TERMINALE (Widest Possible) ---
    st.markdown("<div style='padding:20px; border-bottom:1px solid #111; display:flex; justify-content:space-between;'>", unsafe_allow_html=True)
    st.markdown("<span style='color:#FFD700; font-size:10px; letter-spacing:5px;'>TERMINAL // XAUUSD</span>", unsafe_allow_html=True)
    if st.button("EXIT"):
        st.session_state.auth = False
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    c1, c2 = st.columns([1, 4])
    with c1:
        st.markdown("<div style='padding:20px;'>", unsafe_allow_html=True)
        bal = st.number_input("Equity", value=10000)
        risk = st.slider("Risk %", 0.1, 2.0, 0.5)
        sl = st.number_input("SL Pips", value=20)
        lotti = round((bal * (risk/100)) / (sl * 10), 2)
        st.markdown(f"<div style='border:1px solid #111; padding:20px; text-align:center; margin-top:20px;'><h1 style='color:#FFD700;'>{lotti}</h1><small>LOTTI</small></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.components.v1.html("""
            <div style="height:750px; border-left:1px solid #111;">
                <div id="tv"></div>
            </div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>new TradingView.widget({"width": "100%", "height": 750, "symbol": "OANDA:XAUUSD", "interval": "1", "theme": "dark", "container_id": "tv"});</script>
        """, height=750)
