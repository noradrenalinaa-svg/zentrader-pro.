import streamlit as st
import pandas as pd
import numpy as np

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="ZenTrader AI", layout="wide", page_icon="💎")

# --- 2. MONITORAGGIO UMAMI (ATTIVO) ---
st.markdown("""
<script defer src="https://cloud.umami.is/script.js" data-website-id="48c34484-b01f-4c2d-b606-40f648561dbc"></script>
""", unsafe_allow_html=True)

# --- 3. CSS PREMIUM ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@400;700&display=swap');
    .stApp { background-color: #050505; color: #fff; }
    .main-title { font-family: 'Orbitron'; font-size: 70px; text-align: center; background: linear-gradient(90deg, #ffd700, #ff8c00); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0px;}
    .section-title { font-family: 'Orbitron'; color: #ffd700; text-align: center; margin-top: 50px; text-transform: uppercase; letter-spacing: 2px; }
    .price-card { background: linear-gradient(145deg, #ffd700, #ff8c00); padding: 40px; border-radius: 30px; text-align: center; color: black; box-shadow: 0 10px 30px rgba(255,215,0,0.3); }
    .pay-btn { background-color: black; color: white !important; padding: 15px 30px; border-radius: 10px; text-decoration: none; display: block; margin: 20px auto; font-family: 'Orbitron'; font-weight: bold; width: 200px; text-align:center;}
    .tg-btn { color: black !important; text-decoration: underline; font-weight: bold; font-size: 14px; text-align:center; display:block; text-decoration: none;}
    .about-box { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); padding: 30px; border-radius: 20px; line-height: 1.6; text-align: center; }
    .terminal-card { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255,215,0,0.3); border-radius: 15px; padding: 25px; }
</style>
""", unsafe_allow_html=True)

# --- 4. LOGICA NAVIGAZIONE ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

# --- 5. HOME PAGE ---
if not st.session_state['auth']:
    st.markdown('<h1 class="main-title">ZENTRADER AI</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888; letter-spacing: 4px; font-family:Inter;'>PROTECTING YOUR CAPITAL SINCE 2026</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # LOGIN AREA
    _, col_btn, _ = st.columns([1, 0.6, 1])
    with col_btn:
        with st.expander("🔑 ACCESSO RISERVATO CLIENTI"):
            u = st.text_input("User ID")
            p = st.text_input("Access Key", type="password")
            if st.button("SBLOCCA TERMINALE"):
                if u == "luca" and p == "zen2026":
                    st.session_state['auth'] = True
                    st.rerun()
                else: st.error("Accesso negato.")

    st.markdown("<br><br>", unsafe_allow_html=True)

    # SEZIONE CHI SIAMO
    st.markdown('<h2 class="section-title">La Nostra Filosofia</h2>', unsafe_allow_html=True)
    _, ab_col, _ = st.columns([0.1, 1, 0.1])
    with ab_col:
        st.markdown('<div class="about-box"><p style="font-size: 18px;"><b>ZenTrader AI</b> non è un semplice software di segnali. È un sistema di controllo del rischio. Abbiamo creato questo terminale per chi ha capito che il trading non è indovinare la direzione, ma gestire le perdite. Il nostro sistema impone un <b>Drawdown rigido del 2%</b>, garantendo la longevità del tuo account, specialmente su Prop House.</p></div>', unsafe_allow_html=True)

    # SEZIONE PREZZI
    st.markdown('<h2 class="section-title">Piani di Abbonamento</h2>', unsafe_allow_html=True)
    _, p_col, _ = st.columns([1, 1, 1])
    with p_col:
        st.markdown("""
<div class="price-card">
    <h2 style="margin:0; font-family:Orbitron; letter-spacing:1px;">ELITE ACCESS</h2>
    <h1 style="font-size: 60px; margin:10px 0;">€49<span style="font-size:20px;">/mese</span></h1>
    <ul style="list-style:none; padding:0; text-align:left; font-size:15px; margin: 25px 0;">
        <li>✔️ Calcolo Size Gold/Forex/Indici</li>
        <li>✔️ Protezione Drawdown 2%</li>
        <li>✔️ AI Sentinel News Filter</li>
        <li>✔️ TradingView Premium Integrato</li>
    </ul>
    <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=noradrenalinaa@gmail.com&item_name=ZenTrader%20AI%20Elite&amount=49.00&currency_code=EUR" target="_blank" class="pay-btn">ACQUISTA LICENZA</a>
    <a href="https://t.me/ZenTraderIA" target="_blank" class="tg-btn">Parla con un esperto su Telegram →</a>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br><br><p style='text-align:center; color:#333;'>ZenTrader AI Terminal v2.0 - Strictly for Professional Use</p>", unsafe_allow_html=True)

# --- 6. TERMINALE OPERATIVO (AREA RISERVATA) ---
else:
    st.sidebar.markdown("<h2 style='color:#ffd700; font-family:Orbitron;'>ZEN PRO</h2>", unsafe_allow_html=True)
    if st.sidebar.button("CHIUDI SESSIONE"):
        st.session_state['auth'] = False
        st.rerun()
    
    st.markdown("<h2 style='font-family:Orbitron;'>DASHBOARD OPERATIVA</h2>", unsafe_allow_html=True)
    
    col_tools, col_chart = st.columns([1, 2.8])
    
    with col_tools:
        st.markdown('<div class="terminal-card">', unsafe_allow_html=True)
        st.subheader("Configurazione Rischio")
        asset_choice = st.selectbox("Seleziona Strumento", ["XAUUSD", "EURUSD", "NAS100", "BTCUSD"])
        equity = st.number_input("Equità (€)", value=10000, step=1000)
        risk_perc = st.slider("Rischio per Trade (%)", 0.1, 2.0, 0.5)
        sl_pips = st.number_input("Stop Loss (Pips)", value=20, step=1)
        
        # Calcolo Size
        lot_size = round((equity * (risk_perc/100)) / (sl_pips * 10), 2)
        
        st.markdown("---")
        st.write("LOTTAGGIO CONSIGLIATO:")
        st.markdown(f"<h1 style='color:#ffd700; text-align:center;'>{lot_size}</h1>", unsafe_allow_html=True)
        
        if st.button("INVIA ORDINE AL BRIDGE"):
            st.toast(f"Ordine {asset_choice} pronto per l'esecuzione!")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_chart:
        # Mappa asset per TradingView
        tv_symbols = {"XAUUSD": "OANDA:XAUUSD", "EURUSD": "FX:EURUSD", "NAS100": "CAPITALCOM:US100", "BTCUSD": "BINANCE:BTCUSDT"}
        
        st.components.v1.html(f"""
            <div id="tv_chart" style="height: 600px;"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script type="text/javascript">
            new TradingView.widget({{
              "width": "100%",
              "height": 600,
              "symbol": "{tv_symbols[asset_choice]}",
              "interval": "15",
              "theme": "dark",
              "style": "1",
              "locale": "it",
              "enable_publishing": false,
              "allow_symbol_change": true,
              "container_id": "tv_chart"
            }});
            </script>
        """, height=600)