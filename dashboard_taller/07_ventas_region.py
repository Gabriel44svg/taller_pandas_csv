"""
PASO 6 — Ventas por región
Diapositiva: "Paso 6: ventas por región"

Objetivo: comparar el desempeño entre regiones (¿dónde ocurre?).
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ventas.csv")

# PASO A
ventas_region = (
     df.groupby("Region")["Ventas"]
       .sum()
       .sort_values()
 )
ventas_region.plot(kind="barh")
plt.title("Ventas por region")
plt.xlabel("Ventas")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------------
# Nota: en el TOTAL acumulado del periodo, Sur
# no se ve como la región más débil (arrancó fuerte y solo cae al
# final). Ese es justo el punto pedagógico: una barra de "total"
# puede esconder una tendencia reciente preocupante. Por eso el
# Paso 5 (evolución semanal por región) es el que realmente
# destapa el problema, no esta barra sola.
# ---------------------------------------------------------------
