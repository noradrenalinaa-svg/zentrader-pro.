import streamlit as st

# --- 1. RESET ARCHITETTONICO (Elimina Streamlit visivamente) ---
st.set_page_config(page_title="ZenTrader Pro", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@100;400;800&display=swap');

    /* Sfondo Nero Totale e Font Tecnico */
    .stApp { 
        background-color: #000 !important; 
        color: #fff !important; 
        font-family: 'JetBrains Mono', monospace !important; 
    }
    
    /* Nasconde tutto il superfluo di Streamlit */
    header, footer, section[data-testid="stSidebar"], .stDeployButton { display: none !important; }
    .stMainBlockContainer { padding: 0 !important; max-width: 100% !important; }

    /* Centra tutto nel viewport del Mac */
    .main-container {
        height: 100vh;
        width: 100vw;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 40px;
        box-sizing: border-box;
    }

    /* Titolo Minimalista */
    .brand {
        font-size: clamp(50px, 7vw, 100px);
        font-weight: 800;
        letter-spacing: -6px;
        margin-bottom: 60px;
        text-transform: uppercase;
        color: #fff;
    }
    .brand span { color: #FFD700; }

    /* LA TUA GRIGLIA - STILIZZATA CHIRURGICAMENTE */
    .grid-features {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        width: 100%;
        max-width: 1100px;
        border: 1px solid #111; /* Linea quasi invisibile */
    }

    .card {
        padding: 50px 30px;
        border-right: 1px solid #111;
        transition: 0.3s;
    }
    .card:last-child { border-right: none; }
    .card:hover { background: #050505; }

    .card-label { 
        color: #FFD700; 
        font-size: 10px; 
        letter-spacing: 4px; 
        margin-bottom: 25px; 
        font-weight: 400;
    }

    .card-title { 
        font-size: 18px; 
        font-weight: 400; 
        color: #fff; 
        margin-bottom: 12px; 
        letter-spacing: -1px; 
    }

    .card-txt { 
        font-size: 13px; 
        color: #444; 
        line-height: 1.6; 
        font-weight: 100;
    }

    /* Input di Login - Scomparsa */
    .stTextInput input {
        background: transparent !important;
        border: none !important;
        border-bottom: 1px solid #222 !important;
        color: #FFD700 !important;
        border-radius: 0 !important;
        text-align: center !important;
        padding: 10px 0 !important;
        font-family: 'JetBrains Mono', monospace !important;
    }

    /* Bottone - Minimal White */
    .stButton > button {
        background: #fff !important;
        color: #000 !important;
        border-radius: 0 !important;
        font-weight: 800 !important;
        border: none !important;
        height: 45px;
        width: 100%;
        letter-spacing: 2px;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    # --- VETRINA ---
    st.markdown("""
    <div class="main-container">
        <div class="brand">ZEN<span>TRADER</span></div>
        
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

    # Area Login (Pulita)
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
    # --- TERMINALE OPERATIVO ---
    st.markdown("<div style='padding:40px;'>", unsafe_allow_html=True)
    st.markdown("<h3>BRIDGE.<span style='color:#FFD700;'>LIVE</span></h3>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 4])
    with c1:
        st.markdown("---")
        bal = st.number_input("Capital", value=10000)
        risk = st.slider("Risk %", 0.1, 2.0, 0.5)
        sl = st.number_input("SL Pips", value=20)
        lotti = round((bal * (risk/100)) / (sl * 10), 2)
        st.markdown(f"<div style='border:1px solid #111; padding:20px; text-align:center;'><h1>{lotti}</h1><small>LOTS</small></div>", unsafe_allow_html=True)
        if st.button("LOGOUT"):
            st.session_state.auth = False
            st.rerun()
    with c2:
        st.components.v1.html("""
            <div style="height:700px; border-left:1px solid #111;">
                <div id="tv"></div>
            </div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>new TradingView.widget({"width": "100%", "height": 700, "symbol": "OANDA:XAUUSD", "interval": "1", "theme": "dark", "container_id": "tv"});</script>
        """, height=700)
    st.markdown("</div>", unsafe_allow_html=True)
