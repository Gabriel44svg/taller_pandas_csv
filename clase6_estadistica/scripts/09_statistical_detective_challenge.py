# ============================================================
# 09 - STATISTICAL DETECTIVE CHALLENGE
# Dataset: data/campania_ab.csv
# Columnas: id_usuario, grupo, edad, region, conversion,
#           gasto, tiempo_sitio
#
# Marketing afirma: "La campaña B es mejor que la campaña A."
# Misión de los equipos: determinar si los datos respaldan
# esa afirmación.
#
# Este script es un ESQUELETO guiado (Pasos 1-5 de la
# presentación). Los equipos deben ir descomentando y
# completando lo que falta (marcado con "# TODO").
# ============================================================

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from scipy.stats import ttest_ind

# df = pd.read_csv("data/campania_ab.csv")

# ------------------------------------------------------------
# Paso 1: explorar
#   - tamaño de los grupos
#   - media, mediana, desviación estándar
#   - valores faltantes
#   - posibles outliers
# ------------------------------------------------------------

# print(df.shape)
# df.info()
# print(df.isna().sum())

# resumen = (
#     df.groupby("grupo")["gasto"]
#       .agg(["count", "mean", "median", "std"])
# )
# print(resumen)

# TODO: ¿los tamaños de muestra de A y B son parecidos?
# TODO: ¿qué tan distinta es la media de la mediana en cada grupo?
#       (una gran diferencia entre media y mediana suele ser
#       señal de sesgo u outliers)

# ------------------------------------------------------------
# Paso 2: visualizar
# Cada equipo debe crear al menos una gráfica (boxplot,
# histograma o comparación de medias).
# ------------------------------------------------------------

# sns.boxplot(data=df, x="grupo", y="gasto")
# plt.title("Distribucion del gasto por grupo")
# plt.show()

# TODO: probar también un histograma por grupo, por ejemplo:
# sns.histplot(data=df, x="gasto", hue="grupo", kde=True)
# plt.show()

# ------------------------------------------------------------
# Paso 3: formular hipótesis
#   H0: mu_A = mu_B
#   H1: mu_A != mu_B
# Explicar en lenguaje de negocio qué significaría cada una.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Paso 4: realizar la prueba (Welch t-test)
# Reportar: estadístico t, valor p, alpha, decisión.
# ------------------------------------------------------------

# grupo_a = df.loc[df["grupo"] == "A", "gasto"].dropna()
# grupo_b = df.loc[df["grupo"] == "B", "gasto"].dropna()

# t_stat, p_value = ttest_ind(grupo_a, grupo_b, equal_var=False)
# alpha = 0.05

# print("t-statistic:", t_stat)
# print("p-value:", p_value)

# if p_value < alpha:
#     print("Hay evidencia de una diferencia.")
# else:
#     print("No hay evidencia suficiente.")

# ------------------------------------------------------------
# Paso 5: medir la diferencia
# No basta con reportar el valor p; hay que calcular la
# magnitud y preguntarse si es relevante para el negocio.
# ------------------------------------------------------------

# diferencia = grupo_b.mean() - grupo_a.mean()
# print("Diferencia de medias:", diferencia)

# TODO: comparar también la diferencia de MEDIANAS.
# diferencia_mediana = grupo_b.median() - grupo_a.median()
# print("Diferencia de medianas:", diferencia_mediana)

# TODO (pista para el equipo): investiguen si un pequeño
# número de observaciones con gasto muy alto en algún grupo
# está influyendo desproporcionadamente en la media. Pueden
# revisar los valores más altos con:
# print(df.sort_values("gasto", ascending=False).head(10))

# ------------------------------------------------------------
# Formato de entrega (recordatorio):
#   1. pregunta
#   2. hipótesis
#   3. resumen descriptivo
#   4. visualización
#   5. prueba estadística
#   6. valor p
#   7. diferencia observada
#   8. interpretación
#   9. recomendación
# ------------------------------------------------------------
