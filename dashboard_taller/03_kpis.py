"""
PASO 3 — Calcular KPIs
Diapositiva: "Paso 3: calcular KPIs"

Objetivo: pasar de "un montón de filas" a un puñado de números que
sí responden preguntas de negocio (Ventas totales, Transacciones,
Ticket promedio, Unidades vendidas).

Recordatorio (para reforzar la diapositiva de "Métrica vs KPI"):
KPI = Métrica + Objetivo + Contexto.
Estos cuatro números son insumo para KPIs, pero se vuelven KPI de
verdad cuando los comparamos contra un objetivo o un periodo anterior.
"""

import pandas as pd

df = pd.read_csv("data/ventas.csv", parse_dates=["Fecha"])

# PASO A — ventas totales del periodo
ventas_totales = df["Ventas"].sum()

# PASO B — número de transacciones
transacciones = len(df)

# PASO C — ticket promedio
ticket_promedio = ventas_totales / transacciones

# PASO D — unidades totales vendidas
unidades = df["Cantidad"].sum()

# PASO E — imprimir el resumen
print("Ventas:", f"{ventas_totales:,.2f}")
print("Transacciones:", transacciones)
print("Ticket:", f"{ticket_promedio:,.2f}")
print("Unidades:", unidades)

# ---------------------------------------------------------------
# EXTRA opcional — crecimiento mes a mes (para conectar con la
# fórmula de Growth de la diapositiva de "Fórmulas de KPIs").
# Descomentar solo si hay tiempo / interés del grupo.
# ---------------------------------------------------------------

# EXTRA
# df["Mes"] = df["Fecha"].dt.to_period("M")
# ventas_mes = df.groupby("Mes")["Ventas"].sum()
# crecimiento = ventas_mes.pct_change() * 100
# print("\nVentas por mes:")
# print(ventas_mes)
# print("\nCrecimiento % mes a mes:")
# print(crecimiento.round(1))
#
# Con estos datos, julio 2026 debería mostrar el salto más grande del
# periodo (efecto de la campaña) — buen momento para conectar con la
# diapositiva "Ejemplo: de gráfica a historia".
