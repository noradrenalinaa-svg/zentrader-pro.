import streamlit as st

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="ZenTrader AI", layout="wide", page_icon="💎")

# --- 2. MONITORAGGIO UMAMI ---
st.markdown("""
<script defer src="https://cloud.umami.is/script.js" data-website-id="48c34484-b01f-4c2d-b606-40f648561dbc"></script>
""", unsafe_allow_html=True)

# --- 3. CSS PREMIUM + FAQ ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@400;700&display=swap');
    .stApp { background-color: #050505; color: #fff; }
    .main-title { font-family: 'Orbitron'; font-size: 70px; text-align: center; background: linear-gradient(90deg, #ffd700, #ff8c00); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0px;}
    .section-title { font-family: 'Orbitron'; color: #ffd700; text-align: center; margin-top: 60px; text-transform: uppercase; letter-spacing: 2px; }
    .price-card { background: linear-gradient(145deg, #ffd700, #ff8c00); padding: 40px; border-radius: 30px; text-align: center; color: black; box-shadow: 0 10px 30px rgba(255,215,0,0.3); position: relative; }
    .pay-btn { background-color: black; color: white !important; padding: 15px 30px; border-radius: 10px; text-decoration: none; display: block; margin: 20px auto; font-family: 'Orbitron'; font-weight: bold; width: 220px; text-align:center; transition: 0.3s; border: none;}
    .pay-btn:hover { transform: scale(1.05); cursor: pointer;}
    .tg-btn { color: black !important; font-weight: bold; font-size: 14px; text-align:center; display:block; text-decoration: none; margin-top: 10px;}
    .about-box { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); padding: 30px; border-radius: 20px; line-height: 1.6; text-align: center; }
    
    /* FAQ Styling */
    .st-emotion-cache-p4mowd { background-color: rgba(255,255,255,0.03) !important; border: 1px solid rgba(255,255,255,0.1) !important; border-radius: 10px !important; }
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

    # SEZIONE PREZZI
    st.markdown('<h2 class="section-title">Piani di Abbonamento</h2>', unsafe_allow_html=True)
    _, p_col, _ = st.columns([1, 1, 1])
    with p_col:
        st.markdown("""
<div class="price-card">
    <h2 style="margin:0; font-family:Orbitron; letter-spacing:1px;">ELITE ACCESS</h2>
    <h1 style="font-size: 60px; margin:10px 0;">€49<span style="font-size:20px;">/mese</span></h1>
    <p style="font-size: 12px; font-weight: bold; text-transform: uppercase; margin-bottom: 20px;">Abbonamento mensile a rinnovo automatico</p>
    <ul style="list-style:none; padding:0; text-align:left; font-size:15px; margin: 20px 0;">
        <li>✔️ Calcolo Size Gold/Forex/Indici</li>
        <li>✔️ Protezione Drawdown 2%</li>
        <li>✔️ AI Sentinel News Filter</li>
    </ul>
    <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=noradrenalinaa@gmail.com&item_name=ZenTrader%20AI%20Monthly%20Subscription&amount=49.00&currency_code=EUR" target="_self" class="pay-btn">ATTIVA ABBONAMENTO</a>
    <p style="font-size: 10px; margin-top: -10px;">Puoi disdire in qualsiasi momento dal tuo conto PayPal</p>
    <a href="https://t.me/ZenTraderIA" target="_self" class="tg-btn">Contatta il Fondatore</a>
</div>
""", unsafe_allow_html=True)

    # SEZIONE CHI SIAMO
    st.markdown('<h2 class="section-title">La Nostra Filosofia</h2>', unsafe_allow_html=True)
    _, ab_col, _ = st.columns([0.1, 1, 0.1])
    with ab_col:
        st.markdown('<div class="about-box"><p style="font-size: 18px;"><b>ZenTrader AI</b> è un sistema di controllo del rischio matematico. Abbiamo creato questo terminale per imporre un <b>Drawdown rigido del 2%</b>, garantendo la longevità del tuo account e il superamento delle Prop Challenges.</p></div>', unsafe_allow_html=True)

    # SEZIONE FAQ
    st.markdown('<h2 class="section-title">F.A.Q.</h2>', unsafe_allow_html=True)
    _, faq_col, _ = st.columns([0.1, 1, 0.1])
    with faq_col:
        with st.container():
            with st.expander("Come funziona l'abbonamento?"):
                st.write("L'abbonamento costa 49€ al mese e ti dà accesso illimitato al terminale. Il rinnovo è automatico ogni 30 giorni per garantirti il servizio senza interruzioni.")
            with st.expander("Posso disdire quando voglio?"):
                st.write("Assolutamente sì. Puoi interrompere il rinnovo automatico in qualsiasi momento direttamente dalle impostazioni del tuo conto PayPal o contattando il nostro supporto.")
            with st.expander("Il software funziona su Mac?"):
                st.write("Sì, ZenTrader AI è un terminale web-based. Funziona perfettamente su Safari, Chrome e tutti i browser del tuo MacBook, senza dover installare nulla.")
            with st.expander("Cosa succede se raggiungo il 2% di drawdown?"):
                st.write("Il sistema ti avviserà visivamente e bloccherà il calcolo delle nuove size per la sessione corrente, proteggendo il tuo capitale da ulteriori perdite emotive.")

    st.markdown("<br><br><p style='text-align:center; color:#333; font-size: 10px;'>ZenTrader AI Terminal v2.1. L'abbonamento può essere gestito tramite PayPal.</p>", unsafe_allow_html=True)

# --- 6. TERMINALE OPERATIVO (AREA RISERVATA) ---
else:
    st.sidebar.markdown("<h2 style='color:#ffd700; font-family:Orbitron;'>ZEN PRO</h2>", unsafe_allow_html=True)
    if st.sidebar.button("CHIUDI SESSIONE"):
        st.session_state['auth'] = False
        st.rerun()
    st.info("Benvenuto nel Terminale Operativo.")
    st.write("Software pronto.")