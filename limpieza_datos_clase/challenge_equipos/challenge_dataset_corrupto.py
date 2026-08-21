# ============================================================
# DATA CLEANING CHALLENGE
# Diplomado en Analisis de Datos - Universidad Marista
# ============================================================
#
# Este es el archivo que se le entrega a los EQUIPOS.
# A proposito NO trae pistas de donde estan los problemas: es
# igual para todos los equipos y usa "../datos/ventas_challenge.csv"
# (un dataset corrupto DISTINTO al que se uso en el live coding,
# para que no puedan copiar la solucion de la demo).
#
# Tienen 25 minutos. Deben encontrar y corregir:
#   1. Valores faltantes
#   2. Duplicados
#   3. Categorias inconsistentes
#   4. Espacios ocultos
#   5. Tipos incorrectos
#   6. Fechas invalidas
#   7. Valores imposibles
#   8. Outliers
#   9. Reglas de negocio incumplidas
#
# Regla: cada modificacion debe poder justificarse.
# No gana quien elimine mas datos, gana quien tome mejores
# decisiones.
# ============================================================

import pandas as pd

df = pd.read_csv("../datos/ventas_challenge.csv")

# ------------------------------------------------------------
# Pistas de comandos utiles (descomenten los que necesiten)
# ------------------------------------------------------------

# df.info()
# df.describe(include="all")
# df.isnull().sum()
# df.duplicated().sum()
# df.nunique()
# df["Region"].value_counts(dropna=False)
# df.sort_values("Ventas").head()
# df.sort_values("Ventas").tail()

# ------------------------------------------------------------
# Espacio para su limpieza:
# ------------------------------------------------------------


# ------------------------------------------------------------
# Al final, guarden su resultado:
# ------------------------------------------------------------

# df.to_csv("../datos/ventas_challenge_limpio.csv", index=False)
