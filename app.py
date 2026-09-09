import streamlit as st

st.set_page_config(
    page_title="Netro Detail | Detallado Automotriz",
    page_icon="🚗",
    layout="wide"
)

# Estilos limpios y profesionales
st.markdown("""
    <style>
    .stApp {
        background-color: #f8fafc;
    }
    .subtitulo {
        font-size: 1.3rem;
        color: #0284c7;
        text-align: center;
        font-weight: 700;
        margin-bottom: 25px;
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

# --- ENCABEZADO Y LOGO COMPACTO CENTRADO ---
col_logo1, col_logo2, col_logo3 = st.columns([2, 1, 2])
with col_logo2:
    try:
        st.image("2E4B2249-9AC2-448E-90D5-A77A10E5FF49.jpg", use_container_width=True)
    except:
        st.warning("⚠️ No se encontró la imagen del logo.")

st.markdown('<p class="subtitulo">⚡ Pasión urbana, estética y protección máxima para tu vehículo ⚡</p>', unsafe_allow_html=True)

# --- VIDEOS INSTITUCIONALES Y COMERCIALES ---
col_v1, col_v2, col_v3 = st.columns([1, 6, 1])
with col_v2:
    st.header("🎥 Conoce Netro Detail")
    try:
        st.video("video.mp4")
    except:
        st.info("💡 Coloca tu primer video con el nombre 'video.mp4'.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.header("🛍️ Próximamente a la Venta: Línea de Productos")
    try:
        st.video("video2.mp4")
    except:
        st.info("💡 Coloca tu segundo video con el nombre 'video2.mp4'.")

st.markdown("<br>", unsafe_allow_html=True)

# --- NÚMERO DE TELÉFONO DE CONTACTO DESTACADO ---
st.markdown("""
    <div class="contacto-banner">
        📞 ¡Reserva tu cita o cotiza hoy llamando al: <span style="color: #fef08a; text-shadow: 0 0 5px #000;">+52 (442 121 9758)</span>!
    </div>
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

# --- APARTADO DE CONTACTO ---
st.header("📩 Contáctanos o Agenda una Cita")
st.write("Déjanos tus datos y nos pondremos en contacto contigo lo antes posible para resolver tus dudas.")

with st.form("form_contacto"):
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        nombre = st.text_input("Nombre completo")
        telefono = st.text_input("Número de teléfono")
    with col_f2:
        correo = st.text_input("Correo electrónico")
        paquete_interes = st.selectbox("Paquete o servicio de interés", [
            "Paquete 1", "Paquete 2", "Paquete 3", "Paquete 4", 
            "Servicios Adicionales", "Cotización General"
        ])
    
    dudas = st.text_area("Dudas o comentarios")
    enviar = st.form_submit_button("Enviar Mensaje")
    
    if enviar:
        if nombre and telefono:
            st.success(f"¡Gracias {nombre}! Tus datos han sido enviados correctamente. Nos comunicaremos contigo muy pronto.")
        else:
            st.error("Por favor, completa al menos tu nombre y número de teléfono.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>© 2026 NETRO DETAIL. Todos los derechos reservados.</p>", unsafe_allow_html=True)