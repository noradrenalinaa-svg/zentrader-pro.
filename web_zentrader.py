import streamlit as st
import datetime
import time

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="ZenTrader AI - Citadel", layout="wide", page_icon="🛡️")

# --- 2. UI DESIGN "CITADEL" (Ultra-Luxury) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;900&family=Inter:wght@300;400;700&display=swap');
    
    .stApp { background: #020202; color: #ffffff; }
    
    /* Pannelli ad incasso con riflessi */
    .module-card {
        background: linear-gradient(180deg, #0f0f0f 0%, #050505 100%);
        border: 1px solid #1a1a1a;
        border-radius: 12px; padding: 20px; margin-bottom: 15px;
    }
    
    .danger-zone { border: 1px solid #ff323255 !important; background: rgba(255,50,50,0.02) !important; }
    .gold-glow { border: 1px solid #ffd70044 !important; box-shadow: 0 0 30px rgba(255,215,0,0.05); }

    /* Metriche istituzionali */
    .metric-label { font-size: 10px; color: #444; text-transform: uppercase; letter-spacing: 3px; font-weight: 700; }
    .metric-value { font-family: 'Orbitron'; font-size: 26px; color: #ffd700; }
    
    /* Kill Switch Button */
    .kill-btn > button {
        background: linear-gradient(90deg, #ff4b4b, #990000) !important;
        color: white !important; border: none !important; font-family: 'Orbitron'; font-weight: 900; height: 50px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DI STATO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False
if 'drawdown' not in st.session_state: st.session_state['drawdown'] = 0.45 # Esempio drawdown attuale

if not st.session_state['auth']:
    st.markdown("<div style='height:150px;'></div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; font-family:Orbitron; color:#ffd700; font-size:60px;'>ZENTRADER AI</h1>", unsafe_allow_html=True)
    _, col_log, _ = st.columns([1.2, 1, 1.2])
    with col_log:
        u = st.text_input("LICENSE ID")
        p = st.text_input("ENCRYPTION KEY", type="password")
        if st.button("CONNECT TO CITADEL"):
            if u == "luca" and p == "zen2026":
                st.session_state['auth'] = True
                st.rerun()
else:
    # --- TOP BAR (Istituzionale) ---
    t1, t2, t3, t4 = st.columns([1.5, 1, 1, 0.5])
    with t1: st.markdown("<h2 style='font-family:Orbitron; color:#ffd700; margin:0;'>ZEN.TRADER v6.0</h2>", unsafe_allow_html=True)
    with t2: st.markdown(f"<p class='metric-label'>Daily Drawdown</p><p style='color:#ff3232; font-family:Orbitron; font-size:18px;'>{st.session_state.drawdown}% / 2.0%</p>", unsafe_allow_html=True)
    with t3: st.markdown("<p class='metric-label'>MT5 Bridge</p><p style='color:#00ff64; font-family:Orbitron; font-size:18px;'>STABLE</p>", unsafe_allow_html=True)
    with t4: 
        if st.button("EXIT"):
            st.session_state['auth'] = False
            st.rerun()

    st.divider()

    # --- MAIN TERMINAL ---
    c_left, c_mid, c_right = st.columns([1.1, 2.8, 1.1])

    with c_left:
        # 1. RISK ENGINE & EXECUTION
        st.markdown('<div class="module-card gold-glow">', unsafe_allow_html=True)
        st.markdown("<p class='metric-label'>1. Execution Engine</p>", unsafe_allow_html=True)
        balance = st.number_input("Equity ($)", value=10000)
        risk = st.slider("Risk per Trade", 0.1, 2.0, 0.5)
        sl = st.number_input("Stop Loss (Pips)", value=15)
        
        lots = round((balance * (risk/100)) / (sl * 10), 2)
        st.markdown(f"<div style='text-align:center; padding:15px;'><p class='metric-value' style='font-size:40px;'>{lots}</p><p class='metric-label'>Lots</p></div>", unsafe_allow_html=True)
        
        if st.button("⚡ EXECUTE POSITION", use_container_width=True):
            st.toast("Order sent to MetaTrader 5 Bridge")
        st.markdown('</div>', unsafe_allow_html=True)

        # 2. EMERGENCY KILL SWITCH
        st.markdown('<div class="module-card danger-zone kill-btn">', unsafe_allow_html=True)
        st.markdown("<p class='metric-label' style='color:#ff3232;'>2. Security Protocol</p>", unsafe_allow_html=True)
        if st.button("PANIC: CLOSE ALL POSITIONS", use_container_width=True):
            st.error("MT5 COMMAND: ALL ORDERS CLOSED.")
        st.markdown("<p style='font-size:9px; color:#444; margin-top:5px;'>Chiusura istantanea di ogni ordine attivo su MT5.</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c_mid:
        # 3. CHART & SPREAD MONITOR
        st.components.v1.html(f"""
            <div id="tv" style="height:650px; border-radius:12px; overflow:hidden;"></div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>new TradingView.widget({{"width": "100%", "height": 650, "symbol": "OANDA:XAUUSD", "interval": "15", "theme": "dark", "style": "1", "container_id": "tv"}});</script>
        """, height=650)
        
        # Spread Monitor Bar
        st.markdown("""
            <div style='background:#111; padding:10px; border-radius:10px; display:flex; justify-content:space-around;'>
                <span style='font-size:11px; color:#666;'>SPREAD: <b style='color:#ffd700;'>1.2 Pips</b></span>
                <span style='font-size:11px; color:#666;'>VOLATILITY: <b style='color:#00ff64;'>OPTIMAL</b></span>
                <span style='font-size:11px; color:#666;'>LIQUIDITY: <b style='color:#00ff64;'>HIGH</b></span>
            </div>
        """, unsafe_allow_html=True)

    with c_right:
        # 4. AI MARKET SCANNER
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        st.markdown("<p class='metric-label'>3. AI Trend Scanner</p>", unsafe_allow_html=True)
        st.markdown("""
            <div style='margin:10px 0;'>
                <div style='display:flex; justify-content:space-between;'><span>M15</span><b style='color:#00ff64;'>BULLISH</b></div>
                <div style='display:flex; justify-content:space-between;'><span>H1</span><b style='color:#00ff64;'>BULLISH</b></div>
                <div style='display:flex; justify-content:space-between;'><span>D1</span><b style='color:#ff3232;'>BEARISH</b></div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 5. NEWS CALENDAR PRO
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        st.markdown("<p class='metric-label'>4. Economic Pulse</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:11px;'><b>14:30 USD - CPI Data</b><br><span style='color:#ff3232;'>Critical Impact</span></p>", unsafe_allow_html=True)
        st.progress(0.8) # Tempo mancante visivo
        st.markdown('</div>', unsafe_allow_html=True)

        # 6. SMART JOURNAL
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        st.markdown("<p class='metric-label'>5. Psychology Journal</p>", unsafe_allow_html=True)
        st.text_area("Why this trade?", height=100, placeholder="Identify setup...")
        st.button("LOG TRADE")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<p style='text-align:center; color:#222; font-size:10px; letter-spacing:8px;'>ZEN-ALGO CITADEL INFRASTRUCTURE // SECURE ACCESS</p>", unsafe_allow_html=True)
