import streamlit as st
import time

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="ZenTrader AI", layout="wide", page_icon="💎")

# --- 2. MONITORAGGIO UMAMI ---
st.markdown("""
<script defer src="https://cloud.umami.is/script.js" data-website-id="48c34484-b01f-4c2d-b606-40f648561dbc"></script>
""", unsafe_allow_html=True)

# --- 3. CSS PREMIUM AVANZATO ---
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
        margin-bottom: 10px;
    }

    /* NUOVA GRAFICA PORTALE ACCESSO */
    .login-container {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 215, 0, 0.3);
        border-radius: 25px;
        padding: 40px;
        backdrop-filter: blur(10px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
        text-align: center;
        margin-bottom: 50px;
    }
    
    .login-header {
        font-family: 'Orbitron';
        color: #ffd700;
        font-size: 18px;
        letter-spacing: 2px;
        margin-bottom: 25px;
        display: block;
    }

    .section-title { 
        font-family: 'Orbitron'; 
        color: #ffd700; 
        text-align: center; 
        margin-top: 80px; 
        text-transform: uppercase; 
        letter-spacing: 3px;
        font-size: 22px;
    }

    /* Recensioni */
    .review-card {
        background: rgba(255, 255, 255, 0.02);
        border-left: 3px solid #ffd700;
        padding: 20px;
        border-radius: 0 15px 15px 0;
        height: 100%;
    }

    /* Card Prezzi */
    .price-card { 
        background: linear-gradient(145deg, #ffd700, #ff8c00); 
        padding: 50px 40px; 
        border-radius: 40px; 
        text-align: center; 
        color: black; 
        box-shadow: 0 20px 50px rgba(255,215,0,0.2);
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
    
    /* Input Fields Styling */
    .stTextInput input {
        background-color: rgba(255,255,255,0.05) !important;
        color: white !important;
        border: 1px solid rgba(255,215,0,0.2) !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. LOGICA NAVIGAZIONE ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

# --- 5. HOME PAGE ---
if not st.session_state['auth']:
    st.markdown('<h1 class="main-title">ZENTRADER AI</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; letter-spacing: 5px; font-family:Inter; font-size:14px; margin-bottom:40px;'>ELIMINATE EMOTIONS. MAXIMIZE DISCIPLINE.</p>", unsafe_allow_html=True)
    
    # NUOVO PORTALE ACCESSO GRAFICO
    _, col_login, _ = st.columns([1, 1.2, 1])
    with col_login:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown('<span class="login-header">🔐 SECURITY CHECK</span>', unsafe_allow_html=True)
        u = st.text_input("USER ID", placeholder="Username", label_visibility="collapsed")
        p = st.text_input("ACCESS KEY", type="password", placeholder="Password", label_visibility="collapsed")
        if st.button("UNLOCK TERMINAL", use_container_width=True):
            if u == "luca" and p == "zen2026":
                with st.spinner('Accessing encrypted core...'):
                    time.sleep(1.5)
                    st.session_state['auth'] = True
                    st.rerun()
            else:
                st.error("Invalid Credentials")
        st.markdown('</div>', unsafe_allow_html=True)

    # SEZIONE RECENSIONI
    st.markdown('<h2 class="section-title">Trader Experiences</h2>', unsafe_allow_html=True)
    rev1, rev2, rev3 = st.columns(3)
    with rev1:
        st.markdown('<div class="review-card"><p style="font-style:italic; color:#bbb;">"Il blocco del drawdown al 2% è la funzione che mi ha permesso di passare la mia prima Prop."</p><b style="color:#ffd700; font-family:Orbitron; font-size:10px;">MARCO T.</b></div>', unsafe_allow_html=True)
    with rev2:
        st.markdown('<div class="review-card"><p style="font-style:italic; color:#bbb;">"Rapido, pulito e matematico. Sul Mac gira che è una meraviglia."</p><b style="color:#ffd700; font-family:Orbitron; font-size:10px;">ANDREA L.</b></div>', unsafe_allow_html=True)
    with rev3:
        st.markdown('<div class="review-card"><p style="font-style:italic; color:#bbb;">"Niente più calcoli manuali mentre il prezzo scappa. Indispensabile."</p><b style="color:#ffd700; font-family:Orbitron; font-size:10px;">GIULIA R.</b></div>', unsafe_allow_html=True)

    # SEZIONE PREZZI
    st.markdown('<h2 class="section-title">Elite Membership</h2>', unsafe_allow_html=True)
    _, p_col, _ = st.columns([1, 1, 1])
    with p_col:
        st.markdown("""
<div class="price-card">
    <h1 style="font-size: 65px; margin:10px 0; font-family:Orbitron;">€49<span style="font-size:20px;">/mese</span></h1>
    <p style="font-size:11px; font-weight:bold; letter-spacing:1px; color:rgba(0,0,0,0.6);">RICORRENTE - CANCEL ANYTIME</p>
    <ul style="list-style:none; padding:20px 0; text-align:left; font-size:14px; font-family:Inter;">
        <li>✅ Pro Shield Drawdown (2%)</li>
        <li>✅ Instant Size Calculator</li>
        <li>✅ AI News Sentinel Filter</li>
        <li>✅ No Installation Required</li>
    </ul>
    <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=noradrenalinaa@gmail.com&item_name=ZenTrader%20AI%20Elite%20Monthly&amount=49.00&currency_code=EUR" target="_self" class="pay-btn">START NOW</a>
    <a href="https://t.me/ZenTraderIA" target="_self" style="color:black; text-decoration:none; font-size:12px; font-weight:bold; opacity:0.5;">Supporto Telegram →</a>
</div>
""", unsafe_allow_html=True)

    # FAQ
    st.markdown('<h2 class="section-title">F.A.Q.</h2>', unsafe_allow_html=True)
    _, faq_col, _ = st.columns([0.2, 1, 0.2])
    with faq_col:
        with st.expander("Come funziona l'abbonamento?"):
            st.write("Pagamento mensile automatico via PayPal. Puoi disdire con un clic dal tuo account in ogni momento.")
        with st.expander("Quali asset supporta?"):
            st.write("Oro, Forex, Indici e Crypto. Tutto ciò che serve a un trader moderno.")
        with st.expander("Sicurezza dati?"):
            st.write("I tuoi dati di pagamento sono gestiti interamente da PayPal. Noi non memorizziamo mai le tue carte.")

    st.markdown("<br><br><p style='text-align:center; color:#222; font-size: 10px;'>ZenTrader AI System 2026. Secure Algorithm Trading.</p>", unsafe_allow_html=True)

# --- 6. TERMINALE OPERATIVO ---
else:
    st.sidebar.markdown("<h2 style='color:#ffd700; font-family:Orbitron;'>ZEN PRO</h2>", unsafe_allow_html=True)
    if st.sidebar.button("LOGOUT"):
        st.session_state['auth'] = False
        st.rerun()
    st.info("System Online. Protection Active.")