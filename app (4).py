import streamlit as st
import json, os, base64

st.set_page_config(
    page_title="UrbanStyle — Camisas & Gorras",
    page_icon="👕",
    layout="wide",
)

INSTAGRAM = "https://www.instagram.com/juanjosegiraldo1234?igsh=MTA1OHphNm5pczliZg=="
WHATSAPP  = "https://wa.me/573216445069"

# ── Catálogo fijo ────────────────────────────────────────────────────────────
# Agrega aquí tus productos: pon la imagen en la carpeta "imagenes/"
# Si no tienes imagen todavía deja imagen: ""
PRODUCTOS = [
    # CAMISAS
    {
        "nombre": "Camisa Oversize Negra",
        "precio": "45.000",
        "descripcion": "Algodón 100% · Tallas S–XL",
        "categoria": "camisa",
        "imagen": "",   # Ej: "imagenes/camisa_negra.jpg"
    },
    {
        "nombre": "Camisa Básica Blanca",
        "precio": "40.000",
        "descripcion": "Corte recto · Unisex",
        "categoria": "camisa",
        "imagen": "",
    },
    {
        "nombre": "Camisa Gráfica Urbana",
        "precio": "52.000",
        "descripcion": "Estampado exclusivo · Edición limitada",
        "categoria": "camisa",
        "imagen": "",
    },
    # GORRAS
    {
        "nombre": "Gorra SnapBack Negra",
        "precio": "35.000",
        "descripcion": "Ajuste trasero · Talla única",
        "categoria": "gorra",
        "imagen": "",
    },
    {
        "nombre": "Gorra Bordada UrbanStyle",
        "precio": "38.000",
        "descripcion": "Logo bordado · Colores surtidos",
        "categoria": "gorra",
        "imagen": "",
    },
    {
        "nombre": "Gorra Curved Beige",
        "precio": "36.000",
        "descripcion": "Visera curva · Algodón suave",
        "categoria": "gorra",
        "imagen": "",
    },
]

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800&family=Inter:wght@400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.block-container { padding-top: 1rem !important; max-width: 1200px; }

.hero {
    background: #0f0f0f;
    border-radius: 14px;
    padding: 2.2rem 2.5rem;
    display: flex; align-items: center; justify-content: space-between;
    flex-wrap: wrap; gap: 1.2rem; margin-bottom: 2rem;
}
.hero-logo {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 3rem; font-weight: 800; color: #fff; line-height: 1;
}
.hero-logo span { color: #e63946; }
.hero-sub { color: #888; font-size: 0.92rem; margin-top: 0.3rem; }
.social-links { display: flex; gap: 0.7rem; flex-wrap: wrap; }
.pill {
    display: inline-flex; align-items: center; gap: 0.4rem;
    padding: 0.5rem 1.1rem; border-radius: 999px;
    font-size: 0.88rem; font-weight: 600; text-decoration: none; color: #fff;
}
.pill-ig { background: linear-gradient(135deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888); }
.pill-wa { background: #25d366; }

.sec-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 2rem; font-weight: 800; text-transform: uppercase;
    border-bottom: 3px solid #0f0f0f; padding-bottom: 0.4rem;
    margin: 2rem 0 1.2rem; color: #0f0f0f;
}

.card {
    background: #fff; border: 1px solid #e2e2e2;
    border-radius: 12px; overflow: hidden;
    transition: transform 0.18s, box-shadow 0.18s;
    height: 100%;
}
.card:hover { transform: translateY(-5px); box-shadow: 0 14px 32px rgba(0,0,0,0.11); }
.card-img { width:100%; aspect-ratio:4/5; object-fit:cover; display:block; }
.card-ph {
    width:100%; aspect-ratio:4/5;
    background: linear-gradient(135deg,#ececec,#d8d8d8);
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    font-size:3.5rem; color:#bbb;
}
.card-ph small { font-size:0.7rem; margin-top:0.4rem; font-family:'Inter',sans-serif; color:#bbb; }
.card-body { padding: 1rem; }
.card-name {
    font-family:'Barlow Condensed',sans-serif;
    font-size:1.2rem; font-weight:800; text-transform:uppercase; letter-spacing:0.03em;
}
.card-desc { font-size:0.78rem; color:#888; margin-top:0.2rem; line-height:1.45; }
.card-footer { display:flex; align-items:center; justify-content:space-between; margin-top:0.9rem; }
.price { font-family:'Barlow Condensed',sans-serif; font-size:1.6rem; font-weight:800; color:#e63946; }
.price::before { content:'$'; font-size:0.9em; }
.wa-btn {
    display:inline-flex; align-items:center; gap:0.35rem;
    background:#25d366; color:#fff; padding:0.45rem 0.95rem;
    border-radius:6px; text-decoration:none; font-size:0.82rem; font-weight:700;
}
.wa-btn:hover { background:#1ebe5d; }

.footer {
    background:#0f0f0f; border-radius:12px; padding:1.5rem 2rem;
    margin-top:3rem; display:flex; align-items:center;
    justify-content:space-between; flex-wrap:wrap; gap:1rem;
}
.footer-logo { font-family:'Barlow Condensed',sans-serif; font-size:1.5rem; font-weight:800; color:#fff; }
.footer-logo span { color:#e63946; }
.footer-copy { font-size:0.75rem; color:#555; margin-top:0.2rem; }
</style>
""", unsafe_allow_html=True)

# ── HEADER ───────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero">
  <div>
    <div class="hero-logo">Urban<span>Style</span></div>
    <div class="hero-sub">Camisas y gorras con actitud · Medellín, Colombia</div>
  </div>
  <div class="social-links">
    <a class="pill pill-ig" href="{INSTAGRAM}" target="_blank">📸 Instagram</a>
    <a class="pill pill-wa" href="{WHATSAPP}" target="_blank">💬 WhatsApp</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ── RENDER SECCIÓN ────────────────────────────────────────────────────────────
def render_section(titulo, emoji, items):
    st.markdown(f'<div class="sec-title">{emoji} {titulo}</div>', unsafe_allow_html=True)
    cols = st.columns(3)
    for i, p in enumerate(items):
        wa_link = f"{WHATSAPP}?text=Hola!%20Me%20interesa%20el%20producto:%20{p['nombre'].replace(' ','%20')}"
        if p.get("imagen") and os.path.exists(p["imagen"]):
            with open(p["imagen"], "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            ext = p["imagen"].rsplit(".", 1)[-1]
            img_html = f'<img class="card-img" src="data:image/{ext};base64,{b64}" alt="{p["nombre"]}"/>'
        else:
            img_html = f'<div class="card-ph">{emoji}<small>Foto próximamente</small></div>'

        with cols[i % 3]:
            st.markdown(f"""
            <div class="card">
              {img_html}
              <div class="card-body">
                <div class="card-name">{p['nombre']}</div>
                <div class="card-desc">{p['descripcion']}</div>
                <div class="card-footer">
                  <span class="price">{p['precio']}</span>
                  <a class="wa-btn" href="{wa_link}" target="_blank">💬 Pedir</a>
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)

camisas = [p for p in PRODUCTOS if p["categoria"] == "camisa"]
gorras  = [p for p in PRODUCTOS if p["categoria"] == "gorra"]

render_section("Camisas", "👕", camisas)
st.markdown("<hr style='margin:1rem 0;border-color:#e2e2e2'>", unsafe_allow_html=True)
render_section("Gorras", "🧢", gorras)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="footer">
  <div>
    <div class="footer-logo">Urban<span>Style</span></div>
    <div class="footer-copy">© 2025 · Todos los derechos reservados</div>
  </div>
  <div class="social-links">
    <a class="pill pill-ig" href="{INSTAGRAM}" target="_blank">📸 Instagram</a>
    <a class="pill pill-wa" href="{WHATSAPP}" target="_blank">💬 WhatsApp</a>
  </div>
</div>
""", unsafe_allow_html=True)
