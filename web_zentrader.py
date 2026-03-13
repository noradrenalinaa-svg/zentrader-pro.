import streamlit as st

# --- 1. CONFIGURAZIONE E RESET TOTALE ---
st.set_page_config(page_title="ZenTrader AI Pro", layout="wide")

st.markdown("""
<style>
    /* RESET DRASTICO */
    .stApp { background-color: #000; color: #fff; }
    header, footer, section[data-testid="stSidebar"], .stDeployButton { display: none !important; }
    .stMainBlockContainer { padding: 0 !important; max-width: 100% !important; }

    /* LAYOUT VETRINA */
    .hero-section {
        width: 100%;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 40px;
        background: radial-gradient(circle at 50% 50%, #111 0%, #000 100%);
    }

    .brand-name { font-size: 80px; font-weight: 900; letter-spacing: -4px; margin: 0; }
    .tagline { color: #ffd700; letter-spacing: 8px; font-size: 12px; text-transform: uppercase; margin-bottom: 80px; }

    /* GRID DELLE FEATURES (PULITA) */
    .features-container {
        display: flex;
        gap: 20px;
        max-width: 1100px;
        width: 100%;
        margin-bottom: 80px;
    }

    .f-card {
        flex: 1;
        background: #080808;
        border: 1px solid #1a1a1a;
        padding: 40px 20px;
        border-radius: 12px;
        text-align: center;
        transition: 0.3s;
    }
    .f-card:hover { border-color: #ffd700; background: #0c0c0c; }
    .f-card h3 { font-size: 18px; font-weight: 700; margin-bottom: 10px; color: #fff; }
    .f-card p { font-size: 13px; color: #555; line-height: 1.5; margin: 0; }

    /* LOGIN BOX (CENTRATA E MINIMAL) */
    .login-box {
        width: 100%;
        max-width: 360px;
        padding: 40px;
        background: #050505;
        border: 1px solid #222;
        border-radius: 12px;
    }

    /* FIX INPUT STREAMLIT */
    input { 
        background: #000 !important; 
        border: 1px solid #333 !important; 
        color: #ffd700 !important; 
        border-radius: 4px !important;
        padding: 10px !important;
        font-size: 14px !important;
    }
    
    div.stButton > button {
        background: #fff !important;
        color: #000 !important;
        font-weight: 900 !important;
        border-radius: 4px !important;
        border: none !important;
        height: 45px;
        letter-spacing: 1px;
    }
</style>
""", unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    # --- VETRINA MINIMALISTA ---
    st.markdown("""
    <div class="hero-section">
        <h1 class="brand-name">ZenTrader</h1>
        <p class="tagline">The Institutional Risk Bridge</p>
        
        <div class="features-container">
            <div class="f-card">
                <h3>RISK PROTECT</h3>
                <p>Hardware-level discipline. 2% daily drawdown hard-cap.</p>
            </div>
            <div class="f-card">
                <h3>CLOUD BRIDGE</h3>
                <p>Direct MT5 execution. Zero latency. One click.</p>
            </div>
            <div class="f-card">
                <h3>AI ANALYSIS</h3>
                <p>Proprietary XAUUSD trend & liquidity algorithms.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # LOGIN
    _, col_login, _ = st.columns([1, 0.6, 1])
    with col_login:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        with st.form("auth"):
            st.markdown("<p style='text-align:center; color:#333; font-size:10px; margin-bottom:20px; letter-spacing:2px;'>SECURE ACCESS</p>", unsafe_allow_html=True)
            u = st.text_input("User", placeholder="Username", label_visibility="collapsed")
            p = st.text_input("Pass", type="password", placeholder="Password", label_visibility="collapsed")
            if st.form_submit_button("LOGIN"):
                if u == "luca" and p == "zen2026":
                    st.session_state['auth'] = True
                    st.rerun()
                else: st.error("Invalid")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- TERMINALE OPERATIVO ---
    st.markdown("<div style='padding:20px;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='letter-spacing: -1px;'>TERMINAL <span style='color:#ffd700;'>LIVE</span></h3>", unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1, 4])
    with col_l:
        st.markdown("---")
        bal = st.number_input("Capital", value=10000)
        risk = st.slider("Risk %", 0.1, 2.0, 0.5)
        sl = st.number_input("SL (Pips)", value=20)
        lotti = round((bal * (risk/100)) / (sl * 10), 2)
        st.markdown(f"<div style='background:#111; padding:15px; border:1px solid #222; border-radius:8px;'><small style='color:#444;'>LOTS</small><h2 style='color:#ffd700; margin:0;'>{lotti}</h2></div>", unsafe_allow_html=True)
        if st.button("LOGOUT"):
            st.session_state.auth = False
            st.rerun()
            
    with col_r:
        st.components.v1.html("""
            <div style="height:700px; border-radius:12px; overflow:hidden; border:1px solid #1a1a1a;">
                <div id="tv"></div>
            </div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>new TradingView.widget({"width": "100%", "height": 700, "symbol": "OANDA:XAUUSD", "interval": "15", "theme": "dark", "container_id": "tv"});</script>
        """, height=700)
    st.markdown("</div>", unsafe_allow_html=True)
