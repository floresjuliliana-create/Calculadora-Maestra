import streamlit as st



st.subheader("Calculadora de Venta Unificada")

# Selección de modo
modo = st.radio("¿Qué producto vas a gestionar?", 
                ["Producto Natura (Precio Catálogo)", "Producto Bazar / Marroquinería"])

# Parámetros internos (fijos)
GASTOS_FIJOS = 1820
MARGEN_GANANCIA = 0.40

# Lógica según el modo
if modo == "Producto Natura (Precio Catálogo)":
    precio_venta = st.number_input("Ingresá el valor de venta ($):", min_value=0.0, step=100.0)
    if st.button("CALCULAR"):
        costo_natur = precio_venta * 0.70
        costo_total = costo_natur + GASTOS_FIJOS
        
        ganancia_neta = precio_venta - costo_total
        sobre_negocio = costo_total + (ganancia_neta * 0.20)
        sobre_crecimiento = ganancia_neta * 0.50
        sobre_sueldo = ganancia_neta * 0.30
        
        st.write("---")
        st.write("### --- RESULTADO ---")
        st.info(f"💰 Sobre 1 - Negocio: ${sobre_negocio:,.0f}")
        st.warning(f"📈 Sobre 2 - Crecimiento: ${sobre_crecimiento:,.0f}")
        st.success(f"💵 Sobre 3 - Tu Sueldo Personal: ${sobre_sueldo:,.0f}")

else: # Bazar / Marroquinería
    costo_compra = st.number_input("Ingresá el costo de compra ($):", min_value=0.0, step=100.0)
    if st.button("CALCULAR"):
        precio_venta_sugerido = (costo_compra + GASTOS_FIJOS) / (1 - MARGEN_GANANCIA)
        ganancia_neta = precio_venta_sugerido - costo_compra - GASTOS_FIJOS
        
        st.write(f"Precio de Venta sugerido: **${precio_venta_sugerido:,.0f}**")
        
        sobre_negocio = (costo_compra + GASTOS_FIJOS) + (ganancia_neta * 0.20)
        sobre_crecimiento = ganancia_neta * 0.50
        sobre_sueldo = ganancia_neta * 0.30
        
        st.write("---")
        st.write("### --- RESULTADO ---")
        st.info(f"💰 Sobre 1 - Negocio: ${sobre_negocio:,.0f}")
        st.warning(f"📈 Sobre 2 - Crecimiento: ${sobre_crecimiento:,.0f}")
        st.success(f"💵 Sobre 3 - Tu Sueldo Personal: ${sobre_sueldo:,.0f}")
