import streamlit as st

# --- 1. CONFIGURAZIONE ---
st.set_page_config(page_title="ZenTrader AI Pro", layout="wide")

# --- 2. CSS "HARD-RESET" (Elimina lo stile Streamlit e impone il Trading Style) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&display=swap');
    
    /* Reset Totale */
    .stApp { background-color: #000; color: #fff; font-family: 'Inter', sans-serif; }
    header, footer, section[data-testid="stSidebar"] { display: none !important; }
    .stMainBlockContainer { padding: 0 !important; max-width: 100% !important; }

    /* Vetrina a tutto schermo */
    .landing-wrapper {
        width: 100%;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        background: radial-gradient(circle at top, #111 0%, #000 100%);
        padding: 60px 20px;
    }

    .main-logo { font-size: 64px; font-weight: 900; letter-spacing: -3px; margin-bottom: 5px; }
    .main-sub { color: #ffd700; letter-spacing: 5px; text-transform: uppercase; font-size: 14px; margin-bottom: 60px; }

    /* Griglia Feature senza bug di allineamento */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        width: 100%;
        max-width: 1200px;
        margin-bottom: 60px;
    }

    .card {
        background: #0a0a0a;
        border: 1px solid #1a1a1a;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        transition: 0.3s;
    }
    .card:hover { border-color: #ffd700; background: #111; }
    .card h3 { color: #fff; margin-top: 20px; font-size: 22px; }
    .card p { color: #666; font-size: 15px; margin-top: 10px; line-height: 1.6; }

    /* Form di Login compatto e centrato */
    .login-container {
        background: #0d0d0d;
        border: 1px solid #222;
        padding: 40px;
        border-radius: 20px;
        width: 100%;
        max-width: 400px;
    }

    /* Stile Input e Bottoni */
    input { 
        background: #000 !important; 
        border: 1px solid #333 !important; 
        color: #ffd700 !important; 
        padding: 12px !important;
        border-radius: 8px !important;
    }
    
    .stButton > button {
        background: #ffd700 !important;
        color: #000 !important;
        font-weight: 900 !important;
        height: 50px;
        border-radius: 8px !important;
        border: none !important;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    # --- NUOVA VETRINA PULITA ---
    st.markdown('<div class="landing-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="main-logo">ZenTrader AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-sub">The Institutional Terminal</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-grid">
        <div class="card">
            <div style="font-size:40px;">🛡️</div>
            <h3>Rischio Blindato</h3>
            <p>Calcolo lotti istantaneo con blocco drawdown al 2%. La tua protezione definitiva.</p>
        </div>
        <div class="card">
            <div style="font-size:40px;">⚡</div>
            <h3>Esecuzione Direct</h3>
            <p>Connessione bridge a MetaTrader 5. Ordini eseguiti in millisecondi senza stress.</p>
        </div>
        <div class="card">
            <div style="font-size:40px;">📊</div>
            <h3>Analisi Elite</h3>
            <p>Grafici TradingView integrati con scanner di liquidità e trend AI.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Login
    _, login_col, _ = st.columns([1, 1, 1])
    with login_col:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        with st.form("auth_form"):
            st.markdown("<p style='text-align:center; font-size:12px; color:#444; letter-spacing:2px;'>PRIVATE ACCESS</p>", unsafe_allow_html=True)
            u = st.text_input("User", placeholder="ID", label_visibility="collapsed")
            p = st.text_input("Pass", type="password", placeholder="Password", label_visibility="collapsed")
            if st.form_submit_button("SBLOCCA TERMINALE"):
                if u == "luca" and p == "zen2026":
                    st.session_state['auth'] = True
                    st.rerun()
                else: st.error("Errore")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- TERMINALE (Solo se loggati) ---
    st.markdown("<div style='padding:20px;'>", unsafe_allow_html=True)
    st.title("🛡️ ZenTerminal Live")
    
    col_l, col_r = st.columns([1, 3])
    with col_l:
        st.number_input("Equità", value=10000)
        st.slider("Rischio %", 0.1, 2.0, 0.5)
        st.button("Invia Ordine")
        if st.button("Esci"):
            st.session_state.auth = False
            st.rerun()
    with col_r:
        st.components.v1.html("""
            <div style="height:700px; border-radius:15px; overflow:hidden; border:1px solid #222;">
                <div id="tv"></div>
            </div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>new TradingView.widget({"width": "100%", "height": 700, "symbol": "OANDA:XAUUSD", "interval": "15", "theme": "dark", "container_id": "tv"});</script>
        """, height=700)
    st.markdown("</div>", unsafe_allow_html=True)
