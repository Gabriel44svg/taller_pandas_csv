# ============================================================
# 00 - SETUP
# Clase 6 - Estadística para Data Science
# Diplomado de Python y Análisis de Datos - Universidad Marista
# ============================================================
#
# Ejecuta este bloque al inicio de la clase para dejar listo el
# entorno. El resto de los scripts (01, 02, 03, ...) asumen que
# ya corriste esto y que "df" está disponible.
#
# Ve descomentando línea por línea (o bloque por bloque) según
# avances en la presentación.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.stats import zscore, ttest_ind

sns.set_theme(style="whitegrid")

df = pd.read_csv("data/datos_generales.csv")

print(df.head())
print(df.shape)
df.info()
