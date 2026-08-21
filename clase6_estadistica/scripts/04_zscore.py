# ============================================================
# 04 - Z-SCORE
# Dataset: data/datos_generales.csv
# Requiere: haber corrido 00_setup.py (df cargado)
# ============================================================

# df["z_ventas"] = zscore(
#     df["ventas"].fillna(df["ventas"].mean())
# )

# print(
#     df[["ventas", "z_ventas"]].head()
# )

# ------------------------------------------------------------
# Detección exploratoria de posibles valores extremos
# (|z| > 3 como criterio de referencia, no una regla absoluta)
# ------------------------------------------------------------

# posibles_extremos = df[df["z_ventas"].abs() > 3]
# print(posibles_extremos)

# ------------------------------------------------------------
# Repetir el ejercicio con "ingreso" (recuerden: esta columna
# tiene sesgo positivo a propósito)
# ------------------------------------------------------------

# df["z_ingreso"] = zscore(df["ingreso"])
# extremos_ingreso = df[df["z_ingreso"].abs() > 3]
# print(extremos_ingreso[["id_cliente", "ingreso", "z_ingreso"]])
