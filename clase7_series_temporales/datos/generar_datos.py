"""
generar_datos.py
==================================================================
Genera los dos datasets utilizados en la Clase 7 (Series Temporales I):

    1) ventas_historicas.csv  -> usado en "Live Coding" (Pasos 1-10)
       columnas: fecha, ventas, unidades, promociones, temperatura, region

    2) ventas_tienda.csv      -> usado en "Practica guiada" (equipos)
       columnas: fecha, ventas, unidades, categoria

Ambas series están construidas a propósito con:
    - tendencia creciente (para la sección de Tendencia)
    - estacionalidad semanal (para lag=7, autocorr, ACF/PACF)
    - estacionalidad anual leve, pico en diciembre (para Estacionalidad)
    - ruido aleatorio (para la sección de Ruido)
    - promociones/eventos puntuales (para Errores comunes / outliers)

Ejecutar una sola vez:
    python generar_datos.py
==================================================================
"""

import numpy as np
import pandas as pd

SEED = 42
rng = np.random.default_rng(SEED)

# ==================================================================
# 1) VENTAS_HISTORICAS.CSV  (2 años de datos diarios)
# ==================================================================

fecha_inicio = "2024-01-01"
fecha_fin = "2025-12-31"
fechas = pd.date_range(fecha_inicio, fecha_fin, freq="D")
n = len(fechas)
t = np.arange(n)

# --- Tendencia: crecimiento lineal suave ---
tendencia = 100 + 0.18 * t

# --- Estacionalidad semanal: ventas más altas viernes/sábado ---
dia_semana = fechas.dayofweek  # 0=lunes ... 6=domingo
efecto_semanal = {
    0: -8,   # lunes
    1: -5,   # martes
    2: -2,   # miércoles
    3: 3,    # jueves
    4: 18,   # viernes
    5: 25,   # sábado
    6: -10,  # domingo
}
estacionalidad_semanal = np.array([efecto_semanal[d] for d in dia_semana])

# --- Estacionalidad anual: pico en diciembre, valle en febrero ---
dia_del_anio = fechas.dayofyear
estacionalidad_anual = 30 * np.sin(2 * np.pi * (dia_del_anio - 80) / 365.25)
estacionalidad_anual = np.where(
    fechas.month == 12, estacionalidad_anual + 40, estacionalidad_anual
)

# --- Promociones: ~7% de los días, más frecuentes en nov-dic ---
prob_promo = np.where(fechas.month.isin([11, 12]), 0.20, 0.05)
promociones = rng.binomial(1, prob_promo)
efecto_promo = promociones * rng.normal(35, 8, size=n)

# --- Ruido aleatorio ---
ruido = rng.normal(0, 10, size=n)

ventas = tendencia + estacionalidad_semanal + estacionalidad_anual + efecto_promo + ruido
ventas = np.round(np.clip(ventas, 10, None), 2)

# --- Unidades: relacionadas con ventas + su propio ruido ---
precio_promedio = 12.5
unidades = np.round(ventas / precio_promedio + rng.normal(0, 1.2, size=n)).astype(int)
unidades = np.clip(unidades, 1, None)

# --- Temperatura: estacionalidad anual tipo CDMX (12-26 C) + ruido ---
temperatura = 19 + 6 * np.sin(2 * np.pi * (dia_del_anio - 60) / 365.25) + rng.normal(0, 1.5, size=n)
temperatura = np.round(temperatura, 1)

# --- Región: metadato categórico (no interviene en los cálculos temporales) ---
regiones = ["Centro", "Norte", "Sur", "Este", "Oeste"]
region = rng.choice(regiones, size=n, p=[0.4, 0.15, 0.15, 0.15, 0.15])

df_historicas = pd.DataFrame({
    "fecha": fechas,
    "ventas": ventas,
    "unidades": unidades,
    "promociones": promociones,
    "temperatura": temperatura,
    "region": region,
})

# Insertamos algunos NaN a propósito (para practicar df.isna().sum())
idx_nan = rng.choice(n, size=5, replace=False)
df_historicas.loc[idx_nan, "temperatura"] = np.nan

ruta_historicas = "ventas_historicas.csv"
df_historicas.to_csv(ruta_historicas, index=False)
print(f"[OK] {ruta_historicas} generado con {len(df_historicas)} filas")

# ==================================================================
# 2) VENTAS_TIENDA.CSV  (1 año de datos diarios, para práctica en equipos)
# ==================================================================

fecha_inicio_2 = "2025-01-01"
fecha_fin_2 = "2025-12-31"
fechas2 = pd.date_range(fecha_inicio_2, fecha_fin_2, freq="D")
n2 = len(fechas2)
t2 = np.arange(n2)

tendencia2 = 60 + 0.12 * t2

dia_semana2 = fechas2.dayofweek
efecto_semanal2 = {
    0: -5, 1: -3, 2: 0, 3: 4, 4: 12, 5: 20, 6: -6,
}
estacionalidad_semanal2 = np.array([efecto_semanal2[d] for d in dia_semana2])

dia_del_anio2 = fechas2.dayofyear
estacionalidad_anual2 = 15 * np.sin(2 * np.pi * (dia_del_anio2 - 100) / 365.25)
estacionalidad_anual2 = np.where(
    fechas2.month == 12, estacionalidad_anual2 + 25, estacionalidad_anual2
)

ruido2 = rng.normal(0, 7, size=n2)

ventas2 = tendencia2 + estacionalidad_semanal2 + estacionalidad_anual2 + ruido2
ventas2 = np.round(np.clip(ventas2, 5, None), 2)

precio_promedio2 = 9.0
unidades2 = np.round(ventas2 / precio_promedio2 + rng.normal(0, 1.0, size=n2)).astype(int)
unidades2 = np.clip(unidades2, 1, None)

categorias = ["Electronica", "Ropa", "Alimentos", "Hogar"]
categoria = rng.choice(categorias, size=n2, p=[0.3, 0.3, 0.25, 0.15])

df_tienda = pd.DataFrame({
    "fecha": fechas2,
    "ventas": ventas2,
    "unidades": unidades2,
    "categoria": categoria,
})

# Quitamos algunos días a propósito (para practicar "fechas faltantes")
idx_drop = rng.choice(n2, size=6, replace=False)
df_tienda = df_tienda.drop(index=idx_drop).reset_index(drop=True)

ruta_tienda = "ventas_tienda.csv"
df_tienda.to_csv(ruta_tienda, index=False)
print(f"[OK] {ruta_tienda} generado con {len(df_tienda)} filas")
