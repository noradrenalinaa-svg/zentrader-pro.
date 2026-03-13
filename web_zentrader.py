import streamlit as st

# 1. Configurazione della pagina (deve essere la prima riga di codice)
st.set_page_config(page_title="ZenTrader Pro", layout="wide")

# 2. CSS per rendere tutto nero e professionale (stile terminale)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@100;400&display=swap');
    .stApp { background-color: #000 !important; color: #fff; font-family: 'JetBrains Mono', monospace; }
    header, footer, section[data-testid="stSidebar"] { display: none !important; }
    
    .grid-features {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        margin: 50px auto;
        max-width: 1200px;
    }
    .card {
        border: 1px solid #111;
        padding: 40px;
        background: #050505;
    }
    .card-label { color: #FFD700; font-size: 10px; letter-spacing: 3px; margin-bottom: 20px; }
    .card-title { font-size: 18px; margin-bottom: 10px; color: #fff; }
    .card-txt { font-size: 13px; color: #555; line-height: 1.5; }
</style>
""", unsafe_allow_html=True)

# 3. La tua Griglia HTML (ora dentro st.markdown così non dà errore)
st.markdown("""
<div class="grid-features">
    <div class="card">
        <div class="card-label">01 // RISK</div>
        <div class="card-title">HARD CAP PROTECTION</div>
        <div class="card-txt">Protocollo di sicurezza che blocca fisicamente l'accesso al broker in caso di drawdown superiore al 2%.</div>
    </div>
    <div class="card">
        <div class="card-label">02 // EXECUTION</div>
        <div class="card-title">LATENCY-FREE BRIDGE</div>
        <div class="card-txt">Connessione API diretta con MetaTrader 5. Ordini eseguiti istantaneamente dal terminale web.</div>
    </div>
    <div class="card">
        <div class="card-label">03 // ANALYTICS</div>
        <div class="card-title">QUANT SCANNER</div>
        <div class="card-txt">Algoritmi proprietari per l'individuazione di zone di liquidità e sbilanciamenti di volume.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Login Semplice
st.write("---")
col1, col2, col3 = st.columns([1,1,1])
with col2:
    with st.form("login"):
        u = st.text_input("User")
        p = st.text_input("Password", type="password")
        if st.form_submit_button("SBLOCCA TERMINALE"):
            if u == "luca" and p == "zen2026":
                st.success("Accesso eseguito!")
            else:
                st.error("Credenziali errate")
