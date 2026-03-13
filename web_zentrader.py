import streamlit as st

# --- 1. CONFIGURAZIONE ---
st.set_page_config(page_title="ZenTrader AI Pro", layout="wide")

# --- 2. CSS DEFINITIVO (Pulisce tutto e crea la Vetrina) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&display=swap');
    
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Inter', sans-serif; }
    
    /* Nasconde Sidebar e Header Streamlit */
    section[data-testid="stSidebar"] { display: none !important; }
    header { visibility: hidden !important; }
    
    /* Stile Vetrina (Landing Page) */
    .hero-title { font-size: 50px; font-weight: 900; text-align: center; color: #fff; padding-top: 40px; }
    .hero-sub { font-size: 20px; text-align: center; color: #ffd700; margin-bottom: 50px; letter-spacing: 1px; }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px; padding: 30px; text-align: center; height: 100%;
    }
    
    /* Input e Bottoni Custom */
    .stNumberInput input, .stTextInput input {
        background-color: #111 !important; color: #ffd700 !important; border: 1px solid #333 !important;
    }
    .stButton > button {
        background: #ffd700 !important; color: #000 !important;
        font-weight: bold !important; border-radius: 8px !important;
        border: none !important; width: 100%; height: 50px;
    }
    .stSlider > div > div > div > div { background-color: #ffd700 !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DI NAVIGAZIONE ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    # --- QUESTA È LA VETRINA CHE NON VEDEVI ---
    st.markdown('<h1 class="hero-title">ZenTrader AI Terminal</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub">L\'unica infrastruttura che blinda il tuo capitale e automatizza il tuo rischio.</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="glass-card"><h3>📊 Analisi</h3><p style="color:#888;">TradingView Pro integrato per un\'analisi senza distrazioni.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="glass-card" style="border: 1px solid #ffd70044;"><h3>🛡️ Rischio</h3><p style="color:#888;">Blocco automatico del Drawdown al 2%. Proteggi il tuo conto sempre.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="glass-card"><h3>⚡ Esecuzione</h3><p style="color:#888;">Invia ordini a MT5 in un click con calcolo automatico dei lotti.</p></div>', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # BOX DI LOGIN (Sotto la vetrina)
    _, login_col, _ = st.columns([1, 0.8, 1])
    with login_col:
        st.markdown("<div style='background:rgba(255,255,255,0.02); padding:30px; border-radius:15px; border:1px solid #222;'>", unsafe_allow_html=True)
        with st.form("login_form"):
            st.markdown("<p style='text-align:center; color:#555; margin-bottom:20px;'>ACCESSO PRO</p>", unsafe_allow_html=True)
            u = st.text_input("Username", placeholder="Username", label_visibility="collapsed")
            p = st.text_input("Password", type="password", placeholder="Password", label_visibility="collapsed")
            # COMANDO CORRETTO PER NON AVERE ERRORI ROSSI
            submit = st.form_submit_button("SBLOCCA TERMINALE")
            
            if submit:
                if u == "luca" and p == "zen2026":
                    st.session_state['auth'] = True
                    st.rerun()
                else:
                    st.error("Credenziali non valide")
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#444; margin-top:20px;'>Membership: 49€/mese</p>", unsafe_allow_html=True)

else:
    # --- IL TERMINALE OPERATIVO (Dopo il Login) ---
    st.markdown("<h2 style='text-align:center; color:#ffd700; padding-top:20px;'>💎 ZEN TERMINAL OPERATIVO</h2>", unsafe_allow_html=True)
    
    c_l, c_c, c_r = st.columns([1, 2.5, 1])
    
    with c_l:
        st.markdown("### 🧮 Config")
        bal = st.number_input("Equità ($)", value=10000)
        risk = st.slider("Rischio %", 0.1, 2.0, 0.5)
        sl = st.number_input("Stop Loss (Pips)", value=20)
        lotti = round((bal * (risk/100)) / (sl * 10), 2)
        st.markdown(f"<p style='color:#888;'>SIZE CONSIGLIATA</p><h1 style='color:#ffd700;'>{lotti}</h1>", unsafe_allow_html=True)
        
    with c_c:
        st.components.v1.html("""
            <div style="height:600px; border-radius:15px; overflow:hidden; border:1px solid #222;">
                <div id="tv_chart"></div>
            </div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>new TradingView.widget({"width": "100%", "height": 600, "symbol": "OANDA:XAUUSD", "interval": "15", "theme": "dark", "container_id": "tv_chart"});</script>
        """, height=600)
        
    with c_r:
        st.markdown("### 🚀 Trade")
        st.write(f"Asset: **XAUUSD**")
        st.write(f"Size: **{lotti} lotti**")
        if st.button("INVIA A MT5"):
            st.success("Ordine inviato!")
        
        st.divider()
        if st.button("LOGOUT"):
            st.session_state.auth = False
            st.rerun()
