import streamlit as st

st.set_page_config(page_title="ZenTrader Pro", layout="wide")

# --- CSS RADICALE ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;700&display=swap');
    
    .stApp { background-color: #000; color: #fff; font-family: 'Space Grotesk', sans-serif; }
    header, footer, section[data-testid="stSidebar"] { display: none !important; }

    /* CONTENITORE PRINCIPALE */
    .hero {
        text-align: center;
        padding: 100px 20px;
        background: radial-gradient(circle at center, #1a1a1a 0%, #000 80%);
    }

    .title-main { font-size: 85px; font-weight: 700; letter-spacing: -5px; margin-bottom: 0; line-height: 1; }
    .gold-glow { color: #ffd700; text-shadow: 0 0 20px rgba(255, 215, 0, 0.4); }

    /* GRID DELLE FEATURES */
    .features-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 30px;
        max-width: 1200px;
        margin: 60px auto;
        padding: 0 20px;
    }

    .f-card {
        background: linear-gradient(145deg, #0f0f0f, #050505);
        border: 1px solid #222;
        border-radius: 2px; /* Angoli netti = più cattivo/professionale */
        padding: 60px 30px;
        text-align: left;
        transition: 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }

    .f-card:hover {
        border-color: #ffd700;
        transform: scale(1.02);
        box-shadow: 0 0 40px rgba(255, 215, 0, 0.1);
    }

    .f-card::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 2px;
        background: linear-gradient(90deg, transparent, #ffd700, transparent);
        transform: translateX(-100%); transition: 0.5s;
    }
    .f-card:hover::before { transform: translateX(100%); }

    .f-card h3 { 
        font-size: 14px; letter-spacing: 4px; color: #ffd700; 
        text-transform: uppercase; margin-bottom: 20px; 
    }
    
    .f-card p { 
        font-size: 18px; color: #eee; font-weight: 300; 
        line-height: 1.4; margin: 0; 
    }

    /* LOGIN BOX */
    .login-container {
        max-width: 400px; margin: 40px auto; padding: 40px;
        background: #080808; border: 1px solid #111;
    }
</style>
""", unsafe_allow_html=True)

# --- LAYOUT ---
st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown('<h1 class="title-main">ZEN<span class="gold-glow">TRADER</span></h1>', unsafe_allow_html=True)
st.markdown('<p style="letter-spacing:10px; color:#444; margin-bottom:80px;">QUANTUM RISK INTERFACE</p>', unsafe_allow_html=True)

st.markdown("""
<div class="features-container">
    <div class="f-card">
        <h3>Risk Protect</h3>
        <p>Hard-cap al 2% di drawdown. Disciplina algoritmica che protegge il tuo capitale dai tuoi errori.</p>
    </div>
    <div class="f-card">
        <h3>Cloud Bridge</h3>
        <p>Esecuzione diretta MT5 via API. Zero latenza. Il tuo terminale web comanda il broker.</p>
    </div>
    <div class="f-card">
        <h3>AI Analysis</h3>
        <p>Algoritmi proprietari su XAUUSD. Scannerizza la liquidità istituzionale in tempo reale.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Login minimalista sotto
_, col, _ = st.columns([1, 0.6, 1])
with col:
    with st.form("access"):
        u = st.text_input("USER", label_visibility="collapsed", placeholder="IDENTIFICATION")
        p = st.text_input("PASS", type="password", label_visibility="collapsed", placeholder="SECURITY KEY")
        if st.form_submit_button("SBLOCCA TERMINALE"):
            if u == "luca" and p == "zen2026":
                st.session_state.auth = True
                st.rerun()
st.markdown('</div>', unsafe_allow_html=True)
