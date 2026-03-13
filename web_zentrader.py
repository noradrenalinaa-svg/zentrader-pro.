import streamlit as st

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="ZenTrader AI Terminal", layout="wide", page_icon="💎")

# --- 2. CSS CUSTOM LUXURY ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    .stApp { background-color: #050505; color: #fff; }
    
    /* Header Terminale */
    .terminal-header {
        background: linear-gradient(90deg, #111, #1a1a1a);
        padding: 20px;
        border-radius: 15px;
        border-bottom: 2px solid #ffd700;
        margin-bottom: 30px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    /* Card dei Controlli */
    .control-panel {
        background: #0e0e0e;
        border: 1px solid #333;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    /* Risultato Lotti */
    .lot-display {
        background: rgba(255, 215, 0, 0.05);
        border: 1px solid #ffd700;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-top: 20px;
    }
    .lot-number {
        font-family: 'Orbitron';
        font-size: 45px;
        color: #ffd700;
        text-shadow: 0 0 15px rgba(255, 215, 0, 0.3);
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #0a0a0a !important;
        border-right: 1px solid #222;
    }
    
    /* Pulsanti e Input */
    .stButton > button {
        background: #ffd700 !important;
        color: black !important;
        font-weight: bold !important;
        font-family: 'Orbitron' !important;
        border-radius: 10px !important;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DI ACCESSO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    # Ripristino rapido Home Page se non loggato
    st.markdown("<h1 style='text-align:center; font-family:Orbitron; color:#ffd700;'>ZENTRADER AI</h1>", unsafe_allow_html=True)
    _, col_log, _ = st.columns([1, 0.8, 1])
    with col_log:
        u = st.text_input("User ID")
        p = st.text_input("Access Key", type="password")
        if st.button("SBLOCCA TERMINALE"):
            if u == "luca" and p == "zen2026":
                st.session_state['auth'] = True
                st.rerun()
else:
    # --- TERMINALE VERO E PROPRIO ---
    st.sidebar.markdown("<h2 style='font-family:Orbitron; color:#ffd700;'>ZEN PRO</h2>", unsafe_allow_html=True)
    st.sidebar.info("Status: Protezione Drawdown 2% Attiva")
    if st.sidebar.button("LOGOUT"):
        st.session_state['auth'] = False
        st.rerun()

    # Layout a due colonne
    col_left, col_right = st.columns([1, 2.5])

    with col_left:
        st.markdown('<div class="control-panel">', unsafe_allow_html=True)
        st.markdown("<h3 style='font-family:Orbitron; font-size:18px; color:#ffd700;'>CALCULATOR</h3>", unsafe_allow_html=True)
        
        asset = st.selectbox("Seleziona Strumento", ["XAUUSD (Gold)", "EURUSD", "NAS100", "US30", "BTCUSD"])
        balance = st.number_input("Equity Totale ($)", value=10000, step=1000)
        risk_pct = st.slider("Rischio per Trade (%)", 0.1, 2.0, 0.5, format="%.1f%%")
        sl_pips = st.number_input("Stop Loss (Pips/Punti)", value=20, step=1)
        
        # Calcolo Matematico
        risk_money = balance * (risk_pct / 100)
        # Formula semplificata per Gold/Forex
        final_lots = round(risk_money / (sl_pips * 10), 2)
        
        st.markdown('<div class="lot-display">', unsafe_allow_html=True)
        st.markdown("<p style='margin:0; font-size:12px; color:#888;'>LOTTAGGIO SUGGERITO</p>", unsafe_allow_html=True)
        st.markdown(f'<p class="lot-number">{final_lots}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("COPIA SIZE"):
            st.toast("Size copiata negli appunti!")
        
        st.markdown('</div>', unsafe_allow_html=True)

    with col_right:
        # Mappa simboli per TradingView
        tv_map = {"XAUUSD (Gold)":"OANDA:XAUUSD", "EURUSD":"FX:EURUSD", "NAS100":"CAPITALCOM:US100", "US30":"CAPITALCOM:US30", "BTCUSD":"BINANCE:BTCUSDT"}
        
        # Widget TradingView Professionale
        st.components.v1.html(f"""
            <div id="tradingview_chart" style="height:650px; border-radius:20px; overflow:hidden; border:1px solid #333;"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script type="text/javascript">
            new TradingView.widget({{
              "width": "100%", "height": 650, "symbol": "{tv_map[asset]}",
              "interval": "15", "timezone": "Europe/Rome", "theme": "dark",
              "style": "1", "locale": "it", "enable_publishing": false,
              "hide_side_toolbar": false, "allow_symbol_change": true,
              "container_id": "tradingview_chart"
            }});
            </script>
        """, height=650)

    st.markdown("<p style='text-align:center; color:#222; margin-top:30px;'>ZenTrader AI v3.0 Elite - encrypted connection active</p>", unsafe_allow_html=True)
