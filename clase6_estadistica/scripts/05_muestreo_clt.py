# ============================================================
# 05 - MUESTREO, LEY DE LOS GRANDES NÚMEROS
#      Y TEOREMA CENTRAL DEL LÍMITE (simulación)
# Dataset: data/datos_generales.csv
# Requiere: haber corrido 00_setup.py (df cargado)
# ============================================================

# ------------------------------------------------------------
# Tomar una muestra con Pandas
# ------------------------------------------------------------

# muestra = df.sample(
#     n=100,
#     random_state=42
# )

# media = muestra["ventas"].mean()
# print(media)

# ------------------------------------------------------------
# Cambiar la muestra (misma población, distinta semilla)
# ------------------------------------------------------------

# muestra_1 = df.sample(n=100, random_state=42)
# muestra_2 = df.sample(n=100, random_state=7)

# print(muestra_1["ventas"].mean())
# print(muestra_2["ventas"].mean())

# ------------------------------------------------------------
# Comparar distintos tamaños de muestra
# (Ley de los Grandes Números: al aumentar n, la media
# muestral tiende a estabilizarse cerca de la media
# poblacional)
# ------------------------------------------------------------

# m10 = df.sample(10, random_state=1)["ventas"].mean()
# m100 = df.sample(100, random_state=1)["ventas"].mean()
# m1000 = df.sample(1000, random_state=1)["ventas"].mean()

# print("n=10:", m10)
# print("n=100:", m100)
# print("n=1000:", m1000)
# print("población completa:", df["ventas"].mean())

# ------------------------------------------------------------
# Simulando el Teorema Central del Límite
# Población deliberadamente NO normal (exponencial), para
# mostrar que la distribución de medias muestrales sí lo es.
# ------------------------------------------------------------

# poblacion = np.random.exponential(
#     scale=10,
#     size=100000
# )

# medias = []

# for _ in range(5000):
#     muestra = np.random.choice(poblacion, size=50)
#     medias.append(muestra.mean())

# plt.hist(medias, bins=40)
# plt.title("Distribucion de medias muestrales")
# plt.xlabel("Media")
# plt.ylabel("Frecuencia")
# plt.show()

# ------------------------------------------------------------
# Variante: repetir la simulación anterior pero usando la
# columna "ingreso" del propio dataset (que también tiene
# sesgo) como población de origen.
# ------------------------------------------------------------

# poblacion_ingreso = df["ingreso"].dropna().values

# medias_ingreso = []
# for _ in range(5000):
#     muestra = np.random.choice(poblacion_ingreso, size=50)
#     medias_ingreso.append(muestra.mean())

# plt.hist(medias_ingreso, bins=40)
# plt.title("CLT aplicado a 'ingreso' (población sesgada)")
# plt.show()
