"""
Dashboard con filtros — versión final
Diapositiva: "Agregar filtros"

Correr con:  streamlit run 09_dashboard_streamlit_filtros.py

Este script es la continuación directa del 08_dashboard_streamlit.py:
además de los KPIs y la gráfica, agrega un selectbox para que el
usuario filtre por región. Úsalo como "gran final" del live coding,
o como plantilla base que los equipos extienden en el Dashboard
Challenge.
"""

import streamlit as st
import pandas as pd

# PASO A — base igual que el dashboard anterior
df = pd.read_csv("data/ventas.csv")
st.title("Dashboard de Ventas")

# PASO B — KPIs generales (sin filtrar)
ventas_totales = df["Ventas"].sum()
ticket_promedio = df["Ventas"].mean()

col1, col2 = st.columns(2)
col1.metric("Ventas totales", f"${ventas_totales:,.0f}")
col2.metric("Ticket promedio", f"${ticket_promedio:,.0f}")

# PASO C — el filtro (tal como en la diapositiva)
regiones = df["Region"].unique()

region = st.selectbox(
     "Selecciona una region",
     regiones
 )

df_filtrado = df[
     df["Region"] == region
 ]

ventas = df_filtrado["Ventas"].sum()

st.metric(
     "Ventas de la region",
     f"${ventas:,.0f}"
 )

# ---------------------------------------------------------------
# EXTRA  — Agregamos también un
# filtro de producto y una gráfica que reaccione al filtro
# (esto ya empieza a parecerse al Dashboard Challenge).
# ---------------------------------------------------------------

# EXTRA
# productos = df_filtrado["Producto"].unique()
# producto = st.selectbox("Selecciona un producto (opcional)", ["Todos"] + list(productos))
#
# if producto != "Todos":
#     df_filtrado = df_filtrado[df_filtrado["Producto"] == producto]
#
# ventas_producto_filtrado = (
#     df_filtrado.groupby("Producto")["Ventas"]
#                .sum()
#                .sort_values()
# )
#
# st.subheader(f"Ventas por producto — {region}")
# st.bar_chart(ventas_producto_filtrado)

# ---------------------------------------------------------------
# Frase de la diapositiva para cerrar este bloque:
# "Ahora el dashboard es interactivo. El usuario deja de ser
# espectador y comienza a explorar."
# ---------------------------------------------------------------
