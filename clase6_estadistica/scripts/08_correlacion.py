# ============================================================
# 08 - CORRELACIÓN
# Dataset: data/datos_generales.csv
# Requiere: haber corrido 00_setup.py (df cargado)
# ============================================================

# correlacion = df[["publicidad", "ventas"]].corr()
# print(correlacion)

# ------------------------------------------------------------
# Visualizar la relación
# ------------------------------------------------------------

# sns.scatterplot(data=df, x="publicidad", y="ventas")
# plt.title("Publicidad vs Ventas")
# plt.show()

# ------------------------------------------------------------
# Recordatorio: correlación no implica causalidad.
# Pregunta para el grupo: ¿qué terceras variables podrían
# explicar la relación entre publicidad y ventas, además de
# un efecto directo de la publicidad?
# ------------------------------------------------------------
