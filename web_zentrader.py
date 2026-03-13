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
    
    .main-title { 
        font-family: 'Orbitron'; 
        font-size: clamp(40px, 8vw, 80px); 
        text-align: center; 
        background: linear-gradient(90deg, #ffd700, #ff8c00); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        margin-bottom: 5px;
    }

    /* PULSANTE LOGIN SPOSTATO A DESTRA */
    .stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: #ffd700 !important;
        border: 1px solid #ffd700 !important;
        border-radius: 50px !important;
        padding: 10px 40px !important;
        font-family: 'Orbitron' !important;
        letter-spacing: 2px !important;
        transition: 0.4s all !important;
        float: right; 
    }
    
    .stButton > button:hover {
        background: #ffd700 !important;
        color: black !important;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.4) !important;
    }

    .login-box {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        margin-top: 60px;
        clear: both;
    }

    .section-title { 
        font-family: 'Orbitron'; 
        color: #ffd700; 
        text-align: center; 
        margin-top: 80px; 
        text-transform: uppercase; 
        letter-spacing: 3px;
        font-size: 20px;
    }

    .review-card {
        background: rgba(255, 255, 255, 0.02);
        padding: 25px;
        border-radius: 20px;
        height: 100%;
        border: 1px solid rgba(255,255,255,0.05);
    }

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
    }
</style>
""", unsafe_allow_html=True)

# --- 4. LOGICA NAVIGAZIONE ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

# --- 5. HOME PAGE ---
if not st.session_state['auth']:
    st.markdown('<h1 class="main-title">ZENTRADER AI</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; letter-spacing: 5px; font-family:Inter; font-size:14px; margin-bottom:30px;'>ELIMINATE EMOTIONS. MAXIMIZE DISCIPLINE.</p>", unsafe_allow_html=True)
    
    # PULSANTE ACCESSO (SPOSTATO A DESTRA CON COLONNE 1.2, 1, 0.8)
    _, col_btn, col_spacer = st.columns([1.2, 1, 0.8])
    with col_btn:
        if 'show_login' not in st.session_state:
            st.session_state.show_login = False
        if st.button("ACCEDI AL TERMINALE"):
            st.session_state.show_login = not st.session_state.show_login

    if st.session_state.show_login:
        _, col_login, _ = st.columns([1, 1.5, 1])
        with col_login:
            st.markdown('<div class="login-box">', unsafe_allow_html=True)
            u = st.text_input("User ID", placeholder="Username")
            p = st.text_input("Access Key", type="password", placeholder="Password")
            if st.button("SBLOCCA ORA"):
                if u == "luca" and p == "zen2026":
                    st.session_state['auth'] = True
                    st.rerun()
                else:
                    st.error("Credenziali errate")
            st.markdown('</div>', unsafe_allow_html=True)

    # RECENSIONI
    st.markdown('<h2 class="section-title">Trader Experiences</h2>', unsafe_allow_html=True)
    rev1, rev2, rev3 = st.columns(3)
    with rev1:
        st.markdown('<div class="review-card"><p style="font-style:italic; color:#bbb; font-size:14px;">"Il drawdown al 2% è una garanzia assoluta per chi fa Prop Trading."</p><b style="color:#ffd700; font-family:Orbitron; font-size:11px;">MARCO T.</b></div>', unsafe_allow_html=True)
    with rev2:
        st.markdown('<div class="review-card"><p style="font-style:italic; color:#bbb; font-size:14px;">"Calcolo size istantaneo sul mio Mac. Mai più errori manuali."</p><b style="color:#ffd700; font-family:Orbitron; font-size:11px;">ANDREA L.</b></div>', unsafe_allow_html=True)
    with rev3:
        st.markdown('<div class="review-card"><p style="font-style:italic; color:#bbb; font-size:14px;">"L\'AI Sentinel mi ha salvato da news pesanti. Indispensabile."</p><b style="color:#ffd700; font-family:Orbitron; font-size:11px;">GIULIA R.</b></div>', unsafe_allow_html=True)

    # PREZZI
    st.markdown('<h2 class="section-title">Membership Elite</h2>', unsafe_allow_html=True)
    _, p_col, _ = st.columns([1, 1, 1])
    with p_col:
        st.markdown("""
<div class="price-card">
    <h1 style="font-size: 60px; margin:10px 0; font-family:Orbitron;">€49<span style="font-size:18px;">/mese</span></h1>
    <p style="font-size:11px; font-weight:bold; letter-spacing:1px; color:rgba(0,0,0,0.6);">ABBONAMENTO MENSILE - RICORRENTE</p>
    <ul style="list-style:none; padding:20px 0; text-align:left; font-size:14px; font-family:Inter; color:black;">
        <li>✅ Pro Shield Drawdown (2%)</li>
        <li>✅ Instant Size Calculator</li>
        <li>✅ AI News Sentinel Filter</li>
    </ul>
    <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=noradrenalinaa@gmail.com&item_name=ZenTrader%20AI%20Elite%20Monthly&amount=49.00&currency_code=EUR" target="_self" class="pay-btn">START NOW</a>
    <p style="font-size:10px; color:black; opacity:0.6;">Disdici in qualsiasi momento via PayPal</p>
</div>
""", unsafe_allow_html=True)

    # FAQ (RIPRISTINATE TUTTE)
    st.markdown('<h2 class="section-title">Domande Frequenti</h2>', unsafe_allow_html=True)
    _, faq_col, _ = st.columns([0.2, 1, 0.2])
    with faq_col:
        with st.expander("L'abbonamento si rinnova da solo?"):
            st.write("Sì, il rinnovo è automatico ogni 30 giorni. Puoi gestire o disdire l'abbonamento in totale autonomia dal tuo account PayPal.")
        with st.expander("Posso usarlo per superare le Prop Challenge?"):
            st.write("Certamente. ZenTrader AI è progettato per aiutare i trader a rispettare i limiti di rischio delle Prop Firm, mantenendo il drawdown sotto controllo.")
        with st.expander("Quali asset sono supportati?"):
            st.write("Il sistema supporta Oro (XAUUSD), le principali coppie Forex, Indici (NAS100, US30) e le Crypto più scambiate.")
        with st.expander("Serve installare qualcosa sul mio Mac?"):
            st.write("No. È un terminale web-based. Accedi con le tue credenziali da Safari o Chrome e sei subito pronto a operare.")
        with st.expander("Come ricevo i dati di accesso?"):
            st.write("Subito dopo il pagamento riceverai un'email con il tuo User ID e la tua Access Key personale.")

    st.markdown("<br><br><p style='text-align:center; color:#222; font-size: 10px;'>ZenTrader AI System 2026. Secure Algorithm Trading.</p>", unsafe_allow_html=True)

# --- 6. TERMINALE OPERATIVO (DOPO LOGIN) ---
else:
    st.sidebar.markdown("<h2 style='color:#ffd700; font-family:Orbitron;'>ZEN PRO</h2>", unsafe_allow_html=True)
    if st.sidebar.button("LOGOUT"):
        st.session_state['auth'] = False
        st.rerun()
    st.info("System Online. Protection Active.")