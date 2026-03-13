import streamlit as st
import time

# --- 1. CONFIGURAZIONE PAGINA (Importante per il layout wide) ---
st.set_page_config(page_title="ZenTrader AI - Smetti di perdere", layout="wide")

# --- 2. CSS CUSTOM "GLASSDESIGN" (Tutto nuovo) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&display=swap');
    
    /* SFONDO NERO ASSOLUTO E PULIZIA UI STREAMLIT */
    .stApp { background: #000000; color: #ffffff; font-family: 'Inter', sans-serif; }
    header, [data-testid="stSidebar"], [data-testid="stToolbar"] { visibility: hidden !important; height: 0px !important; }
    .stMainBlockContainer { padding-top: 50px !important; }
    
    /* HERO TITLE E SUBTITLE (In stile Apple) */
    .hero-title { font-size: clamp(35px, 6vw, 65px); font-weight: 900; text-align: center; color: #ffffff; padding-top: 60px; margin-bottom: 0px; }
    .hero-sub { font-size: clamp(16px, 2.5vw, 22px); text-align: center; color: #ffd700; margin-top: -10px; margin-bottom: 70px; font-weight: 300; letter-spacing: 2px; }
    
    /* GLASS CARD DESIGN (La nostra card trasparente con bordi luminosi) */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        transition: 0.3s all;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        height: 100%;
        display: flex; flex-direction: column; align-items: center; justify-content: start;
    }
    .glass-card:hover { 
        border: 1px solid #ffd70044; 
        box-shadow: 0 10px 40px rgba(255, 215, 0, 0.05); 
        transform: translateY(-5px);
    }
    
    .feature-icon { font-size: 45px; margin-bottom: 25px; color: #ffd700; }
    .feature-title { font-size: 24px; font-weight: 700; color: #ffffff; margin-bottom: 10px; }
    .feature-text { font-size: 14px; color: #888888; line-height: 1.6; }
    
    /* PREZZO E CTA (Stile Elite) */
    .cta-area { text-align: center; margin-top: 80px; margin-bottom: 80px; }
    .price-tag { font-size: clamp(40px, 5vw, 60px); font-weight: 900; color: #ffffff; margin-bottom: -10px; }
    
    /* PULSANTE CANCELLATO STREAMLIT -> CREIAMO PULSANTE CUSTOM NELLA CTA */
    .custom-cta-btn {
        background: #ffffff; color: #000000;
        font-weight: 700; font-size: 20px;
        padding: 20px 60px; border-radius: 50px;
        text-decoration: none; transition: 0.3s;
        box-shadow: 0 10px 30px rgba(255, 255, 255, 0.1);
    }
    .custom-cta-btn:hover { background: #ffd700; color: #000; box-shadow: 0 10px 40px rgba(255, 215, 0, 0.3); }

    /* LOGIN BOX PULITA */
    .login-box {
        background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.05);
        border-radius: 20px; padding: 40px;
        width: 100%; max-width: 400px; margin: 0 auto; margin-top: 100px;
    }
    /* Sostituiamo gli input di Streamlit con stili più puliti via CSS */
    [data-testid="stForm"] { border: none !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DI STATO E NAVIGAZIONE ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    # --- LANDING PAGE (Sopra-Login) ---
    st.markdown('<h1 class="hero-title">ZenTrader AI Terminal</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub">L\'unica infrastruttura che blinda il tuo capitale e automatizza il tuo rischio.</p>', unsafe_allow_html=True)
    
    # Sezione 3 Pilastri (Allineate perfettamente)
    col1, col2, col3 = st.columns([1, 1, 1], gap="large")
    with col1:
        st.markdown('<div class="glass-card"><div class="feature-icon">📊</div><div class="feature-title">Analisi Pura</div><div class="feature-text">Grafico TradingView Pro integrato con AI Trend Scanner. Analizza senza distrazioni ed elimina il noise del mercato.</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="glass-card" style="border: 1px solid #ffd70044; background: rgba(255, 215, 0, 0.01);"><div class="feature-icon">🛡️</div><div class="feature-title" style="color:#ffd700;">Rischio Blindato</div><div class="feature-text">Calcolo automatico della size. Il sistema ti impedisce fisicamente di superare il tuo drawdown giornaliero del 2%.</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="glass-card"><div class="feature-icon">⚡</div><div class="feature-title">Esecuzione MT5</div><div class="feature-text">Invia l\'ordine direttamente a MetaTrader con un click. Velocità istituzionale senza stress emotivo.</div></div>', unsafe_allow_html=True)

    # Sezione Prezzo e CTA (Tutto concentrato e pulito)
    st.markdown('<div style="height:50px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="cta-area">', unsafe_allow_html=True)
    st.markdown('<p class="metric-label" style="text-transform:uppercase; color:#888; letter-spacing:3px;">MEMBERSHIP PRO</p>', unsafe_allow_html=True)
    st.markdown('<p class="price-tag">€49 <span style="font-size:16px; color:#555; font-weight:400;">/ mese</span></p>', unsafe_allow_html=True)
    st.markdown('<div style="height:30px;"></div>', unsafe_allow_html=True)
    # TASTO CUSTOM CON PAYPAL LINK (Simulato)
    st.markdown('<a href="https://paypal.me/tuolink" class="custom-cta-btn">ATTIVA ORA</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- SEZIONE LOGIN MINIMALISTA ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    _, login_col, _ = st.columns([1, 1, 1])
    with login_col:
        with st.form("Login Form", clear_on_submit=True):
            st.markdown('<p class="stat-label" style="text-align:center; color:#555;">MEMBERS ACCESS</p>', unsafe_allow_html=True)
            u = st.text_input("Username", placeholder="Username...", label_visibility="collapsed")
            p = st.text_input("Password", type="password", placeholder="Password...", label_visibility="collapsed")
            # Pulsante Streamlit nascosto e sostituito da uno custom via CSS (Simulato per semplicità qui)
            submitted = st.form_submit_with_label("ENTRA NEL TERMINALE")
            if submitted:
                if u == "luca" and p == "zen2026":
                    st.session_state['auth'] = True
                    st.rerun()
                else:
                    st.error("Credenziali Errate")

else:
    # --- IL TERMINALE (Quando Luca è loggato) ---
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update({"auth": False}))
    st.title("Bentornato Luca. Il sistema è pronto.")
    st.write("Esecuzione Grafico e Broker in corso...")
    # ... qui rimetteremo il terminale con le 3 colonne che ti piacevano
