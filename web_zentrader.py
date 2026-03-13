import streamlit as st
import time

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="ZenTrader AI", layout="wide", page_icon="💎")

# --- 2. MONITORAGGIO UMAMI ---
st.markdown("""
<script defer src="https://cloud.umami.is/script.js" data-website-id="48c34484-b01f-4c2d-b606-40f648561dbc"></script>
""", unsafe_allow_html=True)

# --- 3. CSS PREMIUM COMPLETO ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@300;400;700&display=swap');
    
    .stApp { background-color: #050505; color: #fff; }
    
    .main-title { 
        font-family: 'Orbitron'; 
        font-size: clamp(40px, 8vw, 80px); 
        text-align: center; 
        background: linear-gradient(90deg, #ffd700, #ff8c00); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        margin-bottom: 0px;
    }

    .section-title { 
        font-family: 'Orbitron'; 
        color: #ffd700; 
        text-align: center; 
        margin-top: 70px; 
        text-transform: uppercase; 
        letter-spacing: 3px;
        font-size: 24px;
    }

    /* Card Recensioni */
    .review-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 215, 0, 0.1);
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 20px;
        height: 100%;
    }
    .review-text { font-family: 'Inter'; font-style: italic; color: #ccc; font-size: 14px; }
    .review-author { font-family: 'Orbitron'; color: #ffd700; font-size: 12px; margin-top: 15px; display: block; }

    /* Card Prezzi */
    .price-card { 
        background: linear-gradient(145deg, #ffd700, #ff8c00); 
        padding: 50px 40px; 
        border-radius: 40px; 
        text-align: center; 
        color: black; 
        box-shadow: 0 20px 50px rgba(255,215,0,0.15);
    }

    .pay-btn { 
        background-color: black; 
        color: white !important; 
        padding: 18px 35px; 
        border-radius: 15px; 
        text-decoration: none; 
        display: block; 
        margin: 25px auto; 
        font-family: 'Orbitron'; 
        font-weight: bold; 
        width: fit-content;
        transition: 0.4s ease;
    }
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
                    st.session_state['auth'] = True
                    st.rerun()
                else: st.error("Credenziali non valide.")

    # SEZIONE RECENSIONI
    st.markdown('<h2 class="section-title">Cosa dicono i Trader</h2>', unsafe_allow_html=True)
    rev1, rev2, rev3 = st.columns(3)
    with rev1:
        st.markdown('<div class="review-card"><span class="review-text">"Finalmente un calcolatore serio. Da quando uso ZenTrader non ho più sforato il rischio su FTMO. Il blocco del drawdown è un salvavita."</span><span class="review-author">- Marco T. (Prop Trader)</span></div>', unsafe_allow_html=True)
    with rev2:
        st.markdown('<div class="review-card"><span class="review-text">"Interfaccia pulitissima sul mio Mac. In 2 secondi so quanto aprire di size sull\'oro. Vale ogni centesimo dell\'abbonamento."</span><span class="review-author">- Andrea L.</span></div>', unsafe_allow_html=True)
    with rev3:
        st.markdown('<div class="review-card"><span class="review-text">"L\'AI Sentinel mi ha salvato da tre news ad alto impatto questo mese. Indispensabile per chi cerca costanza."</span><span class="review-author">- Giulia R.</span></div>', unsafe_allow_html=True)

    # SEZIONE PREZZI
    st.markdown('<h2 class="section-title">Membership Elite</h2>', unsafe_allow_html=True)
    _, p_col, _ = st.columns([1, 1, 1])
    with p_col:
        st.markdown("""
<div class="price-card">
    <h1 style="font-size: 65px; margin:10px 0; font-family:Orbitron;">€49<span style="font-size:20px;">/mese</span></h1>
    <p style="background: rgba(0,0,0,0.1); display:inline-block; padding:5px 15px; border-radius:20px; font-size:11px; font-weight:bold;">ABBONAMENTO MENSILE RICORRENTE</p>
    <ul style="list-style:none; padding:30px 0; text-align:left; font-size:15px; font-family:Inter;">
        <li>✅ Calcolo Size Anti-Emotività</li>
        <li>✅ Protezione Drawdown 2%</li>
        <li>✅ AI News Sentinel (Real-time)</li>
        <li>✅ Accesso Terminale Web Pro</li>
    </ul>
    <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=noradrenalinaa@gmail.com&item_name=ZenTrader%20AI%20Elite%20Monthly&amount=49.00&currency_code=EUR" target="_self" class="pay-btn">ATTIVA ABBONAMENTO</a>
    <p style="font-size: 10px; color: black; opacity: 0.7;">Disdici in qualsiasi momento via PayPal</p>
</div>
""", unsafe_allow_html=True)

    # SEZIONE FAQ (RIPRISTINATA COMPLETA)
    st.markdown('<h2 class="section-title">Domande Frequenti</h2>', unsafe_allow_html=True)
    _, faq_col, _ = st.columns([0.1, 1, 0.1])
    with faq_col:
        with st.expander("L'abbonamento si rinnova da solo?"):
            st.write("Sì, per garantirti l'accesso ininterrotto, l'abbonamento si rinnova automaticamente ogni 30 giorni. Puoi annullarlo quando vuoi con un clic dal tuo conto PayPal.")
        with st.expander("Posso usarlo per le Prop Challenge?"):
            st.write("Certamente. Il sistema è ottimizzato per chi deve rispettare regole rigide di gestione del rischio (come il drawdown giornaliero).")
        with st.expander("Quali asset posso calcolare?"):
            st.write("Oro (XAUUSD), le principali coppie Forex (EURUSD, GBPUSD, ecc.), Indici (NAS100, US30) e le principali Crypto.")
        with st.expander("Devo installare software sul Mac?"):
            st.write("No, ZenTrader AI è un terminale cloud. Ti basta il browser del tuo MacBook per essere operativo ovunque.")
        with st.expander("È sicuro il pagamento?"):
            st.write("Usiamo PayPal, il sistema più sicuro al mondo. I tuoi dati finanziari non passano mai dai nostri server.")
        with st.expander("Cosa ricevo dopo il pagamento?"):
            st.write("Riceverai immediatamente via email le tue credenziali (User ID e Access Key) per sbloccare il terminale su questo sito.")

    st.markdown("<br><br><p style='text-align:center; color:#333; font-size: 11px;'>© 2026 ZenTrader AI System. Licenza mensile ricorrente.</p>", unsafe_allow_html=True)

# --- 6. TERMINALE OPERATIVO ---
else:
    st.sidebar.markdown("<h2 style='color:#ffd700; font-family:Orbitron;'>ZEN PRO</h2>", unsafe_allow_html=True)
    if st.sidebar.button("LOGOUT"):
        st.session_state['auth'] = False
        st.rerun()
    st.info("Accesso Eseguito. Buona sessione, Luca.")