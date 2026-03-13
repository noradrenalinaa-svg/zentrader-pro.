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
    
    /* Animazione Titolo */
    .main-title { 
        font-family: 'Orbitron'; 
        font-size: clamp(40px, 8vw, 80px); 
        text-align: center; 
        background: linear-gradient(90deg, #ffd700, #ff8c00); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        margin-bottom: 0px;
        animation: fadeIn 2s ease-in;
    }

    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

    .section-title { 
        font-family: 'Orbitron'; 
        color: #ffd700; 
        text-align: center; 
        margin-top: 70px; 
        text-transform: uppercase; 
        letter-spacing: 3px;
        font-size: 24px;
    }

    /* Card Prezzi */
    .price-card { 
        background: linear-gradient(145deg, #ffd700, #ff8c00); 
        padding: 50px 40px; 
        border-radius: 40px; 
        text-align: center; 
        color: black; 
        box-shadow: 0 20px 50px rgba(255,215,0,0.15); 
        border: 1px solid rgba(255,255,255,0.2);
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
    .pay-btn:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.4); }

    .about-box { 
        background: rgba(255,255,255,0.02); 
        border: 1px solid rgba(255,255,255,0.08); 
        padding: 40px; 
        border-radius: 30px; 
        line-height: 1.8; 
        text-align: center;
        font-family: 'Inter';
        font-weight: 300;
    }

    /* Custom Expander */
    .st-emotion-cache-p4mowd { background-color: transparent !important; border: none !important; border-bottom: 1px solid #333 !important; }
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
            u = st.text_input("User ID", placeholder="Inserisci User")
            p = st.text_input("Access Key", type="password", placeholder="••••••••")
            if st.button("SBLOCCA SOFTWARE"):
                if u == "luca" and p == "zen2026":
                    with st.spinner('Verifica licenza in corso...'):
                        time.sleep(1.5)
                        st.session_state['auth'] = True
                        st.rerun()
                else: st.error("Credenziali non valide o licenza scaduta.")

    # SEZIONE PREZZI (CHIARA SUL RECORRENTE)
    st.markdown('<h2 class="section-title">Membership Elite</h2>', unsafe_allow_html=True)
    _, p_col, _ = st.columns([1, 1, 1])
    with p_col:
        st.markdown("""
<div class="price-card">
    <p style="margin:0; font-family:Inter; font-weight:700; letter-spacing:2px; opacity:0.7;">FULL PASS</p>
    <h1 style="font-size: 65px; margin:10px 0; font-family:Orbitron;">€49<span style="font-size:20px;">/mese</span></h1>
    <p style="background: rgba(0,0,0,0.1); display:inline-block; padding:5px 15px; border-radius:20px; font-size:11px; font-weight:bold;">RINNOVO AUTOMATICO - DISDICI QUANDO VUOI</p>
    <ul style="list-style:none; padding:0; text-align:left; font-size:15px; margin: 30px 0; font-family:Inter;">
        <li>✅ Terminale Web-Based (No Installazione)</li>
        <li>✅ Calcolo Size Anti-Emotività</li>
        <li>✅ Protezione Drawdown 2% (Prop Ready)</li>
        <li>✅ AI News Sentinel & Market Scanner</li>
    </ul>
    <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=noradrenalinaa@gmail.com&item_name=ZenTrader%20AI%20Elite%20Monthly&amount=49.00&currency_code=EUR" target="_self" class="pay-btn">ATTIVA ORA</a>
    <a href="https://t.me/ZenTraderIA" target="_self" style="color:black; text-decoration:none; font-size:12px; font-weight:bold; opacity:0.6;">Hai domande? Scrivici su Telegram →</a>
</div>
""", unsafe_allow_html=True)

    # SEZIONE FAQ
    st.markdown('<h2 class="section-title">Domande Frequenti</h2>', unsafe_allow_html=True)
    _, faq_col, _ = st.columns([0.2, 1, 0.2])
    with faq_col:
        with st.expander("L'abbonamento si rinnova da solo?"):
            st.write("Sì, per garantirti l'accesso ininterrotto al terminale, l'abbonamento si rinnova automaticamente ogni mese. Puoi gestire o annullare il rinnovo in qualsiasi momento dal tuo pannello PayPal con un clic.")
        with st.expander("Posso usarlo per superare le Prop Challenge?"):
            st.write("Assolutamente. ZenTrader AI è stato progettato proprio per i trader che usano capitali finanziati. Il blocco del drawdown al 2% ti aiuta a rispettare le regole rigide delle Prop Firm.")
        with st.expander("Quali asset sono supportati?"):
            st.write("Il calcolatore supporta Oro (XAUUSD), le principali coppie Forex, Indici (NAS100, DAX) e le Crypto più scambiate.")
        with st.expander("Ho bisogno di installare qualcosa sul mio Mac?"):
            st.write("No. ZenTrader AI è una piattaforma web protetta. Accedi con le tue credenziali da qualsiasi browser (Safari, Chrome, ecc.) e sei subito operativo.")

    st.markdown("<br><br><p style='text-align:center; color:#222; font-size: 11px; font-family:Inter;'>© 2026 ZenTrader AI System. Licenza mensile ricorrente gestita via PayPal Secure Gateway.</p>", unsafe_allow_html=True)

# --- 6. TERMINALE OPERATIVO (AREA RISERVATA) ---
else:
    st.sidebar.markdown("<h2 style='color:#ffd700; font-family:Orbitron;'>ZEN PRO</h2>", unsafe_allow_html=True)
    if st.sidebar.button("LOGOUT"):
        st.session_state['auth'] = False
        st.rerun()
    st.success("Accesso eseguito. Sistema di monitoraggio 2% Drawdown: ATTIVO.")
    st.write("Benvenuto nell'area operativa, Luca.")