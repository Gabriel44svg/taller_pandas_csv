# ============================================================
# GENERADOR DE DATASET CORRUPTO
# Diplomado en Analisis de Datos - Universidad Marista
# Sesion: Limpieza de Datos
# ============================================================
#
# Este script CREA el archivo "../datos/ventas_corruptas.csv" que se usa
# en el LIVE CODING de la sesion.
#
# No es un script para mostrar a los alumnos: es la "receta" que
# tu (instructor) corres UNA VEZ antes de la clase para producir
# el CSV con el que van a trabajar. Ya viene ejecutado y el
# resultado esta en "../datos/ventas_corruptas.csv", pero lo dejamos aqui
# comentado y documentado por si quieres regenerarlo, cambiar la
# semilla (seed) para tener una version distinta, o ajustar el
# nivel de "suciedad" de los datos.
#
# Usa una semilla fija (seed) para que el dataset sea 100%
# reproducible: correr este script siempre da el mismo resultado.
# ============================================================

import numpy as np
import pandas as pd

# ------------------------------------------------------------
# 0. CONFIGURACION GENERAL
# ------------------------------------------------------------

SEED = 42
N = 10_000  # numero de filas "base" antes de anadir duplicados

rng = np.random.default_rng(SEED)

# ------------------------------------------------------------
# 1. CATALOGOS BASE (valores "limpios" de referencia)
# ------------------------------------------------------------

NOMBRES = [
    "Ana Garcia", "Luis Hernandez", "Maria Lopez", "Jose Martinez",
    "Laura Sanchez", "Carlos Ramirez", "Sofia Torres", "Miguel Flores",
    "Daniela Cruz", "Jorge Morales", "Paola Rios", "Ricardo Vargas",
    "Fernanda Castro", "Andres Ortiz", "Valeria Mendoza", "Diego Romero",
    "Camila Reyes", "Alejandro Diaz", "Isabel Guzman", "Pedro Aguilar",
]

PRODUCTOS = [
    "Laptop", "Monitor", "Teclado", "Mouse", "Impresora",
    "Silla", "Escritorio", "Bocina", "Camara", "Tablet",
]

REGIONES = ["Norte", "Sur", "Centro", "Occidente"]

# ------------------------------------------------------------
# 2. COLUMNAS "LIMPIAS" DE PARTIDA
# ------------------------------------------------------------

ids = np.arange(1, N + 1)
clientes = rng.choice(NOMBRES, size=N)
productos = rng.choice(PRODUCTOS, size=N)
regiones = rng.choice(REGIONES, size=N)

# Edad: distribucion normal centrada en 38, truncada despues
edades = rng.normal(loc=38, scale=12, size=N).round().astype(int)

# Precio base (numerico limpio antes de "ensuciarlo")
precios = rng.normal(loc=850, scale=300, size=N).round(2)
precios = np.clip(precios, 50, None)

# Fechas base: un rango de 2 anios
fechas_base = pd.to_datetime("2024-01-01") + pd.to_timedelta(
    rng.integers(0, 900, size=N), unit="D"
)

# Ventas: la mayoria en un rango normal de negocio
ventas = rng.normal(loc=1400, scale=350, size=N).round(2)
ventas = np.clip(ventas, 100, None)

df = pd.DataFrame({
    "ID": ids,
    "Cliente": clientes,
    "Producto": productos,
    "Region": regiones,
    "Edad": edades,
    "Precio": precios,
    "Fecha": fechas_base,
    "Ventas": ventas,
})

# ------------------------------------------------------------
# 3. "ENSUCIAR" LA COLUMNA Region (texto inconsistente)
# ------------------------------------------------------------
# Mismo valor semantico, escrito de formas distintas:
# "Norte", "norte", "NORTE", " Norte", "Norte "
# Ademas, distintos "sabores" de valor faltante.

def ensuciar_region(valor, r):
    tipo = r.random()
    if tipo < 0.15:
        return valor.lower()
    elif tipo < 0.25:
        return valor.upper()
    elif tipo < 0.32:
        return f" {valor}"
    elif tipo < 0.39:
        return f"{valor} "
    else:
        return valor

df["Region"] = [ensuciar_region(v, rng) for v in df["Region"]]

# ~4% de faltantes en Region, con distintas representaciones
mask_region_na = rng.random(N) < 0.04
opciones_na_region = ["N/A", "?", "sin informacion", None, ""]
df.loc[mask_region_na, "Region"] = rng.choice(
    opciones_na_region, size=mask_region_na.sum()
)

# ------------------------------------------------------------
# 4. "ENSUCIAR" Edad (tipos y valores imposibles)
# ------------------------------------------------------------
# - ~2% valores faltantes (NaN)
# - ~1% negativos (error de captura)
# - ~1% > 120 (imposible)
# - ~0.5% como texto "desconocida" (rompe el tipo numerico)

edad_col = df["Edad"].astype(object)

mask_na = rng.random(N) < 0.02
mask_neg = (~mask_na) & (rng.random(N) < 0.01)
mask_alta = (~mask_na) & (~mask_neg) & (rng.random(N) < 0.01)
mask_texto = (~mask_na) & (~mask_neg) & (~mask_alta) & (rng.random(N) < 0.005)

edad_col[mask_na] = np.nan
edad_col[mask_neg] = -rng.integers(1, 10, size=mask_neg.sum())
edad_col[mask_alta] = rng.integers(150, 400, size=mask_alta.sum())
edad_col[mask_texto] = "desconocida"

df["Edad"] = edad_col

# ------------------------------------------------------------
# 5. "ENSUCIAR" Precio (numero guardado como texto)
# ------------------------------------------------------------
# - Formato "$1,234.50"
# - ~5% "sin dato"
# - Algunos <= 0 (rompe regla de negocio)

def formatear_precio(valor, r):
    tipo = r.random()
    if tipo < 0.05:
        return "sin dato"
    if tipo < 0.08:
        # precio invalido: negativo o cero
        return f"${-abs(valor):,.2f}"
    if tipo < 0.55:
        return f"${valor:,.2f}"
    # el resto, numero "limpio" pero como string
    return f"{valor:.2f}"

df["Precio"] = [formatear_precio(v, rng) for v in df["Precio"]]

# ------------------------------------------------------------
# 6. "ENSUCIAR" Fecha (formatos mixtos + invalidas)
# ------------------------------------------------------------

MESES_ES = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo",
    6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre",
    10: "Octubre", 11: "Noviembre", 12: "Diciembre",
}

def formatear_fecha(ts, r):
    tipo = r.random()
    if tipo < 0.03:
        return ""  # faltante
    if tipo < 0.06:
        return "32/13/2026"  # fecha imposible
    if tipo < 0.30:
        return ts.strftime("%d/%m/%Y")
    if tipo < 0.55:
        return ts.strftime("%Y-%m-%d")
    if tipo < 0.75:
        return ts.strftime("%m-%d-%Y")
    # formato con mes en texto en espanol (pandas no lo parsea directo)
    return f"{MESES_ES[ts.month]} {ts.day} {ts.year}"

df["Fecha"] = [formatear_fecha(ts, rng) for ts in df["Fecha"]]

# ------------------------------------------------------------
# 7. OUTLIERS en Ventas (valores extremos, no necesariamente error)
# ------------------------------------------------------------

mask_outlier = rng.random(N) < 0.004
df.loc[mask_outlier, "Ventas"] = rng.choice(
    [125000, 98000, 76000], size=mask_outlier.sum()
)

# ------------------------------------------------------------
# 8. NORMALIZAR ALGO DE Producto (inconsistencias leves de texto)
# ------------------------------------------------------------

def ensuciar_producto(valor, r):
    if r.random() < 0.1:
        return valor.upper()
    if r.random() < 0.1:
        return f" {valor}"
    return valor

df["Producto"] = [ensuciar_producto(v, rng) for v in df["Producto"]]

# ------------------------------------------------------------
# 9. DUPLICADOS
# ------------------------------------------------------------
# a) Duplicados EXACTOS: repetir filas completas tal cual.
# b) Duplicados LOGICOS: mismo ID/Cliente, pero con Fecha o
#    Ventas ligeramente distintos (misma entidad, registro repetido).

# a) Exactos (~1.5%)
dup_exactos = df.sample(n=int(N * 0.015), random_state=SEED)

# b) Logicos (~1.5%): mismo ID, cambia la Fecha/Ventas
dup_logicos = df.sample(n=int(N * 0.015), random_state=SEED + 1).copy()
dup_logicos["Ventas"] = (dup_logicos["Ventas"] * rng.uniform(
    0.95, 1.05, size=len(dup_logicos)
)).round(2)

df_final = pd.concat([df, dup_exactos, dup_logicos], ignore_index=True)

# Barajar las filas para que los duplicados no queden todos al final
df_final = df_final.sample(frac=1, random_state=SEED).reset_index(drop=True)

# ------------------------------------------------------------
# 10. GUARDAR CSV
# ------------------------------------------------------------

df_final.to_csv("../datos/ventas_corruptas.csv", index=False)

print("Dataset generado:", df_final.shape)
print(df_final.head())
