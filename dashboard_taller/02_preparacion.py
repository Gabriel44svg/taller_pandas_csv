"""
PASO 2 — Preparar los datos
Diapositiva: "Paso 2: preparar los datos"

Objetivo: convertir Fecha a datetime, confirmar el cálculo de Ventas
y crear la columna Mes para los análisis por periodo.

Concepto para remarcar (está también en la diapositiva):
"Garbage In -> Garbage Out". Una visualización depende de la calidad
de los datos que recibe.
"""

import pandas as pd

df = pd.read_csv("data/ventas.csv")

# PASO A — convertir Fecha de texto a datetime real
df["Fecha"] = pd.to_datetime(df["Fecha"])

#PASO B — (re)calcular Ventas = Cantidad * Precio
# El CSV ya trae "Ventas" calculada, pero vale la pena mostrar cómo
# se construye y confirmar que coincide con lo que ya está en el CSV.
df["Ventas"] = df["Cantidad"] * df["Precio"]

# PASO C — crear la columna Mes (periodo, no fecha exacta)
df["Mes"] = df["Fecha"].dt.to_period("M")

# PASO D — verificar el resultado
print(df.head())
print(df.dtypes)

# ---------------------------------------------------------------
# Notas
#   - dt.to_period("M") agrupa por mes-año (2026-01, 2026-02, ...)
#     sin importar el día, ideal para "ventas por mes".
#   - Si alguien pregunta por qué no usar df["Fecha"].dt.month solo:
#     porque perderías el año si el dataset cruzara varios años.
# ---------------------------------------------------------------
