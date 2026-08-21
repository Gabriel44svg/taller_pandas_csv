# ============================================================
# 01 - TENDENCIA CENTRAL
# Media, mediana, moda
# Dataset: data/datos_generales.csv
# Requiere: haber corrido 00_setup.py (df cargado)
# ============================================================

# ------------------------------------------------------------
# Media
# ------------------------------------------------------------

# media = df["ventas"].mean()
# print(media)

# ------------------------------------------------------------
# Mediana
# ------------------------------------------------------------

# mediana = df["ventas"].median()
# print(mediana)

# ------------------------------------------------------------
# Media vs mediana con "ingreso" (columna con sesgo positivo
# por diseño: hay clientes con ingresos muy altos)
# ------------------------------------------------------------

# media_ingreso = df["ingreso"].mean()
# mediana_ingreso = df["ingreso"].median()

# print("Media ingreso:", media_ingreso)
# print("Mediana ingreso:", mediana_ingreso)

# print("¿Cuál representa mejor al cliente típico?")

# ------------------------------------------------------------
# Moda (variable categórica)
# ------------------------------------------------------------

# moda = df["categoria"].mode()
# print(moda)

# frecuencias = df["categoria"].value_counts()
# print(frecuencias)
