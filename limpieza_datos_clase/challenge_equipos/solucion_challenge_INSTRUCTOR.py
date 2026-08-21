# ============================================================
# SOLUCION DEL CHALLENGE - SOLO PARA EL INSTRUCTOR
# NO COMPARTIR CON LOS EQUIPOS ANTES DE TERMINAR EL EJERCICIO
# ============================================================
#
# Esta es la solucion de referencia para "../datos/ventas_challenge.csv"
# (el dataset del Challenge por equipos, distinto al de la demo).
# Te sirve para:
#   - Validar rapido lo que entreguen los equipos.
#   - Tener a la mano los numeros "esperados" (cuantos duplicados,
#     cuantos faltantes, etc.) para el cierre y la validacion.
#
# Estructura identica al pipeline usado en el live coding.
# ============================================================

import pandas as pd

df = pd.read_csv("../datos/ventas_challenge.csv")

# ------------------------------------------------------------
# 1. Auditoria inicial (numeros de referencia)
# ------------------------------------------------------------
print("Shape original:", df.shape)
print(df.isnull().sum())
print("Duplicados exactos:", df.duplicated().sum())
print(df["Region"].value_counts(dropna=False))

# ------------------------------------------------------------
# 2. Texto inconsistente -> Region y Producto
# ------------------------------------------------------------
df["Region"] = df["Region"].str.strip().str.lower()
df["Producto"] = df["Producto"].str.strip().str.title()

# ------------------------------------------------------------
# 3. Tipos incorrectos
# ------------------------------------------------------------
df["Edad"] = pd.to_numeric(df["Edad"], errors="coerce")

df["Precio"] = (
    df["Precio"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)
df["Precio"] = pd.to_numeric(df["Precio"], errors="coerce")

# OJO: formatos de fecha mixtos -> requiere format="mixed"
df["Fecha"] = pd.to_datetime(
    df["Fecha"], errors="coerce", format="mixed", dayfirst=True
)

# ------------------------------------------------------------
# 4. Reglas de negocio / valores imposibles
# ------------------------------------------------------------
df.loc[(df["Edad"] < 0) | (df["Edad"] > 120), "Edad"] = pd.NA
df.loc[df["Precio"] <= 0, "Precio"] = pd.NA

# ------------------------------------------------------------
# 5. Outliers en Ventas (metodo IQR) - solo para IDENTIFICAR,
#    no se eliminan automaticamente (discutir con el grupo si
#    son errores o casos reales extremos)
# ------------------------------------------------------------
Q1 = df["Ventas"].quantile(0.25)
Q3 = df["Ventas"].quantile(0.75)
IQR = Q3 - Q1
lim_inf = Q1 - 1.5 * IQR
lim_sup = Q3 + 1.5 * IQR

outliers = df[(df["Ventas"] < lim_inf) | (df["Ventas"] > lim_sup)]
print("Outliers detectados en Ventas:", len(outliers))

# ------------------------------------------------------------
# 6. Imputacion minima
# ------------------------------------------------------------
df["Edad"] = df["Edad"].fillna(df["Edad"].median())
df["Region"] = df["Region"].fillna("desconocida")

# ------------------------------------------------------------
# 7. Duplicados
# ------------------------------------------------------------
print("Antes de dedup:", df.shape)
df = df.drop_duplicates()
print("Despues de dedup (exactos):", df.shape)

# Duplicados logicos: mismo ID con Ventas ligeramente distintas.
# Se conserva el mas reciente segun Fecha.
df = df.sort_values("Fecha")
df = df.drop_duplicates(subset=["ID"], keep="last")
print("Despues de dedup por ID:", df.shape)

# ------------------------------------------------------------
# 8. Validacion final
# ------------------------------------------------------------
print(df.isnull().sum())
print(df.dtypes)

assert df["Edad"].between(0, 120).all()
assert (df["Precio"].dropna() > 0).all()
assert df.duplicated().sum() == 0

df.to_csv("../datos/ventas_challenge_solucion.csv", index=False)
print("Solucion guardada en ventas_challenge_solucion.csv")
