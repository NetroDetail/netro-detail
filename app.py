import streamlit as st

st.set_page_config(
    page_title="Netro Detail | Detallado Automotriz",
    page_icon="🚗",
    layout="wide"
)

# Estilos profesionales con el banner horizontal texturizado de lado a lado
st.markdown("""
    <style>
    .stApp {
        background-color: #f8fafc;
    }
    /* Franja banner horizontal de lado a lado con la textura de fondo del logo */
    .banner-completo {
        background-color: #e2e8f0;
        background-image: radial-gradient(#cbd5e1 1.2px, transparent 1.2px), radial-gradient(#cbd5e1 1.2px, #e2e8f0 1.2px);
        background-size: 24px 24px;
        background-position: 0 0, 12px 12px;
        width: 100vw;
        position: relative;
        left: calc(-50vw + 50%);
        padding: 35px 0;
        margin-top: -20px;
        margin-bottom: 30px;
        border-top: 3px solid #cbd5e1;
        border-bottom: 3px solid #cbd5e1;
        box-shadow: inset 0 4px 10px rgba(0,0,0,0.04);
    }
    .subtitulo {
        font-size: 1.3rem;
        color: #0284c7;
        text-align: center;
        font-weight: 700;
        margin-top: 15px;
        margin-bottom: 0px;
    }
    .contacto-banner {
        background: linear-gradient(90deg, #ff7e00, #ec4899, #06b6d4);
        padding: 22px;
        border-radius: 12px;
        text-align: center;
        font-size: 1.4rem;
        font-weight: bold;
        color: white;
        margin-bottom: 35px;
        box-shadow: 0 4px 15px rgba(236, 72, 153, 0.3);
    }
    .card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 16px;
        border: 2px solid #38bdf8;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
        color: #1e293b !important;
        margin-bottom: 25px;
    }
    .card-2 {
        border: 2px solid #ec4899;
    }
    .card-3 {
        border: 2px solid #ff7e00;
    }
    .card-4 {
        border: 2px solid #a855f7;
    }
    .card h3 {
        color: #0f172a !important;
        margin-top: 0;
        font-size: 1.5rem;
    }
    .card li {
        color: #334155 !important;
        margin-bottom: 8px;
        font-size: 1.05rem;
        font-weight: 500;
    }
    h1, h2 {
        color: #0f172a !important;
    }
    p {
        color: #475569 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- BANNER HORIZONTAL CONTINUO CON LA TEXTURA DEL LOGO ---
st.markdown('<div class="banner-completo">', unsafe_allow_html=True)

col_logo1, col_logo2, col_logo3 = st.columns([2, 1, 2])
with col_logo2:
    try:
        st.image("2E4B2249-9AC2-448E-90D5-A77A10E5FF49.jpg", use_container_width=True)
    except:
        st.warning("⚠️ No se encontró la imagen del logo.")

st.markdown('<p class="subtitulo">⚡ Pasión por la estética y protección máxima para tu vehículo ⚡</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- SECCIÓN 1: VIDEOS INFORMATIVOS DE LA MARCA ---
st.header("🎥 Conoce Netro Detail")
st.write("Descubre quiénes somos y nuestra línea exclusiva de productos:")

col_v1, col_v2 = st.columns(2)
with col_v1:
    st.markdown("### Presentación Oficial")
    try:
        st.video("video.mp4")
    except:
        st.info("💡 Falta el archivo video.mp4")

with col_v2:
    st.markdown("### Línea de Productos")
    try:
        st.video("video2.mp4")
    except:
        st.info("💡 Falta el archivo video2.mp4")

st.markdown("<br>", unsafe_allow_html=True)

# --- SECCIÓN 2: VIDEOS DE RESULTADOS PROFESIONALES ---
st.header("✨ Resultados Profesionales")
st.write("Mira los acabados de alto nivel que logramos en los vehículos de nuestros clientes:")

col_v3, col_v4 = st.columns(2)
with col_v3:
    st.markdown("### Resultado: Aplicación de Cerámico")
    try:
        st.video("video3.mp4")
    except:
        st.info("💡 Sube tu video3.mp4 en GitHub para mostrarlo aquí.")

with col_v4:
    st.markdown("### Resultado: Pulido y Encerado")
    try:
        st.video("video4.mp4")
    except:
        st.info("💡 Sube tu video4.mp4 en GitHub para mostrarlo aquí.")

st.markdown("<br>", unsafe_allow_html=True)

# --- BANNER DE WHATSAPP INTERACTIVO ---
whatsapp_url = "https://wa.me/524421219758?text=Hola,%20me%20interesa%20cotizar%20un%20servicio%20de%20detallado%20para%20mi%20auto."

st.markdown(f"""
    <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
        <div class="contacto-banner" style="cursor: pointer;">
            💬 ¡Reserva tu cita o cotiza hoy por WhatsApp: <span style="color: #fef08a; text-shadow: 0 0 5px #000;">+52 (442) 121-9758</span>! 📲
        </div>
    </a>
""", unsafe_allow_html=True)

st.markdown("---")

# --- SECCIÓN DE PAQUETES ---
st.header("✨ Nuestros Paquetes de Detallado")
st.write("Selecciona el nivel de renovación que tu auto necesita:")

col1, col2 = st.columns(2)

with col1:
    # PAQUETE 1
    st.markdown("""
        <div class="card">
            <h3>🔹 Paquete 1</h3>
            <hr style="border-color: #38bdf8;">
            <ul>
                <li>Lavado profundo (exterior)</li>
                <li>Detallado interior (Limpieza y aspirado)</li>
                <li>Descontaminación mecánica y química de pintura</li>
                <li>Pulido de 1 paso (corrección hasta un 50%)</li>
                <li>Abrillantado de llantas</li>
                <li>Aplicación de cera</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # PAQUETE 3
    st.markdown("""
        <div class="card card-3">
            <h3>🔥 Paquete 3</h3>
            <hr style="border-color: #ff7e00;">
            <ul>
                <li>Lavado profundo (exterior)</li>
                <li>Detallado interior (Limpieza y aspirado)</li>
                <li>Descontaminación mecánica y química de pintura</li>
                <li>Limpieza de emblemas</li>
                <li>Pulido de 2 pasos (corrección hasta un 90%)</li>
                <li>Descontaminación química de rines</li>
                <li>Abrillantado de llantas</li>
                <li><b>Aplicación de cera carnauba Meguiar’s Gold Class</b></li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # PAQUETE 2
    st.markdown("""
        <div class="card card-2">
            <h3>🌟 Paquete 2</h3>
            <hr style="border-color: #ec4899;">
            <ul>
                <li>Lavado profundo (exterior)</li>
                <li>Detallado interior (Limpieza y aspirado)</li>
                <li>Descontaminación mecánica y química de pintura</li>
                <li>Limpieza de emblemas</li>
                <li>Pulido de 2 pasos (corrección hasta un 80%)</li>
                <li>Descontaminación química de rines</li>
                <li>Abrillantado de llantas</li>
                <li><b>Aplicación de cera Meguiar’s Cleaner Wax</b></li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # PAQUETE 4
    st.markdown("""
        <div class="card card-4">
            <h3>💎 Paquete 4 (Nivel Pro / Cerámico)</h3>
            <hr style="border-color: #a855f7;">
            <ul>
                <li>Lavado profundo (exterior)</li>
                <li>Detallado interior (Limpieza y aspirado)</li>
                <li>Descontaminación mecánica y química de pintura</li>
                <li>Limpieza de emblemas</li>
                <li>Pulido de 2 pasos (corrección hasta un 90%)</li>
                <li>Descontaminación química de rines</li>
                <li>Abrillantado de llantas</li>
                <li><b>Aplicación de cerámico Chemical Guys</b></li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- SERVICIOS ADICIONALES ---
st.header("🛠️ Servicios Adicionales")
col_add1, col_add2, col_add3 = st.columns(3)

with col_add1:
    st.info("**Lavado de vestiduras**\n\nEliminación profunda de manchas y suciedad acumulada en tela.")
with col_add2:
    st.info("**Limpieza e hidratación de asientos de piel**\n\nNutrición profesional para evitar cuarteaduras y alargar su vida.")
with col_add3:
    st.info("**Lavado básico de auto**\n\nMantenimiento rápido y seguro para el día a día.")

st.markdown("---")

# --- APARTADO DE CONTACTO (CONECTADO A FORMSPREE) ---
st.header("📩 Contáctanos o Agenda una Cita")
st.write("Déjanos tus datos y nos pondremos en contacto contigo lo antes posible para resolver tus dudas.")

formspree_url = "https://formspree.io/f/mkjnkprw"

st.markdown(f"""
<form action="{formspree_url}" method="POST">
    <div style="margin-bottom: 15px;">
        <label style="color: #1e293b; font-weight: bold;">Nombre completo</label><br>
        <input type="text" name="nombre" required style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #cbd5e1;">
    </div>
    <div style="margin-bottom: 15px;">
        <label style="color: #1e293b; font-weight: bold;">Número de teléfono</label><br>
        <input type="text" name="telefono" required style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #cbd5e1;">
    </div>
    <div style="margin-bottom: 15px;">
        <label style="color: #1e293b; font-weight: bold;">Correo electrónico</label><br>
        <input type="email" name="correo" required style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #cbd5e1;">
    </div>
    <div style="margin-bottom: 15px;">
        <label style="color: #1e293b; font-weight: bold;">Paquete o servicio de interés</label><br>
        <select name="paquete_interes" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #cbd5e1;">
            <option value="Paquete 1">Paquete 1</option>
            <option value="Paquete 2">Paquete 2</option>
            <option value="Paquete 3">Paquete 3</option>
            <option value="Paquete 4">Paquete 4</option>
            <option value="Servicios Adicionales">Servicios Adicionales</option>
            <option value="Cotización General">Cotización General</option>
        </select>
    </div>
    <div style="margin-bottom: 15px;">
        <label style="color: #1e293b; font-weight: bold;">Dudas o comentarios</label><br>
        <textarea name="dudas" rows="4" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #cbd5e1;"></textarea>
    </div>
    <button type="submit" style="background: linear-gradient(90deg, #ff7e00, #ec4899); color: white; padding: 10px 20px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer;">Enviar Mensaje</button>
</form>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>© 2026 NETRO DETAIL. Todos los derechos reservados.</p>", unsafe_allow_html=True)
