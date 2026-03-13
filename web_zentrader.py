import streamlit as st
import datetime
import time

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="ZenTrader AI Elite", layout="wide", page_icon="💎")

# --- 2. CSS LUXURY 5.2 ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    .stApp { background: radial-gradient(circle at top right, #111, #050505); color: #fff; }
    
    .glass-card { 
        background: rgba(255, 255, 255, 0.02); 
        border: 1px solid rgba(255, 255, 255, 0.05); 
        border-radius: 12px; padding: 15px; margin-bottom: 15px; 
    }
    .gold-glow { border: 1px solid #ffd70044; box-shadow: 0 0 15px rgba(255, 215, 0, 0.03); }
    
    .stat-label { font-size: 9px; color: #666; text-transform: uppercase; letter-spacing: 2px; }
    .stat-value { font-family: 'Orbitron'; font-size: 18px; color: #ffd700; }
    
    /* Timeframe badges */
    .tf-badge { 
        padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: bold;
        background: rgba(0, 255, 65, 0.1); color: #00ff41; border: 1px solid #00ff4133;
    }
</style>
""", unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown("<h1 style='text-align:center; font-family:Orbitron; color:#ffd700; margin-top:150px;'>ZENTRADER AI</h1>", unsafe_allow_html=True)
    _, col_log, _ = st.columns([1, 0.6, 1])
    with col_log:
        u = st.text_input("User ID")
        p = st.text_input("Access Key", type="password")
        if st.button("UNLOCK"):
            if u == "luca" and p == "zen2026":
                st.session_state['auth'] = True
                st.rerun()
else:
    # --- HEADER ---
    c1, c2, c3 = st.columns([2, 1, 1])
    with c1: st.markdown("<h3 style='font-family:Orbitron; color:#ffd700; margin:0;'>ZEN TERMINAL PRO</h3>", unsafe_allow_html=True)
    with c3: 
        if st.button("LOGOUT"):
            st.session_state['auth'] = False
            st.rerun()

    st.divider()

    # --- NUOVO LAYOUT BILANCIATO 1 : 2.5 : 1 ---
    col_risk, col_chart, col_intel = st.columns([1, 2.5, 1])

    # COLONNA 1: RISCHIO E BROKER
    with col_risk:
        st.markdown('<div class="glass-card gold-glow">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>Risk Engine</p>", unsafe_allow_html=True)
        balance = st.number_input("Equity ($)", value=10000)
        risk = st.slider("Risk %", 0.1, 2.0, 0.5)
        sl = st.number_input("Stop Loss (Pips)", value=20)
        lots = round((balance * (risk/100)) / (sl * 10), 2)
        st.markdown(f"<div style='text-align:center;'><p class='stat-value' style='font-size:35px;'>{lots}</p></div>", unsafe_allow_html=True)
        st.button("🚀 SEND TO MT5", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>Checklist Disciplina</p>", unsafe_allow_html=True)
        st.checkbox("Analisi HTF fatta")
        st.checkbox("Rischio accettato")
        st.checkbox("News controllate")
        st.markdown('</div>', unsafe_allow_html=True)

    # COLONNA 2: IL GRAFICO (PIÙ LARGO)
    with col_chart:
        st.components.v1.html(f"""
            <div id="tv_chart" style="height:680px; border-radius:12px; overflow:hidden; border:1px solid #222;"></div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>
            new TradingView.widget({{"width": "100%", "height": 680, "symbol": "OANDA:XAUUSD", "interval": "15", "theme": "dark", "style": "1", "locale": "it", "container_id": "tv_chart"}});
            </script>
        """, height=680)

    # COLONNA 3: MARKET INTELLIGENCE (RIEMPIE IL VUOTO)
    with col_intel:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>AI Trend Scanner</p>", unsafe_allow_html=True)
        st.markdown("""
            <div style='display:flex; justify-content:space-between; margin-top:10px;'>
                <span>M15 <span class='tf-badge'>BULLISH</span></span>
                <span>H1 <span class='tf-badge'>BULLISH</span></span>
                <span>D1 <span class='tf-badge' style='background:rgba(255,75,75,0.1); color:#ff4b4b; border:1px solid #ff4b4b33;'>BEARISH</span></span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>Upcoming News</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:11px; margin-bottom:5px;'>🔴 <b>USD - CPI m/m</b><br><span style='color:#666;'>In: 01h 45m</span></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:11px;'>🟠 <b>GBP - GDP q/q</b><br><span style='color:#666;'>In: 04h 20m</span></p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>Trade Journal</p>", unsafe_allow_html=True)
        st.text_input("Setup Name", placeholder="es. Gold Liquidity")
        st.text_area("Notes", placeholder="Sostegni/Resistenze...", height=150)
        st.button("SAVE TRADE", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<p style='text-align:center; color:#222; font-size:10px; margin-top:30px;'>ZEN-ALGO INTELLIGENCE UNIT // DISCIPLINE IS FREEDOM</p>", unsafe_allow_html=True)
