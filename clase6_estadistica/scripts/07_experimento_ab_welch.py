# ============================================================
# 07 - CASO PRÁCTICO: EXPERIMENTO A/B (Live Coding)
# Dataset: data/experimento_marketing.csv
# Columnas: id_usuario, grupo (A/B), gasto
#
# Sigue los "Paso 1..7" de la presentación. Ve descomentando
# un bloque a la vez.
# ============================================================

# ------------------------------------------------------------
# Paso 1: cargar el dataset
# ------------------------------------------------------------

# import pandas as pd
# from scipy.stats import ttest_ind

# df = pd.read_csv("data/experimento_marketing.csv")

# print(df.head())
# print(df.shape)
# df.info()

# ------------------------------------------------------------
# Paso 2: descriptiva por grupo
# ------------------------------------------------------------

# resumen = (
#     df.groupby("grupo")["gasto"]
#       .agg(["count", "mean", "median", "std"])
# )
# print(resumen)

# ------------------------------------------------------------
# Paso 3: visualizar
# ------------------------------------------------------------

# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.boxplot(data=df, x="grupo", y="gasto")
# plt.title("Distribucion del gasto por grupo")
# plt.show()

# ------------------------------------------------------------
# Pregunta antes de probar:
# ¿Parece existir una diferencia? Recuerda: una diferencia
# visual no demuestra por sí sola una diferencia estadística.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Paso 4: separar grupos
# ------------------------------------------------------------

# grupo_a = df.loc[df["grupo"] == "A", "gasto"].dropna()
# grupo_b = df.loc[df["grupo"] == "B", "gasto"].dropna()

# print(grupo_a.mean())
# print(grupo_b.mean())

# ------------------------------------------------------------
# Formular hipótesis
#   H0: mu_A = mu_B
#   H1: mu_A != mu_B
# ------------------------------------------------------------

# ------------------------------------------------------------
# Paso 5: Welch t-test
# ------------------------------------------------------------

# t_stat, p_value = ttest_ind(
#     grupo_a,
#     grupo_b,
#     equal_var=False
# )

# print("t-statistic:", t_stat)
# print("p-value:", p_value)

# ------------------------------------------------------------
# Paso 6: decisión estadística
# ------------------------------------------------------------

# alpha = 0.05

# if p_value < alpha:
#     print("Hay evidencia de una diferencia.")
# else:
#     print("No hay evidencia suficiente.")

# ------------------------------------------------------------
# Paso 7: diferencia observada (magnitud)
# ------------------------------------------------------------

# media_a = grupo_a.mean()
# media_b = grupo_b.mean()
# diferencia = media_b - media_a

# print("Media A:", media_a)
# print("Media B:", media_b)
# print("Diferencia:", diferencia)

# ------------------------------------------------------------
# Extra: tamaño del efecto (Cohen's d, con varianza combinada)
# ------------------------------------------------------------

# import numpy as np

# n_a, n_b = len(grupo_a), len(grupo_b)
# s_pooled = np.sqrt(
#     (
#         (n_a - 1) * grupo_a.std(ddof=1) ** 2
#         + (n_b - 1) * grupo_b.std(ddof=1) ** 2
#     )
#     / (n_a + n_b - 2)
# )

# cohen_d = (media_b - media_a) / s_pooled
# print("Cohen's d:", cohen_d)
# print("(referencia orientativa: ~0.2 pequeño, ~0.5 mediano, ~0.8 grande)")
