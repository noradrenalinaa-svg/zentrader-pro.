import streamlit as st

# --- 1. CONFIGURAZIONE ---
st.set_page_config(page_title="ZenTrader AI Pro", layout="wide")

# --- 2. CSS "CINEMATIC" (Design Ultra-Premium) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&display=swap');
    
    /* Sfondo Nero Assoluto */
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Inter', sans-serif; }
    
    /* Rimuove ogni traccia di Streamlit standard */
    header, footer, section[data-testid="stSidebar"] { display: none !important; }
    .stMainBlockContainer { padding: 0 !important; max-width: 100% !important; }

    /* Container Vetrina */
    .hero-container {
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: radial-gradient(circle at center, #111 0%, #000 70%);
    }

    .hero-title { font-size: 80px; font-weight: 900; letter-spacing: -2px; margin-bottom: 10px; }
    .hero-sub { font-size: 24px; color: #ffd700; font-weight: 300; margin-bottom: 60px; letter-spacing: 4px; text-transform: uppercase; }

    /* Card di Design */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 40px;
        text-align: center;
        transition: 0.4s;
    }
    .glass-card:hover { border-color: #ffd700; background: rgba(255, 215, 0, 0.02); transform: translateY(-10px); }
    
    .card-icon { font-size: 50px; margin-bottom: 20px; }
    .card-title { font-size: 22px; font-weight: 700; margin-bottom: 15px; }
    .card-desc { font-size: 15px; color: #888; line-height: 1.6; }

    /* Login Box Ultra-Clean */
    .login-wrapper {
        background: #0a0a0a;
        border: 1px solid #1a1a1a;
        border-radius: 20px;
        padding: 40px;
        width: 100%;
        max-width: 450px;
        margin-top: 50px;
    }

    /* Override Input Streamlit */
    input { 
        background-color: #111 !important; 
        border: 1px solid #222 !important; 
        color: #fff !important; 
        border-radius: 12px !important;
        padding: 15px !important;
    }
    
    .stButton > button {
        background: #ffffff !important;
        color: #000 !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        height: 55px;
        border-radius: 12px !important;
        border: none !important;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    # --- LANDING PAGE CINEMATICA ---
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title">ZenTrader AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub">Infrastruttura di Trading Elite</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1], gap="large")
    with col1:
        st.markdown('<div class="glass-card"><div class="card-icon">📊</div><div class="card-title">Analisi Pro</div><div class="card-desc">Integrazione TradingView nativa con algoritmi di scansione trend in tempo reale.</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="glass-card" style="border-color: #ffd70044;"><div class="card-icon">🛡️</div><div class="card-title" style="color:#ffd700">Rischio Zero</div><div class="card-desc">Protocollo di protezione drawdown al 2%. Il sistema blocca l\'operatività se sei in pericolo.</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="glass-card"><div class="card-icon">⚡</div><div class="card-title">Esecuzione</div><div class="card-desc">Connessione Bridge MT5 ultra-rapida. Esegui ordini calcolati in millisecondi.</div></div>', unsafe_allow_html=True)

    # Box di Login
    _, login_col, _ = st.columns([1, 1, 1])
    with login_col:
        st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)
        with st.form("login_pro"):
            st.markdown("<p style='text-align:center; color:#555; letter-spacing:2px; font-weight:700;'>MEMBERS LOGIN</p>", unsafe_allow_html=True)
            u = st.text_input("User", placeholder="ID Utente", label_visibility="collapsed")
            p = st.text_input("Pass", type="password", placeholder="Password", label_visibility="collapsed")
            if st.form_submit_button("SBLOCCA ACCESSO"):
                if u == "luca" and p == "zen2026":
                    st.session_state['auth'] = True
                    st.rerun()
                else: st.error("Accesso Negato")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- TERMINALE OPERATIVO (Layout Wide e Pulito) ---
    st.markdown("<div style='padding: 30px;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-weight:900; letter-spacing:-1px;'>TERMINALE OPERATIVO <span style='color:#ffd700;'>• LIVE</span></h2>", unsafe_allow_html=True)
    
    c_tools, c_main = st.columns([1, 3])
    
    with c_tools:
        st.markdown("### 🧮 Risk Management")
        bal = st.number_input("Equità ($)", value=10000)
        risk = st.slider("Rischio %", 0.1, 2.0, 0.5)
        sl = st.number_input("Stop Loss (Pips)", value=20)
        lotti = round((bal * (risk/100)) / (sl * 10), 2)
        st.markdown(f"<div style='background:#111; padding:20px; border-radius:15px; border:1px solid #222; margin-top:20px;'><p style='color:#888; font-size:12px;'>LOTTAGGIO CALCOLATO</p><h1 style='color:#ffd700; margin:0;'>{lotti}</h1></div>", unsafe_allow_html=True)
        
        if st.button("LOGOUT"):
            st.session_state.auth = False
            st.rerun()

    with c_main:
        st.components.v1.html("""
            <div style="height:700px; border-radius:24px; overflow:hidden; border:1px solid #222;">
                <div id="tv_chart"></div>
            </div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>new TradingView.widget({"width": "100%", "height": 700, "symbol": "OANDA:XAUUSD", "interval": "15", "theme": "dark", "container_id": "tv_chart"});</script>
        """, height=700)
    st.markdown("</div>", unsafe_allow_html=True)
