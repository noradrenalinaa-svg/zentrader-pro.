import streamlit as st
import datetime

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="ZenTrader AI Elite", layout="wide", page_icon="💎")

# --- 2. CSS CUSTOM ULTRA-PREMIUM (Aggiornato) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    .stApp { background-color: #020202; color: #fff; }
    .premium-card { background: #0a0a0a; border: 1px solid #1a1a1a; border-radius: 12px; padding: 20px; margin-bottom: 15px; }
    .gold-border { border: 1px solid #ffd70033; }
    .stat-label { font-size: 10px; color: #555; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 5px; }
    .stat-value { font-family: 'Orbitron'; font-size: 22px; color: #ffd700; }
    .stTextInput>div>div>input, .stTextArea>div>textarea { background-color: #111 !important; color: #fff !important; border: 1px solid #222 !important; }
    .stCheckbox { font-size: 12px; color: #888; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DI ACCESSO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown("<h1 style='text-align:center; font-family:Orbitron; color:#ffd700; margin-top:100px;'>ZENTRADER AI</h1>", unsafe_allow_html=True)
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
    with c1: st.markdown("<h2 style='font-family:Orbitron; color:#ffd700;'>ZEN TERMINAL v4.0</h2>", unsafe_allow_html=True)
    with c2: st.markdown(f"<p style='color:#666; margin-top:10px;'>{datetime.datetime.now().strftime('%d %B %Y | %H:%M')}</p>", unsafe_allow_html=True)
    with c3: 
        if st.button("LOGOUT"):
            st.session_state['auth'] = False
            st.rerun()

    st.divider()

    col_side, col_main, col_journal = st.columns([1, 2.2, 0.8])

    # --- COLONNA SINISTRA: RISCHIO & DISCIPLINA ---
    with col_side:
        st.markdown('<div class="premium-card gold-border">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>1. Checklist Disciplina</p>", unsafe_allow_html=True)
        check1 = st.checkbox("Analisi completata")
        check2 = st.checkbox("Nessuna news imminente")
        check3 = st.checkbox("Accetto la perdita")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>2. Risk Engine</p>", unsafe_allow_html=True)
        balance = st.number_input("Equity ($)", value=10000)
        risk_pct = st.slider("Rischio %", 0.1, 2.0, 0.5)
        sl_pips = st.number_input("Stop Loss", value=20)
        
        risk_cash = balance * (risk_pct / 100)
        lots = round(risk_cash / (sl_pips * 10), 2)
        
        if check1 and check2 and check3:
            st.markdown(f"<div style='text-align:center; padding:10px; background:#ffd700; border-radius:8px; color:black;'>", unsafe_allow_html=True)
            st.markdown(f"<span style='font-size:12px; font-weight:bold;'>SIZE SUGGERITA</span><br><span style='font-family:Orbitron; font-size:28px;'>{lots}</span>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("Completa la checklist per sbloccare la size.")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- COLONNA CENTRALE: GRAFICO ---
    with col_main:
        st.components.v1.html(f"""
            <div id="tv_chart" style="height:650px; border-radius:12px; overflow:hidden; border:1px solid #1a1a1a;"></div>
            <script src="https://s3.tradingview.com/tv.js"></script>
            <script>
            new TradingView.widget({{
              "width": "100%", "height": 650, "symbol": "OANDA:XAUUSD",
              "interval": "15", "theme": "dark", "style": "1", "locale": "it", "container_id": "tv_chart"
            }});
            </script>
        """, height=650)

    # --- COLONNA DESTRA: JOURNAL & AI ---
    with col_journal:
        st.markdown('<div class="premium-card" style="height:650px;">', unsafe_allow_html=True)
        st.markdown("<p class='stat-label'>📓 Trade Journal</p>", unsafe_allow_html=True)
        st.text_input("Asset", placeholder="es. XAUUSD")
        st.selectbox("Setup", ["Breakout", "Retest", "Trendline", "Smart Money"])
        st.text_area("Perché entri?", placeholder="Descrivi il tuo 'Why'...", height=150)
        
        st.markdown("<br><p class='stat-label'>💡 AI Insight</p>", unsafe_allow_html=True)
        st.write("Il Volatility Index è basso. Considera target conservativi.")
        
        if st.button("SALVA TRADE"):
            st.success("Trade salvato nel Journal!")
        
        st.divider()
        st.markdown("<p class='stat-label'>⏳ Zen Mode</p>", unsafe_allow_html=True)
        if st.button("ATTIVA FOCUS (30m)"):
            st.toast("Zen Mode Attiva. Allontanati dal grafico.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<p style='text-align:center; color:#222; font-size:10px;'>ZEN-ALGO INTELLIGENCE UNIT // DISCIPLINE IS FREEDOM</p>", unsafe_allow_html=True)
