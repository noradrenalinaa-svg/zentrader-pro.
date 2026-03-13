import streamlit as st

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="ZenTrader AI Pro", layout="wide", page_icon="💎")

# --- 2. CSS CUSTOM ULTRA-PREMIUM ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    .stApp { background-color: #030303; color: #fff; }
    
    /* Pannelli */
    .premium-card {
        background: linear-gradient(145deg, #0f0f0f, #151515);
        border: 1px solid #222;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 15px;
    }
    
    .gold-border { border: 1px solid #ffd70044; }
    
    /* Metriche High-End */
    .stat-box { text-align: center; padding: 10px; border-radius: 10px; background: rgba(255,255,255,0.02); }
    .stat-label { font-size: 10px; color: #666; text-transform: uppercase; letter-spacing: 1px; }
    .stat-value { font-family: 'Orbitron'; font-size: 20px; color: #ffd700; }
    
    /* Sentiment Bar */
    .sentiment-bar {
        height: 8px;
        background: linear-gradient(90deg, #ff4b4b 0%, #ffd700 50%, #00ff41 100%);
        border-radius: 5px;
        margin: 10px 0;
    }
    
    /* Pulsanti */
    .stButton > button {
        background: linear-gradient(90deg, #ffd700, #ff8c00) !important;
        color: black !important;
        font-weight: 900 !important;
        font-family: 'Orbitron' !important;
        border: none !important;
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DI ACCESSO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown("<h1 style='text-align:center; font-family:Orbitron; color:#ffd700; margin-top:50px;'>ZENTRADER AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666;'>SYSTEM ACCESS REQUIRED</p>", unsafe_allow_html=True)
    _, col_log, _ = st.columns([1, 0.6, 1])
    with col_log:
        u = st.text_input("User ID", placeholder="Admin ID")
        p = st.text_input("Access Key", type="password", placeholder="••••••••")
        if st.button("UNLOCK SYSTEM"):
            if u == "luca" and p == "zen2026":
                st.session_state['auth'] = True
                st.rerun()
else:
    # --- HEADER TERMINALE ---
    h_col1, h_col2, h_col3 = st.columns([2, 1, 1])
    with h_col1:
        st.markdown("<h2 style='font-family:Orbitron; color:#ffd700; margin:0;'>ZEN TERMINAL PRO</h2>", unsafe_allow_html=True)
    with h_col2:
        st.markdown('<div class="stat-box"><div class="stat-label">AI SENTINEL</div><div class="stat-value" style="color:#00ff41;">SECURE</div></div>', unsafe_allow_html=True)
    with h_col3:
        if st.button("LOGOUT"):
            st.session_state['auth'] = False
            st.rerun()

    st.markdown("---")

    # --- LAYOUT PRINCIPALE ---
    col_side, col_main = st.columns([1, 3])

    with col_side:
        # 1. RISK CALCULATOR CARD
        st.markdown('<div class="premium-card gold-border">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>Risk Engine</p>", unsafe_allow_html=True)
        asset = st.selectbox("Asset", ["XAUUSD (Gold)", "NAS100", "EURUSD", "BTCUSD"])
        balance = st.number_input("Account Balance ($)", value=10000, step=1000)
        risk_pct = st.slider("Risk Per Trade", 0.1, 2.0, 0.5, format="%.1f%%")
        sl_pips = st.number_input("Stop Loss", value=20)
        
        risk_cash = balance * (risk_pct / 100)
        lots = round(risk_cash / (sl_pips * 10), 2)
        
        st.markdown(f"""
            <div style="text-align:center; margin-top:15px; padding:15px; background:rgba(255,215,0,0.1); border-radius:10px;">
                <div class="stat-label">SUGGESTED POSITION</div>
                <div style="font-family:Orbitron; font-size:35px; color:#ffd700;">{lots} LOTS</div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 2. MARKET SENTIMENT CARD
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>Market Sentiment (AI)</p>", unsafe_allow_html=True)
        st.markdown("<div class='sentiment-bar'></div>", unsafe_allow_html=True)
        st.markdown("<div style='display:flex; justify-content:space-between; font-size:10px; color:#555;'><span>BEARISH</span><span>NEUTRAL</span><span>BULLISH</span></div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; font-size:12px; margin-top:10px; color:#00ff41;'>Strong Accumulation Detected</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 3. NEWS FEED ALERT
        st.markdown('<div class="premium-card" style="border-left: 3px solid #ff4b4b;">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label' style='color:#ff4b4b;'>⚠️ News Sentinel</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:12px; margin:0;'>Next Impact: <b>US Core CPI</b></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:10px; color:#666;'>In: 02h 45m 12s</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_main:
        # CHART CARD
        tv_map = {"XAUUSD (Gold)":"OANDA:XAUUSD", "NAS100":"CAPITALCOM:US100", "EURUSD":"FX:EURUSD", "BTCUSD":"BINANCE:BTCUSDT"}
        
        st.components.v1.html(f"""
            <div id="tv_chart" style="height:680px; border-radius:15px; border:1px solid #222; overflow:hidden;"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script type="text/javascript">
            new TradingView.widget({{
              "width": "100%", "height": 680, "symbol": "{tv_map[asset]}",
              "interval": "15", "theme": "dark", "style": "1", "locale": "it",
              "enable_publishing": false, "hide_side_toolbar": false, "container_id": "tv_chart"
            }});
            </script>
        """, height=680)

    st.markdown("<p style='text-align:center; color:#222; font-size:10px; letter-spacing:2px;'>ZEN-ALGO INTELLIGENCE UNIT // 2026</p>", unsafe_allow_html=True)
