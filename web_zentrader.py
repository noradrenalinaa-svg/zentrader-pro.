import streamlit as st
import datetime
import time

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="ZenTrader AI Pro", layout="wide", page_icon="💎")

# --- 2. CSS "BLACK EDITION" UI ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Inter:wght@300;400;600&display=swap');
    
    .stApp { background: #000000; color: #ffffff; font-family: 'Inter', sans-serif; }
    
    /* Card Design */
    .glass-card { 
        background: linear-gradient(145deg, #0a0a0a 0%, #111111 100%); 
        border: 1px solid #1f1f1f; 
        border-radius: 16px; padding: 20px; margin-bottom: 20px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    }
    
    .gold-glow { 
        border: 1px solid #ffd70033 !important; 
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.05);
    }
    
    /* Input Styling */
    .stNumberInput input, .stSelectbox div, .stTextArea textarea {
        background-color: #000 !important; color: #ffd700 !important;
        border: 1px solid #222 !important; border-radius: 8px !important;
    }
    
    /* Typography */
    .stat-label { font-size: 10px; color: #555; text-transform: uppercase; letter-spacing: 2.5px; margin-bottom: 8px; }
    .stat-value { font-family: 'Orbitron'; font-size: 28px; color: #ffd700; text-shadow: 0 0 10px rgba(255,215,0,0.2); }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #ffd700, #ff8c00) !important;
        color: #000 !important; font-weight: 700 !important; border: none !important;
        border-radius: 10px !important; padding: 12px !important; width: 100%;
        transition: 0.3s;
    }
    .stButton > button:hover { transform: scale(1.02); box-shadow: 0 0 20px rgba(255,215,0,0.4); }

    /* Timeframe Badges */
    .badge-up { background: rgba(0,255,100,0.1); color: #00ff64; padding: 3px 8px; border-radius: 5px; font-size: 10px; font-weight: bold; }
    .badge-down { background: rgba(255,50,50,0.1); color: #ff3232; padding: 3px 8px; border-radius: 5px; font-size: 10px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 3. CONTROLLO ACCESSO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    # Home Page Minimalista per il Login
    st.markdown("<div style='height:100px;'></div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; font-family:Orbitron; color:#ffd700; font-size:50px;'>ZENTRADER AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#444; letter-spacing:5px;'>ELITE TRADING INFRASTRUCTURE</p>", unsafe_allow_html=True)
    
    _, col_log, _ = st.columns([1.2, 1, 1.2])
    with col_log:
        st.markdown("<div class='glass-card' style='margin-top:40px;'>", unsafe_allow_html=True)
        u = st.text_input("SYSTEM ID")
        p = st.text_input("ACCESS KEY", type="password")
        if st.button("INITIALIZE"):
            if u == "luca" and p == "zen2026":
                st.session_state['auth'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
else:
    # --- TERMINALE OPERATIVO PRO ---
    # Header minimal con icone
    h1, h2, h3 = st.columns([2, 1, 1])
    with h1: st.markdown("<h2 style='font-family:Orbitron; color:#ffd700; margin:0;'>ZEN.TRADER // TERMINAL</h2>", unsafe_allow_html=True)
    with h2: st.markdown("<p style='color:#00ff64; font-size:12px; margin-top:10px;'>● MT5 BRIDGE ACTIVE</p>", unsafe_allow_html=True)
    with h3: 
        if st.button("LOGOUT", key="logout"):
            st.session_state['auth'] = False
            st.rerun()

    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

    # LAYOUT 3 COLONNE (1 : 2.5 : 1)
    c_risk, c_chart, c_intel = st.columns([1, 2.5, 1])

    with c_risk:
        # RISK ENGINE CARD
        st.markdown('<div class="glass-card gold-glow">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>Risk Parameters</p>", unsafe_allow_html=True)
        balance = st.number_input("Account Equity ($)", value=10000, step=1000)
        risk_pct = st.slider("Risk per Trade", 0.1, 2.0, 0.5, format="%.1f%%")
        sl_pips = st.number_input("Stop Loss (Pips)", value=20)
        
        # Calcolo Size
        lots = round((balance * (risk_pct/100)) / (sl_pips * 10), 2)
        
        st.markdown("<div style='text-align:center; margin:20px 0;'>", unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>Recommended Size</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='stat-value' style='font-size:48px;'>{lots}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.button("🚀 EXECUTE ORDER")
        st.markdown('</div>', unsafe_allow_html=True)

        # DISCIPLINE CARD
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>Discipline Checklist</p>", unsafe_allow_html=True)
        st.checkbox("High Timeframe Trend")
        st.checkbox("No News within 30m")
        st.checkbox("Risk fully accepted")
        st.markdown('</div>', unsafe_allow_html=True)

    with c_chart:
        # CHART INTEGRATO (Senza bordi brutti)
        st.components.v1.html(f"""
            <div id="chart" style="height:700px; border-radius:12px; overflow:hidden; border:1px solid #1f1f1f;"></div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>
            new TradingView.widget({{"width": "100%", "height": 700, "symbol": "OANDA:XAUUSD", "interval": "15", "theme": "dark", "style": "1", "locale": "it", "enable_publishing": false, "container_id": "chart"}});
            </script>
        """, height=700)

    with c_intel:
        # AI MARKET SCANNER
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>AI Trend Scanner</p>", unsafe_allow_html=True)
        st.markdown("""
            <div style='display:flex; justify-content:space-between; margin:10px 0;'>
                <span>M15 <span class='badge-up'>BULLISH</span></span>
                <span>H1 <span class='badge-up'>BULLISH</span></span>
                <span>D1 <span class='badge-down'>BEARISH</span></span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # NEWS ALERT CARD
        st.markdown('<div class="glass-card" style="border-left: 2px solid #ff3232;">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label' style='color:#ff3232;'>High Impact News</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:12px; margin:0;'><b>USD - Retail Sales</b></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:10px; color:#666;'>Today at 14:30 (In 2h 25m)</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # SMART JOURNAL CARD
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>Smart Journal</p>", unsafe_allow_html=True)
        st.text_input("Trade Setup", placeholder="e.g. Liquidity Sweep")
        st.text_area("Trading Notes", placeholder="Emotions, targets...", height=180)
        if st.button("SAVE ANALYSIS"):
            st.toast("Trade Analysis Saved!")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<p style='text-align:center; color:#222; font-size:10px; margin-top:30px; letter-spacing:5px;'>ZEN-ALGO INTELLIGENCE UNIT // VERSION 5.5</p>", unsafe_allow_html=True)
