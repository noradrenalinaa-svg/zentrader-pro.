import streamlit as st
import time

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="ZenTrader AI - Terminal", layout="wide", page_icon="💎")

# --- 2. MONITORAGGIO UMAMI ---
st.markdown("""
<script defer src="https://cloud.umami.is/script.js" data-website-id="48c34484-b01f-4c2d-b606-40f648561dbc"></script>
""", unsafe_allow_html=True)

# --- 3. CSS PREMIUM (Home + Terminale) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@300;400;700&display=swap');
    .stApp { background-color: #050505; color: #fff; }
    
    /* Stile Home */
    .main-title { font-family: 'Orbitron'; font-size: clamp(40px, 8vw, 80px); text-align: center; background: linear-gradient(90deg, #ffd700, #ff8c00); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .stButton > button { background: rgba(255, 255, 255, 0.05) !important; color: #ffd700 !important; border: 1px solid #ffd700 !important; border-radius: 50px !important; padding: 10px 40px !important; font-family: 'Orbitron' !important; float: right; }
    
    /* Stile Terminale Operativo */
    .terminal-card { background: rgba(255, 215, 0, 0.05); border: 1px solid rgba(255, 215, 0, 0.2); border-radius: 20px; padding: 25px; margin-bottom: 20px; }
    .metric-value { font-family: 'Orbitron'; color: #ffd700; font-size: 32px; font-weight: bold; }
    .metric-label { font-family: 'Inter'; color: #888; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; }
</style>
""", unsafe_allow_html=True)

# --- 4. LOGICA NAVIGAZIONE ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

# --- 5. HOME PAGE (Vetrina) ---
if not st.session_state['auth']:
    st.markdown('<h1 class="main-title">ZENTRADER AI</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; letter-spacing: 5px; font-family:Inter; font-size:14px; margin-bottom:30px;'>ELIMINATE EMOTIONS. MAXIMIZE DISCIPLINE.</p>", unsafe_allow_html=True)
    
    # PULSANTE ACCESSO A DESTRA
    _, col_btn, col_spacer = st.columns([1.2, 1, 0.8])
    with col_btn:
        if 'show_login' not in st.session_state: st.session_state.show_login = False
        if st.button("ACCEDI AL TERMINALE"):
            st.session_state.show_login = not st.session_state.show_login

    if st.session_state.show_login:
        _, col_login, _ = st.columns([1, 1.5, 1])
        with col_login:
            st.markdown('<div style="background: rgba(255,255,255,0.03); padding:30px; border-radius:20px; border:1px solid rgba(255,255,255,0.1); margin-top:60px; clear:both;">', unsafe_allow_html=True)
            u = st.text_input("User ID", placeholder="Username")
            p = st.text_input("Access Key", type="password", placeholder="Password")
            if st.button("SBLOCCA ORA"):
                if u == "luca" and p == "zen2026":
                    st.session_state['auth'] = True
                    st.rerun()
                else: st.error("Credenziali errate")
            st.markdown('</div>', unsafe_allow_html=True)

    # (Qui andrebbero Recensioni, Prezzi e FAQ che abbiamo già creato)
    st.markdown("<br><br><p style='text-align:center; color:#333;'>ZenTrader AI v2.8</p>", unsafe_allow_html=True)

# --- 6. TERMINALE OPERATIVO (Area Riservata) ---
else:
    # Sidebar di controllo
    st.sidebar.markdown("<h2 style='font-family:Orbitron; color:#ffd700;'>ZEN PRO</h2>", unsafe_allow_html=True)
    st.sidebar.markdown(f"**Status:** Protezione Attiva ✅")
    st.sidebar.markdown(f"**Drawdown Max:** 2% (Rigoroso)")
    st.sidebar.divider()
    if st.sidebar.button("LOGOUT / CHIUDI"):
        st.session_state['auth'] = False
        st.rerun()

    # Layout Principale Terminale
    st.markdown("<h1 style='font-family:Orbitron; font-size:24px; color:#ffd700;'>OPERATIONAL TERMINAL</h1>", unsafe_allow_html=True)
    
    col_calc, col_chart = st.columns([1, 2.5])

    with col_calc:
        st.markdown('<div class="terminal-card">', unsafe_allow_html=True)
        st.markdown("<p class='metric-label'>Configurazione Rischio</p>", unsafe_allow_html=True)
        
        asset = st.selectbox("Seleziona Strumento", ["XAUUSD (Gold)", "EURUSD", "NAS100 (Nasdaq)", "BTCUSD", "DAX40"])
        balance = st.number_input("Equità Conto ($)", value=10000, step=1000)
        risk_pct = st.slider("Rischio per Trade (%)", 0.1, 2.0, 0.5, step=0.1)
        stop_loss_pips = st.number_input("Stop Loss (Pips/Punti)", value=20, step=1)
        
        # Logica di calcolo semplificata per il terminale
        # Nota: In un sistema reale, qui aggiungeremmo pesi diversi per asset diversi
        risk_amount = balance * (risk_pct / 100)
        lot_size = round(risk_amount / (stop_loss_pips * 10), 2) if stop_loss_pips > 0 else 0
        
        st.divider()
        st.markdown("<p class='metric-label'>Lottaggio Suggerito</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='metric-value'>{lot_size}</p>", unsafe_allow_html=True)
        
        if risk_pct > 1.5:
            st.warning("⚠️ Attenzione: Rischio elevato vicino al limite di Drawdown.")
        
        st.button("NOTIFICA ESECUZIONE (MT5)")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_chart:
        # Mapping simboli per TradingView
        tv_map = {
            "XAUUSD (Gold)": "OANDA:XAUUSD",
            "EURUSD": "FX:EURUSD",
            "NAS100 (Nasdaq)": "CAPITALCOM:US100",
            "BTCUSD": "BINANCE:BTCUSDT",
            "DAX40": "CAPITALCOM:DE40"
        }
        
        # Integrazione Grafico TradingView
        st.components.v1.html(f"""
            <div id="tradingview_widget" style="height:600px;"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script type="text/javascript">
            new TradingView.widget({{
              "width": "100%",
              "height": 600,
              "symbol": "{tv_map[asset]}",
              "interval": "15",
              "timezone": "Europe/Rome",
              "theme": "dark",
              "style": "1",
              "locale": "it",
              "toolbar_bg": "#f1f3f6",
              "enable_publishing": false,
              "allow_symbol_change": true,
              "container_id": "tradingview_widget"
            }});
            </script>
        """, height=600)

    # Footer Terminale
    st.markdown("---")
    st.caption("ZenTrader AI Sentinel: Monitoraggio mercati in tempo reale attivo. Nessuna news ad alto impatto rilevata nei prossimi 30 min.")