"""
PASO 5 — Tendencia temporal
Diapositiva: "Paso 5: tendencia temporal"

Objetivo: ver cómo evolucionan las ventas en el tiempo (tendencia,
picos, caídas), no solo el total acumulado.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ventas.csv", parse_dates=["Fecha"])

# =================================================================
# VERSIÓN 1 — diaria, tal como en la diapositiva
# =================================================================

# PASO A
ventas_fecha = (
     df.groupby("Fecha")["Ventas"]
       .sum()
 )
ventas_fecha.plot(kind="line", marker="o")
plt.title("Evolucion de ventas")
plt.xlabel("Fecha")
plt.ylabel("Ventas")
plt.grid(alpha=0.3)
plt.show()

# ---------------------------------------------------------------
# Nota: a nivel diario la serie se ve "ruidosa" (mucho zig-zag).
# Es un buen momento para preguntar al grupo: ¿cómo suavizamos
# esto para ver la tendencia real?
# ---------------------------------------------------------------

# =================================================================
# VERSIÓN 2 — semanal (más clara para ver la tendencia y la caída
# de la región Sur en las últimas semanas)
# =================================================================

# PASO B
ventas_semana = (
     df.set_index("Fecha")["Ventas"]
       .resample("W")
       .sum()
 )
ventas_semana.plot(kind="line", marker="o")
plt.title("Evolucion semanal de ventas")
plt.xlabel("Semana")
plt.ylabel("Ventas")
plt.grid(alpha=0.3)
plt.show()

# =================================================================
# VERSIÓN 3 — el "insight" de la sesión: comparar la tendencia de
# la región Sur contra el resto, para encontrar la caída sostenida
# de las últimas 4 semanas .
# =================================================================

# PASO C
pivote_region = (
     df.set_index("Fecha")
       .groupby("Region")["Ventas"]
       .resample("W")
       .sum()
       .unstack("Region")
 )
pivote_region.plot(kind="line", marker="o")
plt.title("Evolucion semanal de ventas por region")
plt.xlabel("Semana")
plt.ylabel("Ventas")
plt.legend(title="Region")
plt.grid(alpha=0.3)
plt.show()
#
# Pregunta al grupo: ¿qué región se despega del resto en las
# últimas semanas... para bien o para mal?
