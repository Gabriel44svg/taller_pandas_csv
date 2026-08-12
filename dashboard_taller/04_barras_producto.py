"""
Gráfica de barras — Ventas por producto
Diapositivas: "Barras con Python" (sección Gráficas categóricas)
              y "Paso 4: ventas por producto" (Live Coding)

Objetivo: comparar categorías (productos) usando barras ordenadas.

Pregunta para el grupo:
¿Qué producto genera más ventas? ¿Y cuál genera menos?
(Luego, en Paso 4: ¿qué producto está impulsando los ingresos?)
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ventas.csv")

# =================================================================
# VERSIÓN 1 — como en la diapositiva "Barras con Python"
# (barras verticales, ordenadas de mayor a menor)
# =================================================================

# PASO A
ventas_producto = (
     df.groupby("Producto")["Ventas"]
       .sum()
       .sort_values(ascending=False)
 )

# PASO B
ventas_producto.plot(kind="bar")
plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Ventas")
plt.tight_layout()
plt.show()

# =================================================================
# VERSIÓN 2 — como en la diapositiva "Paso 4: ventas por producto"
# (barras horizontales, ordenadas de menor a mayor: el líder queda
# arriba, que es más fácil de leer con muchas categorías)
# =================================================================

# PASO C
ventas_producto_h = (
     df.groupby("Producto")["Ventas"]
       .sum()
       .sort_values()
 )
ventas_producto_h.plot(kind="barh")
plt.title("Ventas por producto")
plt.xlabel("Ventas")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------------
# Nota: con este dataset, Laptop debería
# quedar muy por encima del resto (concentra ~60% del ingreso),
# seguido de Monitor. Es el gancho perfecto para la diapositiva
# "Correlación no implica causalidad" / "dependencia de productos
# líderes" que aparece más adelante en la conclusión ejecutiva.
# ---------------------------------------------------------------
