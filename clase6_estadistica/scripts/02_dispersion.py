# ============================================================
# 02 - DISPERSIÓN
# Rango, varianza, desviación estándar, coeficiente de variación
# Dataset: data/datos_generales.csv
# Requiere: haber corrido 00_setup.py (df cargado)
# ============================================================

# ------------------------------------------------------------
# Rango
# ------------------------------------------------------------

# rango = df["ventas"].max() - df["ventas"].min()
# print(rango)

# ------------------------------------------------------------
# Varianza
# ------------------------------------------------------------

# varianza = df["ventas"].var()
# print(varianza)

# ------------------------------------------------------------
# Desviación estándar
# ------------------------------------------------------------

# desviacion = df["ventas"].std()
# print(desviacion)

# ------------------------------------------------------------
# Misma media, ¿diferente dispersión?
# Comparemos "ventas" contra "publicidad" usando el
# coeficiente de variación (medida relativa de dispersión).
# ------------------------------------------------------------

# cv_ventas = df["ventas"].std() / df["ventas"].mean()
# cv_publicidad = df["publicidad"].std() / df["publicidad"].mean()

# print("CV ventas:", cv_ventas)
# print("CV publicidad:", cv_publicidad)

# ------------------------------------------------------------
# Ejercicio para el grupo: construir dos sub-muestras
# artificiales con la misma media pero distinta dispersión,
# tal como el ejemplo Grupo A / Grupo B de la presentación,
# y comprobarlo con .std()
# ------------------------------------------------------------

# import numpy as np
# grupo_a = np.array([48, 49, 50, 51, 52])
# grupo_b = np.array([10, 30, 50, 70, 90])

# print("Media A:", grupo_a.mean(), "Std A:", grupo_a.std(ddof=1))
# print("Media B:", grupo_b.mean(), "Std B:", grupo_b.std(ddof=1))
