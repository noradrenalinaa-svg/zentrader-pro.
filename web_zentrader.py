import streamlit as st

# --- 1. CONFIGURAZIONE ---
st.set_page_config(page_title="ZenTrader AI Pro", layout="wide")

# --- 2. CSS DEFINITIVO (Pulisce tutto e toglie il grigio) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&display=swap');
    
    /* Forza il tema scuro totale */
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Inter', sans-serif; }
    
    /* Nasconde Sidebar e Toolbar di Streamlit che sporcano lo schermo */
    section[data-testid="stSidebar"] { display: none !important; }
    header { visibility: hidden !important; }
    footer { visibility: hidden !important; }
    
    /* Card Glassmorphism per i widget */
    div[data-testid="stVerticalBlock"] > div.element-container { 
        background: rgba(255, 255, 255, 0.02); 
        border-radius: 10px; padding: 5px; 
    }

    /* Personalizzazione Input e Slider (Togliamo il rosso brutto) */
    .stNumberInput input, .stTextInput input {
        background-color: #111 !important; color: #ffd700 !important; border: 1px solid #333 !important;
    }
    .stSlider > div > div > div > div { background-color: #ffd700 !important; } /* Colore slider oro */
    
    /* Bottoni Custom */
    .stButton > button {
        background: #ffd700 !important; color: #000 !important;
        font-weight: bold !important; border-radius: 8px !important;
        border: none !important; width: 100%; height: 45px;
    }
    
    /* Titoli */
    .main-title { font-size: 40px; font-weight: 800; color: #fff; text-align: center; margin-bottom: 40px; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DI ACCESSO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    # LANDING / LOGIN
    st.markdown('<h1 class="main-title">ZenTrader AI Terminal</h1>', unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 0.8, 1])
    with col:
        with st.form("login_form"):
            st.markdown("<p style='text-align:center; color:#888;'>Inserisci le credenziali Pro</p>", unsafe_allow_html=True)
            u = st.text_input("Username", label_visibility="collapsed", placeholder="Username")
            p = st.text_input("Password", type="password", label_visibility="collapsed", placeholder="Password")
            # CORREZIONE ERRORE: Usiamo il comando corretto
            submit = st.form_submit_button("SBLOCCA TERMINALE")
            
            if submit:
                if u == "luca" and p == "zen2026":
                    st.session_state['auth'] = True
                    st.rerun()
                else:
                    st.error("Accesso negato")
else:
    # --- TERMINALE OPERATIVO (Pulito, senza sidebar) ---
    st.markdown("<h2 style='text-align:center; color:#ffd700;'>💎 TERMINALE OPERATIVO</h2>", unsafe_allow_html=True)
    
    col_l, col_c, col_r = st.columns([1, 2, 1])
    
    with col_l:
        st.markdown("### 🧮 Rischio")
        bal = st.number_input("Equità ($)", value=10000)
        risk = st.slider("Rischio %", 0.1, 2.0, 0.5)
        sl = st.number_input("Stop Loss (Pips)", value=20)
        lotti = round((bal * (risk/100)) / (sl * 10), 2)
        st.markdown(f"<p style='font-size:14px; color:#888;'>LOTTI SUGGERITI</p><h1 style='color:#ffd700;'>{lotti}</h1>", unsafe_allow_html=True)
        
    with col_c:
        # Grafico pulito
        st.components.v1.html("""
            <div id="tv" style="height:600px; border-radius:15px; overflow:hidden; border:1px solid #222;"></div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>new TradingView.widget({"width": "100%", "height": 600, "symbol": "OANDA:XAUUSD", "interval": "15", "theme": "dark", "container_id": "tv"});</script>
        """, height=600)
        
    with col_r:
        st.markdown("### 🚀 Esecuzione")
        st.write(f"Asset: **XAUUSD**")
        st.write(f"Size: **{lotti}**")
        if st.button("ESEGUI ORDINE"):
            st.success("Ordine inviato a MT5")
        
        st.divider()
        if st.button("LOGOUT"):
            st.session_state.auth = False
            st.rerun()
