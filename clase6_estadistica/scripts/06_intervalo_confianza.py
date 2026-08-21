# ============================================================
# 06 - ERROR ESTÁNDAR E INTERVALO DE CONFIANZA
# Dataset: data/datos_generales.csv
# Requiere: haber corrido 00_setup.py (df cargado)
# ============================================================

# ------------------------------------------------------------
# Error estándar manual
#   SE = s / sqrt(n)
# ------------------------------------------------------------

# datos = df["ventas"].dropna()

# s = datos.std()
# n = len(datos)
# se = s / np.sqrt(n)

# print("Desviación estándar:", s)
# print("n:", n)
# print("Error estándar:", se)

# ------------------------------------------------------------
# Intervalo de confianza al 95% con SciPy
# ------------------------------------------------------------

# media = datos.mean()
# sem = stats.sem(datos)

# ic = stats.t.interval(
#     confidence=0.95,
#     df=len(datos) - 1,
#     loc=media,
#     scale=sem
# )

# print("Media:", media)
# print("IC 95%:", ic)

# ------------------------------------------------------------
# ¿Qué pasa con el intervalo si usamos una muestra pequeña
# en lugar de todos los datos? (más ancho = menos precisión)
# ------------------------------------------------------------

# muestra_chica = datos.sample(30, random_state=3)
# media_chica = muestra_chica.mean()
# sem_chica = stats.sem(muestra_chica)

# ic_chica = stats.t.interval(
#     confidence=0.95,
#     df=len(muestra_chica) - 1,
#     loc=media_chica,
#     scale=sem_chica
# )

# print("IC 95% con n=30:", ic_chica)
# print("Ancho n=30:", ic_chica[1] - ic_chica[0])
# print("Ancho con todos los datos:", ic[1] - ic[0])
