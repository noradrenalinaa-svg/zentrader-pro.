import streamlit as st

# --- 1. CONFIGURAZIONE E RESET TOTALE ---
st.set_page_config(page_title="ZenTrader AI Pro", layout="wide")

st.markdown("""
<style>
    /* RESET ARCHITETTURALE */
    .stApp { background-color: #000; color: #fff; }
    header, footer, section[data-testid="stSidebar"], .stDeployButton { display: none !important; }
    .stMainBlockContainer { padding: 0 !important; max-width: 100% !important; }
    [data-testid="stVerticalBlock"] { gap: 0 !important; }

    /* DESIGN VETRINA PRO */
    .landing-page {
        width: 100%;
        min-height: 100vh;
        background: #000;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 80px 5%;
    }
    
    .title { font-family: 'Inter', sans-serif; font-size: 70px; font-weight: 900; letter-spacing: -4px; margin-bottom: 0; }
    .subtitle { color: #ffd700; text-transform: uppercase; letter-spacing: 6px; font-size: 14px; margin-bottom: 80px; }

    /* FEATURE GRID */
    .grid {
        display: flex;
        justify-content: center;
        gap: 30px;
        width: 100%;
        max-width: 1200px;
        margin-bottom: 80px;
    }
    
    .feature-card {
        background: #0a0a0a;
        border: 1px solid #1a1a1a;
        padding: 50px 30px;
        border-radius: 24px;
        text-align: center;
        flex: 1;
        transition: 0.4s;
    }
    .feature-card:hover { border-color: #ffd700; transform: translateY(-10px); }
    .feature-card h3 { font-size: 24px; margin-bottom: 15px; }
    .feature-card p { color: #666; font-size: 15px; line-height: 1.6; }

    /* LOGIN BOX STYLE */
    .login-section {
        width: 100%;
        max-width: 400px;
        background: #0d0d0d;
        border: 1px solid #222;
        border-radius: 20px;
        padding: 40px;
    }
    
    /* FIX PER GLI INPUT DI STREAMLIT */
    input { 
        background: #000 !important; 
        border: 1px solid #333 !important; 
        color: #ffd700 !important; 
        border-radius: 10px !important;
        padding: 12px !important;
    }
    
    div.stButton > button {
        background: #ffd700 !important;
        color: #000 !important;
        font-weight: 900 !important;
        height: 55px;
        border-radius: 10px !important;
        border: none !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state['auth'] = False

# --- LOGICA DI NAVIGAZIONE ---
if not st.session_state['auth']:
    # PAGINA DI VENDITA
    st.markdown(f"""
    <div class="landing-page">
        <div class="title">ZenTrader AI</div>
        <div class="subtitle">Institutional Risk Terminal</div>
        <div class="grid">
            <div class="feature-card">
                <div style="font-size:40px; margin-bottom:20px;">🛡️</div>
                <h3>Rischio</h3>
                <p>Protezione automatica del capitale con blocco drawdown al 2%.</p>
            </div>
            <div class="feature-card" style="border-color: #ffd70044;">
                <div style="font-size:40px; margin-bottom:20px;">⚡</div>
                <h3>Esecuzione</h3>
                <p>Ponte diretto verso MT5 per ordini istantanei calcolati al millimetro.</p>
            </div>
            <div class="feature-card">
                <div style="font-size:40px; margin-bottom:20px;">📊</div>
                <h3>Analisi</h3>
                <p>Grafici TradingView integrati con scanner trend avanzato.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # LOGIN BOX (Usando widget Streamlit ma dentro la nostra struttura CSS)
    _, login_col, _ = st.columns([1, 0.8, 1])
    with login_col:
        st.markdown('<div class="login-section">', unsafe_allow_html=True)
        with st.form("auth_pro"):
            st.markdown("<p style='text-align:center; color:#555; margin-bottom:20px;'>MEMBERS AREA</p>", unsafe_allow_html=True)
            u = st.text_input("User", placeholder="Username", label_visibility="collapsed")
            p = st.text_input("Pass", type="password", placeholder="Password", label_visibility="collapsed")
            if st.form_submit_button("ACCEDI AL TERMINALE"):
                if u == "luca" and p == "zen2026":
                    st.session_state['auth'] = True
                    st.rerun()
                else: st.error("Accesso Negato")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- TERMINALE OPERATIVO (Layout Mac Pro) ---
    st.markdown("<div style='padding: 30px;'>", unsafe_allow_html=True)
    st.markdown("<h2>ZEN.TERMINAL <span style='color:#ffd700;'>• LIVE</span></h2>", unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1, 3.5])
    with col_l:
        st.markdown("### 🧮 Config")
        bal = st.number_input("Equity", value=10000)
        risk = st.slider("Risk %", 0.1, 2.0, 0.5)
        sl = st.number_input("SL Pips", value=20)
        lotti = round((bal * (risk/100)) / (sl * 10), 2)
        st.markdown(f"<div style='background:#111; padding:20px; border-radius:15px; border:1px solid #222; margin-top:20px;'><p style='color:#888; font-size:12px;'>SIZE CALCOLATA</p><h1 style='color:#ffd700; margin:0;'>{lotti}</h1></div>", unsafe_allow_html=True)
        
        if st.button("LOGOUT"):
            st.session_state.auth = False
            st.rerun()
            
    with col_r:
        st.components.v1.html("""
            <div style="height:750px; border-radius:24px; overflow:hidden; border:1px solid #222;">
                <div id="tv_chart"></div>
            </div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>new TradingView.widget({"width": "100%", "height": 750, "symbol": "OANDA:XAUUSD", "interval": "15", "theme": "dark", "container_id": "tv_chart"});</script>
        """, height=750)
    st.markdown("</div>", unsafe_allow_html=True)
