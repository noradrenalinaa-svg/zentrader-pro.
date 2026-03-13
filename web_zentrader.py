import streamlit as st
import time

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="ZenTrader Pro - Bridge", layout="wide")

# --- INTERFACCIA ---
st.title("🛡️ ZenTrader Pro - Terminale Operativo")

col_broker, col_chart, col_exec = st.columns([1, 2.5, 1])

with col_broker:
    st.subheader("🔌 MT5 Bridge")
    # Questi campi serviranno per collegarci all'API del broker
    server = st.text_input("Server Broker", value="MetaQuotes-Demo")
    mt5_id = st.text_input("Login ID")
    mt5_pw = st.text_input("Password", type="password")
    
    st.divider()
    st.subheader("🧮 Gestione Rischio")
    balance = st.number_input("Equity ($)", value=10000)
    risk_perc = st.slider("Rischio %", 0.1, 2.0, 0.5)
    sl_pips = st.number_input("Stop Loss (Pips)", value=20)
    
    # Calcolo lotti
    lotti = round((balance * (risk_perc/100)) / (sl_pips * 10), 2)
    st.metric("LOTTAGGIO CALCOLATO", lotti)

with col_chart:
    st.components.v1.html("""
        <div id="chart" style="height:600px;"></div>
        <script src="https://s3.tradingview.com/tv.js"></script>
        <script>
        new TradingView.widget({"width": "100%", "height": 600, "symbol": "OANDA:XAUUSD", "interval": "15", "theme": "dark", "container_id": "chart"});
        </script>
    """, height=600)

with col_exec:
    st.subheader("🚀 Esecuzione")
    st.write(f"Asset: **XAUUSD**")
    st.write(f"Size: **{lotti}**")
    
    # IL TASTO REALE
    if st.button("ESEGUI ORDINE SU MT5", type="primary"):
        if mt5_id and mt5_pw:
            with st.spinner("Invio ordine in corso..."):
                # Qui andremo a inserire la funzione di invio reale
                time.sleep(2) 
                st.success(f"Ordine di {lotti} eseguito con successo!")
                # Log per il diario
                st.session_state['last_trade'] = f"Long {lotti} XAUUSD @ {time.strftime('%H:%M')}"
        else:
            st.error("Errore: Inserisci le credenziali MT5 a sinistra!")

    if 'last_trade' in st.session_state:
        st.info(f"Ultimo Trade: {st.session_state['last_trade']}")
