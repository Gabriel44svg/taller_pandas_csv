"""
Dashboard rápido con Streamlit
Diapositiva: "Dashboard rápido con Streamlit"

Correr con:  streamlit run 08_dashboard_streamlit.py

Objetivo: mostrar que con muy poco código se pasa de un CSV a un
dashboard interactivo en el navegador (KPI cards + una gráfica).
"""

import streamlit as st
import pandas as pd

# PASO A — cargar los datos y poner un título
df = pd.read_csv("data/ventas.csv")
st.title("Dashboard de Ventas")

# DESCOMENTAR PASO B — dos KPIs simples en columnas
ventas = df["Ventas"].sum()
ticket = df["Ventas"].mean()
#
col1, col2 = st.columns(2)
col1.metric("Ventas", f"${ventas:,.0f}")
col2.metric("Ticket promedio", f"${ticket:,.0f}")

# PASO C — una gráfica de barras nativa de Streamlit
ventas_region = (
     df.groupby("Region")["Ventas"]
       .sum()
 )

st.subheader("Ventas por region")
st.bar_chart(ventas_region)

# ---------------------------------------------------------------
# Nota: st.bar_chart es intencionalmente
# "básico" (no se puede ordenar tan fácil como con matplotlib).
# Es un buen contraste para discutir: velocidad de desarrollo vs
# control fino sobre la visualización.
# ---------------------------------------------------------------
