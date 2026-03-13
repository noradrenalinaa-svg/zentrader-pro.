import streamlit as st
import time

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="ZenTrader AI", layout="wide", page_icon="💎")

# --- 2. MONITORAGGIO UMAMI ---
st.markdown("""
<script defer src="https://cloud.umami.is/script.js" data-website-id="48c34484-b01f-4c2d-b606-40f648561dbc"></script>
""", unsafe_allow_html=True)

# --- 3. CSS PREMIUM ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@300;400;700&display=swap');
    .stApp { background-color: #050505; color: #fff; }
    .main-title { font-family: 'Orbitron'; font-size: clamp(40px, 8vw, 80px); text-align: center; background: linear-gradient(90deg, #ffd700, #ff8c00); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0px; animation: fadeIn 1.5s ease-in; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
    .section-title { font-family: 'Orbitron'; color: #ffd700; text-align: center; margin-top: 70px; text-transform: uppercase; letter-spacing: 3px; font-size: 24px; }
    .price-card { background: linear-gradient(145deg, #ffd700, #ff8c00); padding: 50px 40px; border-radius: 40px; text-align: center; color: black; box-shadow: 0 20px 50px rgba(255,215,0,0.1); border: 1px solid rgba(255,255,255,0.2); }
    .pay-btn { background-color: black; color: white !important; padding: 18px 35px; border-radius: 15px; text-decoration: none; display: block; margin: 25px auto; font-family: 'Orbitron'; font-weight: bold; width: fit-content; transition: 0.3s ease; border: none; }
    .pay-btn:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,0,0,0.3); }
    .about-box { background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08); padding: 40px; border-radius: 30px; text-align: center; font-family: 'Inter'; font-weight: 300; }
</style>
""", unsafe_allow_html=True)

# --- 4. LOGICA NAVIGAZIONE ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

# --- 5. HOME PAGE ---
if not st.session_state['auth']:
    st.markdown('<h1 class="main-title">ZENTRADER AI</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; letter-spacing: 5px; font-family:Inter; font-size:14px;'>ELIMINATE EMOTIONS. MAXIMIZE DISCIPLINE.</p>", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    # LOGIN AREA
    _, col_login, _ = st.columns([1, 0.8, 1])
    with col_login:
        with st.expander("🔑 PORTALE ACCESSO CLIENTI"):
            u = st.text_input("User ID")
            p = st.text_input("Access Key", type="password")
            if st.button("SBLOCCA SOFTWARE"):
                if u == "luca" and p == "zen2026":
                    st.success("Licenza Verificata.")
                    time.sleep(1)
                    st.session_state['auth'] = True
                    st.rerun()
                else: st.error("Credenziali non valide.")

    # PREZZI
    st.markdown('<h2 class="section-title">Membership Elite</h2>', unsafe_allow_html=True)
    _, p_col, _ = st.columns([1, 1, 1])
    with p_col:
        st.markdown("""
<div class="price-card">
    <h1 style="font-size: 65px; margin:10px 0; font-family:Orbitron;">€49<span style="font-size:20px;">/mese</span></h1>
    <p style="background: rgba(0,0,0,0.1); display:inline-block; padding:5px 15px; border-radius:20px; font-size:11px; font-weight:bold;">ABBONAMENTO MENSILE - RICORRENTE</p>
    <ul style="list-style:none; padding:30px 0; text-align:left; font-size:15px; font-family:Inter;">
        <li>✅ Calcolo Size Anti-Emotività</li>
        <li>✅ Protezione Drawdown 2%</li>
        <li>✅ AI News Sentinel Integrato</li>
    </ul>
    <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=noradrenalinaa@gmail.com&item_name=ZenTrader%20AI%20Elite%20Monthly&amount=49.00&currency_code=EUR" target="_self" class="pay-btn">ATTIVA ABBONAMENTO</a>
    <a href="https://t.me/ZenTraderIA" target="_self" style="color:black; text-decoration:none; font-size:12px; font-weight:bold; opacity:0.6;">Supporto Telegram →</a>
</div>
""", unsafe_allow_html=True)

    # FAQ
    st.markdown('<h2 class="section-title">Domande Frequenti</h2>', unsafe_allow_html=True)
    _, faq_col, _ = st.columns([0.2, 1, 0.2])
    with faq_col:
        with st.expander("È sicuro pagare con PayPal?"):
            st.write("Sì, usiamo il gateway sicuro di PayPal. Non memorizziamo i dati della tua carta e puoi gestire l'abbonamento in totale autonomia.")
        with st.expander("Come ricevo le credenziali?"):
            st.write("Dopo il pagamento, riceverai un'email con il tuo User ID e Access Key. Se hai fretta, puoi scriverci subito su Telegram allegando lo screenshot del pagamento.")

# --- 6. TERMINALE OPERATIVO ---
else:
    st.sidebar.markdown("<h2 style='color:#ffd700; font-family:Orbitron;'>ZEN PRO</h2>", unsafe_allow_html=True)
    if st.sidebar.button("LOGOUT"):
        st.session_state['auth'] = False
        st.rerun()
    st.info("Terminale Attivo. Buona sessione, Luca.")