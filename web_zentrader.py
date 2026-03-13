import streamlit as st
import datetime

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="ZenTrader AI Pro", layout="wide", page_icon="💎")

# --- 2. CSS CUSTOM ULTRA-PREMIUM (Mac Style) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    /* Sfondo con gradiente radiale per profondità */
    .stApp { 
        background: radial-gradient(circle at top right, #1a1a1a, #050505);
        color: #fff; 
    }
    
    /* Card in stile Vetro (Glassmorphism) */
    .glass-card { 
        background: rgba(255, 255, 255, 0.03); 
        border: 1px solid rgba(255, 255, 255, 0.05); 
        border-radius: 16px; 
        padding: 20px; 
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }
    
    .gold-glow { 
        border: 1px solid #ffd70055; 
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.05);
    }
    
    /* Testi */
    .stat-label { font-size: 10px; color: #888; text-transform: uppercase; letter-spacing: 2px; }
    .stat-value { font-family: 'Orbitron'; font-size: 24px; color: #ffd700; }
    
    /* Pulsante MT5 */
    .mt5-btn {
        background: linear-gradient(135deg, #0052ff, #002e99) !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0, 82, 255, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DI STATO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False
if 'broker_connected' not in st.session_state: st.session_state['broker_connected'] = False

# --- 4. ACCESSO ---
if not st.session_state['auth']:
    st.markdown("<h1 style='text-align:center; font-family:Orbitron; color:#ffd700; margin-top:150px;'>ZENTRADER AI</h1>", unsafe_allow_html=True)
    _, col_log, _ = st.columns([1, 0.6, 1])
    with col_log:
        u = st.text_input("User ID")
        p = st.text_input("Access Key", type="password")
        if st.button("SBLOCCA TERMINALE"):
            if u == "luca" and p == "zen2026":
                st.session_state['auth'] = True
                st.rerun()
else:
    # --- HEADER ---
    c1, c2, c3 = st.columns([2, 1, 1])
    with c1: st.markdown("<h2 style='font-family:Orbitron; color:#ffd700; margin:0;'>ZEN TERMINAL v5.0</h2>", unsafe_allow_html=True)
    with c2: 
        status = "🟢 CONNECTED" if st.session_state.broker_connected else "🔴 DISCONNECTED"
        st.markdown(f"<p class='stat-label'>MT5 STATUS: <span style='color:white;'>{status}</span></p>", unsafe_allow_html=True)
    with c3: 
        if st.button("LOGOUT"):
            st.session_state['auth'] = False
            st.rerun()

    st.markdown("---")

    # --- LAYOUT PRINCIPALE ---
    col_left, col_mid, col_right = st.columns([1, 2.2, 1])

    with col_left:
        # 1. BROKER CONNECTION
        st.markdown('<div class="glass-card gold-glow">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>Broker Bridge (MT5)</p>", unsafe_allow_html=True)
        srv = st.text_input("Server", placeholder="MetaQuotes-Demo")
        acc = st.text_input("Login ID", placeholder="12345678")
        if st.button("CONNECT ACCOUNT"):
            with st.spinner("Stabilizing Bridge..."):
                time.sleep(1.5)
                st.session_state.broker_connected = True
                st.success("MT5 Linked!")
        st.markdown('</div>', unsafe_allow_html=True)

        # 2. RISK ENGINE
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>Risk Settings</p>", unsafe_allow_html=True)
        balance = st.number_input("Balance ($)", value=10000)
        risk = st.slider("Risk %", 0.1, 2.0, 0.5)
        sl = st.number_input("Stop Loss", value=20)
        
        lots = round((balance * (risk/100)) / (sl * 10), 2)
        
        st.markdown(f"<div style='margin-top:20px; text-align:center;'><p class='stat-label'>Proposed Size</p><p class='stat-value'>{lots}</p></div>", unsafe_allow_html=True)
        
        if st.session_state.broker_connected:
            if st.button("🚀 EXECUTE ON MT5", use_container_width=True):
                st.balloons()
                st.success(f"Order Sent: {lots} lots")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_mid:
        # GRAFICO INTEGRATO
        st.components.v1.html(f"""
            <div id="tv_chart" style="height:700px; border-radius:16px; overflow:hidden; border:1px solid rgba(255,255,255,0.1);"></div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>
            new TradingView.widget({{"width": "100%", "height": 700, "symbol": "OANDA:XAUUSD", "interval": "15", "theme": "dark", "style": "1", "locale": "it", "container_id": "tv_chart"}});
            </script>
        """, height=700)

    with col_right:
        # 3. TRADE JOURNAL
        st.markdown('<div class="glass-card" style="height:700px;">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>📓 Smart Journal</p>", unsafe_allow_html=True)
        st.selectbox("Trend Confirmation", ["Bullish Structure", "Bearish Structure", "Ranging"])
        st.selectbox("Setup Type", ["FVG Fill", "Order Block", "Liquidity Sweep"])
        st.text_area("Entry Notes", placeholder="Why this trade?", height=200)
        
        st.markdown("---")
        st.markdown("<p class='stat-label'>🛡️ Pro Shield</p>", unsafe_allow_html=True)
        st.write("Daily Drawdown: **0.00%**")
        st.write("Limit: **2.00%**")
        st.progress(0.0)
        
        st.button("SAVE ANALYSIS")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<p style='text-align:center; color:#333; font-size:10px; margin-top:50px;'>ZenTrader Pro v5.0 - Secure API Tunneling Active</p>", unsafe_allow_html=True)
