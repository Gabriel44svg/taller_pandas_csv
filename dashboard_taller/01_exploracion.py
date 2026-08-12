"""
PASO 1 — Cargar y explorar
Diapositiva: "Paso 1: cargar y explorar"

Objetivo: antes de crear cualquier gráfica, entender qué hay en los
datos: columnas, tipos, tamaño, nulos y estadísticas básicas.

Pregunta al grupo (lánzala ANTES de descomentar el código):
¿Qué preguntas de negocio podríamos responder con estos datos?
"""

import pandas as pd

# PASO A — cargar el CSV
df = pd.read_csv("data/ventas.csv")

#  PASO B — primer vistazo
print(df.head())

# PASO C — dimensiones (filas, columnas)
print(df.shape)

# PASO D — tipos de dato de cada columna
print(df.info())

# PASO E — valores nulos por columna
print(df.isnull().sum())

# PASO F — estadísticas descriptivas de columnas numéricas
print(df.describe())

# ---------------------------------------------------------------
#   - Fecha llega como texto (object), no como datetime todavía.
#     Eso se corrige en el Paso 2 con pd.to_datetime.
#   - No hay nulos: es un dataset limpio a propósito, para no
#     desviar la primera sesión hacia limpieza de datos.
#   - df.describe() ya deja ver que "Cantidad" y "Precio" varían
#     mucho por producto -> pie para preguntar "¿qué tan comparables
#     son estas transacciones entre sí?"
# ---------------------------------------------------------------
