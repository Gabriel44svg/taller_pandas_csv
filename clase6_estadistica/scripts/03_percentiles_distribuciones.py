# ============================================================
# 03 - PERCENTILES Y DISTRIBUCIONES
# Dataset: data/datos_generales.csv
# Requiere: haber corrido 00_setup.py (df cargado)
# ============================================================

# ------------------------------------------------------------
# Percentiles / cuartiles
# ------------------------------------------------------------

# q1 = df["ventas"].quantile(0.25)
# mediana = df["ventas"].quantile(0.50)
# q3 = df["ventas"].quantile(0.75)
# p95 = df["ventas"].quantile(0.95)

# print(q1, mediana, q3, p95)

# ------------------------------------------------------------
# Interpretación: ¿en qué percentil de "ingreso" está un
# cliente con ingreso == 50000?
# ------------------------------------------------------------

# import scipy.stats as stats
# percentil_cliente = stats.percentileofscore(
#     df["ingreso"].dropna(), 50000
# )
# print(percentil_cliente)

# ------------------------------------------------------------
# Visualizar la distribución de "ventas"
# ------------------------------------------------------------

# sns.histplot(
#     data=df,
#     x="ventas",
#     kde=True
# )
# plt.title("Distribucion de ventas")
# plt.show()

# ------------------------------------------------------------
# Visualizar la distribución de "ingreso" (sesgada a la
# derecha por diseño) para comparar forma con "ventas"
# ------------------------------------------------------------

# sns.histplot(
#     data=df,
#     x="ingreso",
#     kde=True
# )
# plt.title("Distribucion de ingreso (con sesgo)")
# plt.show()

# print("media ingreso:", df["ingreso"].mean())
# print("mediana ingreso:", df["ingreso"].median())
# print("¿media > mediana? -> señal de sesgo positivo")
