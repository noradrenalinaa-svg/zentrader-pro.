import streamlit as st
import time

# --- 1. CONFIGURAZIONE ---
st.set_page_config(page_title="ZenTrader AI - Smetti di perdere", layout="wide")

# --- 2. CSS PER LA PAGINA DI VENDITA ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
    .stApp { background: #050505; color: #fff; font-family: 'Inter', sans-serif; }
    
    .hero-title { font-size: 55px; font-weight: 800; text-align: center; background: linear-gradient(90deg, #ffd700, #ff8c00); -webkit-background-clip: text; -webkit-text-fill-color: transparent; padding-top: 50px; }
    .hero-sub { font-size: 20px; text-align: center; color: #888; margin-bottom: 50px; }
    
    .feature-card { background: #111; border: 1px solid #222; border-radius: 15px; padding: 30px; text-align: center; height: 100%; }
    .feature-icon { font-size: 40px; margin-bottom: 15px; }
    .price-tag { font-size: 48px; font-weight: 800; color: #ffd700; text-align: center; margin: 30px 0; }
    
    .cta-button > button { 
        background: #ffd700 !important; color: #000 !important; font-weight: bold !important; 
        font-size: 20px !important; width: 100%; height: 60px; border-radius: 10px !important;
    }
    .login-box { background: #0a0a0a; border: 1px solid #1a1a1a; padding: 20px; border-radius: 10px; margin-top: 50px; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DI NAVIGAZIONE ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    # --- LANDING PAGE ---
    st.markdown('<h1 class="hero-title">ZenTrader AI Terminal</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub">L\'unica infrastruttura che blinda il tuo capitale e automatizza il tuo rischio.</p>', unsafe_allow_html=True)
    
    # Sezione 3 Pilastri
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="feature-card"><div class="feature-icon">📊</div><h3>Analisi Pura</h3><p>Grafico TradingView Pro integrato con AI Trend Scanner. Analizza senza distrazioni.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="feature-card"><div class="feature-icon">🛡️</div><h3>Rischio Blindato</h3><p>Calcolo automatico della size. Il sistema ti impedisce di superare il tuo drawdown del 2%.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="feature-card"><div class="feature-icon">⚡</div><h3>Esecuzione MT5</h3><p>Invia l\'ordine direttamente a MetaTrader con un click. Velocità istituzionale.</p></div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Sezione Prezzo e Login
    c_pay, c_spacer, c_login = st.columns([1.5, 0.5, 1])
    
    with c_pay:
        st.markdown('<div class="feature-card" style="border: 2px solid #ffd70033;">', unsafe_allow_html=True)
        st.markdown("### Membership Pro")
        st.markdown('<p class="price-tag">49€<span style="font-size:18px; color:#555;"> / mese</span></p>', unsafe_allow_html=True)
        st.write("✅ Terminale Operativo Completo")
        st.write("✅ Collegamento Bridge MT5")
        st.write("✅ AI News Sentinel & Journal")
        st.markdown('<div class="cta-button">', unsafe_allow_html=True)
        if st.button("ATTIVA ORA (PAYPAL)"):
            st.info("Qui inseriremo il tuo link PayPal.me")
        st.markdown('</div></div>', unsafe_allow_html=True)

    with c_login:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.subheader("Accesso Utenti")
        user = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("ENTRA NEL TERMINALE"):
            if user == "luca" and password == "zen2026":
                st.session_state['auth'] = True
                st.rerun()
            else:
                st.error("Credenziali non valide")
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- IL TERMINALE (Quello che abbiamo fatto prima) ---
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update({"auth": False}))
    st.title("🛡️ ZenTrader Terminal")
    # ... qui rimetteremo le 3 colonne del terminale che ti piacevano
    st.write("Bentornato Luca. Il sistema è pronto per l'esecuzione.")
    if st.button("Apri Interfaccia Operativa"):
        st.write("Visualizzazione Grafico e Broker...")
