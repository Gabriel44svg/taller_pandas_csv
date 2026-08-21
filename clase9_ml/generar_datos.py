"""
Genera los datasets sinteticos para la Clase 9 (Introduccion a Machine Learning)
- viviendas.csv         -> usado en el Live Coding (primer modelo)
- viviendas_reto.csv    -> usado en el Machine Learning Challenge
"""

import numpy as np
import pandas as pd

np.random.seed(42)

# ------------------------------------------------------------
# 1. viviendas.csv  (Live Coding)
# columnas: metros, habitaciones, banios, antiguedad, precio
# ------------------------------------------------------------

n = 1000

metros = np.random.normal(loc=120, scale=40, size=n).clip(35, 320).round(1)
habitaciones = np.random.choice([1, 2, 3, 4, 5], size=n, p=[0.05, 0.25, 0.35, 0.25, 0.10])
banios = np.random.choice([1, 2, 3, 4], size=n, p=[0.30, 0.40, 0.20, 0.10])
antiguedad = np.random.gamma(shape=2.0, scale=6.0, size=n).clip(0, 45).round().astype(int)

ruido = np.random.normal(loc=0, scale=150000, size=n)

precio = (
    300000
    + 18000 * metros
    + 150000 * habitaciones
    + 80000 * banios
    - 4000 * antiguedad
    + ruido
).clip(min=450000)

precio = (precio / 1000).round() * 1000  # redondear a miles

df_viviendas = pd.DataFrame({
    "metros": metros,
    "habitaciones": habitaciones,
    "banios": banios,
    "antiguedad": antiguedad,
    "precio": precio.astype(int)
})

# unos pocos NaN para que la exploracion (df.isna().sum()) tenga sentido
nan_idx = np.random.choice(df_viviendas.index, size=8, replace=False)
df_viviendas.loc[nan_idx, "antiguedad"] = np.nan

df_viviendas.to_csv("/home/claude/clase9_ml/data/viviendas.csv", index=False)

# ------------------------------------------------------------
# 2. viviendas_reto.csv (Machine Learning Challenge)
# columnas: metros, habitaciones, banios, antiguedad, distancia_centro, precio
# ------------------------------------------------------------

n2 = 800

metros2 = np.random.normal(loc=115, scale=45, size=n2).clip(30, 340).round(1)
habitaciones2 = np.random.choice([1, 2, 3, 4, 5], size=n2, p=[0.08, 0.27, 0.32, 0.23, 0.10])
banios2 = np.random.choice([1, 2, 3, 4], size=n2, p=[0.32, 0.38, 0.20, 0.10])
antiguedad2 = np.random.gamma(shape=2.2, scale=6.5, size=n2).clip(0, 50).round().astype(int)
distancia_centro = np.random.exponential(scale=7.0, size=n2).clip(0.3, 35).round(1)

ruido2 = np.random.normal(loc=0, scale=160000, size=n2)

precio2 = (
    280000
    + 17500 * metros2
    + 140000 * habitaciones2
    + 75000 * banios2
    - 3800 * antiguedad2
    - 9000 * distancia_centro
    + ruido2
).clip(min=400000)

precio2 = (precio2 / 1000).round() * 1000

df_reto = pd.DataFrame({
    "metros": metros2,
    "habitaciones": habitaciones2,
    "banios": banios2,
    "antiguedad": antiguedad2,
    "distancia_centro": distancia_centro,
    "precio": precio2.astype(int)
})

# algunos NaN y un par de outliers para el analisis de errores del reto
nan_idx2 = np.random.choice(df_reto.index, size=6, replace=False)
df_reto.loc[nan_idx2, "banios"] = np.nan

outlier_idx = np.random.choice(df_reto.index, size=4, replace=False)
df_reto["precio"] = df_reto["precio"].astype(float)
df_reto.loc[outlier_idx, "precio"] = df_reto.loc[outlier_idx, "precio"] * 2.2
df_reto["precio"] = df_reto["precio"].round().astype(int)

df_reto.to_csv("/home/claude/clase9_ml/data/viviendas_reto.csv", index=False)

print("viviendas.csv:", df_viviendas.shape)
print("viviendas_reto.csv:", df_reto.shape)
print(df_viviendas.head())
print(df_reto.head())
