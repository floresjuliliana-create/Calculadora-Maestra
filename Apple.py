import streamlit as st

# Selección de modo
modo = st.radio("¿Qué producto vas a gestionar?", 
                ["Producto Natura (Precio Catálogo)", "Producto Bazar / Marroquinería"])

# Parámetros internos (fijos)
GASTOS_FIJOS = 1820
MARGEN_GANANCIA = 0.40

# --- Lógica Natura ---
if modo == "Producto Natura (Precio Catálogo)":
    precio_catalogo = st.number_input("Ingresá el valor de venta del catálogo ($):", min_value=0.0, step=100.0)
    
    if st.button("CALCULAR"):
        # Precio mínimo para no perder (Costo Natura 70% + Gastos Fijos)
        costo_natur = precio_catalogo * 0.70
        precio_minimo = costo_natur + GASTOS_FIJOS
        
        st.write(f"Precio mínimo de venta para no perder: **${precio_minimo:,.0f}**")
        
        ganancia_neta = precio_catalogo - precio_minimo
        sobre_negocio = precio_minimo + (ganancia_neta * 0.20)
        sobre_crecimiento = ganancia_neta * 0.50
        sobre_sueldo = ganancia_neta * 0.30
        
        st.write("---")
        st.write("### --- RESULTADO ---")
        st.info(f"💰 Sobre 1 - Negocio: ${sobre_negocio:,.0f}")
        st.warning(f"📈 Sobre 2 - Crecimiento: ${sobre_crecimiento:,.0f}")
        st.success(f"💵 Sobre 3 - Tu Sueldo Personal: ${sobre_sueldo:,.0f}")

# --- Lógica Bazar ---
else: 
    costo_compra = st.number_input("Ingresá el costo de compra ($):", min_value=0.0, step=100.0)
    
    if st.button("CALCULAR"):
        # Calculamos el precio sugerido
        precio_sugerido = (costo_compra + GASTOS_FIJOS) / (1 - MARGEN_GANANCIA)
        ganancia_neta = precio_sugerido - costo_compra - GASTOS_FIJOS
        
        st.write(f"Precio sugerido de venta: **${precio_sugerido:,.0f}**")
        
        sobre_negocio = (costo_compra + GASTOS_FIJOS) + (ganancia_neta * 0.20)
        sobre_crecimiento = ganancia_neta * 0.50
        sobre_sueldo = ganancia_neta * 0.30
        
        st.write("---")
        st.write("### --- RESULTADO ---")
        st.info(f"💰 Sobre 1 - Negocio: ${sobre_negocio:,.0f}")
        st.warning(f"📈 Sobre 2 - Crecimiento: ${sobre_crecimiento:,.0f}")
        st.success(f"💵 Sobre 3 - Tu Sueldo Personal: ${sobre_sueldo:,.0f}")

