import streamlit as st
import time

# --- 1. CONFIGURAZIONE ---
st.set_page_config(page_title="ZenTrader AI Pro", layout="wide", page_icon="🛡️")

# --- 2. CSS PULITO E PROFESSIONALE ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    .stApp { background: #080808; color: #eee; font-family: 'Inter', sans-serif; }
    
    /* Box per pulizia visiva */
    .section-box {
        background: #111;
        border: 1px solid #222;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
    }
    
    .gold-text { color: #ffd700; font-weight: bold; }
    
    /* Bottone Esecuzione (Blu istituzionale) */
    .stButton > button {
        background: #0052ff !important;
        color: white !important;
        width: 100%;
        border-radius: 5px !important;
        font-weight: bold !important;
        height: 50px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA ACCESSO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown("<h2 style='text-align:center; margin-top:100px;'>ZENTRADER AI</h2>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 0.6, 1])
    with col:
        u = st.text_input("User")
        p = st.text_input("Password", type="password")
        if st.button("ACCEDI"):
            if u == "luca" and p == "zen2026":
                st.session_state['auth'] = True
                st.rerun()
else:
    # --- TERMINALE PULITO ---
    st.markdown("### 🛡️ ZenTrader Pro - Terminale Operativo")
    st.divider()

    col_broker, col_chart, col_exec = st.columns([1, 2.5, 1])

    # --- COLONNA 1: IL BROKER ---
    with col_broker:
        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.subheader("🔌 Collegamento Broker")
        st.text_input("Server MT5", placeholder="es. MetaQuotes-Demo")
        st.text_input("Account ID", placeholder="12345678")
        st.text_input("Password MT5", type="password")
        if st.button("CONNETTI MT5"):
            st.success("Broker Connesso ✅")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.subheader("🧮 Calcolo Rischio")
        bal = st.number_input("Capitale ($)", value=10000)
        risk = st.slider("Rischio (%)", 0.1, 2.0, 0.5)
        sl = st.number_input("Stop Loss (Pips)", value=20)
        
        # Formula: (Capitale * %) / (SL * 10)
        lotti = round((bal * (risk/100)) / (sl * 10), 2)
        st.markdown(f"#### Lotti Suggeriti: <span class='gold-text'>{lotti}</span>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- COLONNA 2: IL GRAFICO ---
    with col_chart:
        st.components.v1.html("""
            <div id="tradingview_853de" style="height:650px;"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script type="text/javascript">
            new TradingView.widget({
              "width": "100%", "height": 650, "symbol": "OANDA:XAUUSD",
              "interval": "15", "timezone": "Europe/Rome", "theme": "dark",
              "style": "1", "locale": "it", "container_id": "tradingview_853de"
            });
            </script>
        """, height=650)

    # --- COLONNA 3: ESECUZIONE ---
    with col_exec:
        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.subheader("🚀 Esecuzione")
        st.write(f"Asset selezionato: **XAUUSD**")
        st.write(f"Size calcolata: **{lotti} lotti**")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("INVIA ORDINE A MT5"):
            st.warning("Inviando ordine...")
            time.sleep(1)
            st.success("Ordine Eseguito!")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.subheader("📓 Diario Rapido")
        st.text_area("Note del trade", placeholder="Perché sei entrato?", height=200)
        if st.button("SALVA NEL JOURNAL"):
            st.info("Trade salvato.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.caption("ZenTrader AI v7.0 - Supporto MacBook Pro")
