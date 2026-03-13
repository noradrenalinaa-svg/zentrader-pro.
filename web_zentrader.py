import streamlit as st

# --- 1. SETUP RADICALE ---
st.set_page_config(page_title="ZenTrader Pro", layout="wide")

# --- 2. IL "MOTORE" DI DESIGN (CSS BLINDATO) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@100;400&family=Inter:wght@900&display=swap');

    /* Reset Totale */
    .stApp { background-color: #000 !important; font-family: 'JetBrains Mono', monospace !important; }
    header, footer, section[data-testid="stSidebar"], .stDeployButton { display: none !important; }
    .stMainBlockContainer { padding: 0 !important; max-width: 100% !important; }

    /* Container Principale */
    .viewport {
        height: 100vh;
        width: 100vw;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: #000;
        padding: 40px;
    }

    /* La tua Griglia - Versione Razor Sharp */
    .grid-features {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        width: 100%;
        max-width: 1100px;
        border-top: 1px solid #111;
        border-bottom: 1px solid #111;
        margin-bottom: 60px;
    }

    .card {
        padding: 60px 40px;
        border-right: 1px solid #111;
        transition: 0.3s ease;
    }
    .card:last-child { border-right: none; }
    .card:hover { background: #050505; }

    .card-label { color: #FFD700; font-size: 10px; letter-spacing: 4px; margin-bottom: 30px; }
    .card-title { font-family: 'Inter', sans-serif; font-size: 18px; font-weight: 900; color: #fff; margin-bottom: 15px; letter-spacing: -1px; }
    .card-txt { font-size: 13px; color: #444; line-height: 1.7; font-weight: 100; }

    /* OVERRIDE TOTALE DEI WIDGET STREAMLIT */
    /* Elimina i box grigi intorno agli input */
    div[data-baseweb="input"] {
        background-color: transparent !important;
        border: none !important;
    }
    
    input {
        background-color: transparent !important;
        border: none !important;
        border-bottom: 1px solid #222 !important;
        color: #FFD700 !important;
        border-radius: 0 !important;
        text-align: center !important;
        font-size: 14px !important;
        padding: 10px 0 !important;
        font-family: 'JetBrains Mono', monospace !important;
    }

    input:focus {
        border-bottom: 1px solid #FFD700 !important;
        box-shadow: none !important;
    }

    /* Bottone stile Apple Dark */
    .stButton > button {
        background-color: transparent !important;
        color: #fff !important;
        border: 1px solid #222 !important;
        border-radius: 0px !important;
        width: 100%;
        height: 45px;
        font-size: 12px !important;
        letter-spacing: 2px !important;
        text-transform: uppercase;
        transition: 0.3s;
    }

    .stButton > button:hover {
        border-color: #FFD700 !important;
        color: #FFD700 !important;
    }

    /* Nasconde i messaggi di errore brutti */
    .stAlert { background-color: transparent !important; color: #ff4b4b !important; border: none !important; }
</style>
""", unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown('<div class="viewport">', unsafe_allow_html=True)
    
    # LA TUA GRIGLIA PULITA
    st.markdown("""
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

    # LOGIN AREA (SENZA FORM GRIGIO)
    _, col_center, _ = st.columns([1, 0.3, 1])
    with col_center:
        u = st.text_input("USER", placeholder="USER_ID", label_visibility="collapsed")
        p = st.text_input("PASS", type="password", placeholder="ACCESS_KEY", label_visibility="collapsed")
        if st.button("OPEN TERMINAL"):
            if u == "luca" and p == "zen2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.toast("Access Denied", icon="🚫")
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown("<h2 style='padding:40px; color:#FFD700;'>TERMINAL ACTIVE</h2>", unsafe_allow_html=True)
    if st.button("LOGOUT"):
        st.session_state.auth = False
        st.rerun()
