"""
Histograma — Distribución de las ventas
Diapositiva: "Histograma en Python" (sección Distribuciones)

Objetivo: ver cómo se distribuyen los montos de venta por
transacción (no el total, sino cada fila del CSV).

Diapositiva dice:
"No basta con decir 'la mayoría está entre 500 y 1000'.
Pregúntate: ¿qué decisión podría cambiar gracias a esta distribución?"
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ventas.csv")

# DESCOMENTAR PASO A
plt.hist(
     df["Ventas"],
     bins=20,
     edgecolor="black"
 )
plt.title("Distribucion de las ventas")
plt.xlabel("Ventas")
plt.ylabel("Frecuencia")
plt.show()

# ---------------------------------------------------------------
# EXTRA opcional — comparar la distribución por producto con un
# boxplot, para conectar directamente con la diapositiva de
# "Boxplot: el detector de sospechosos".
# ---------------------------------------------------------------

# EXTRA
# df.boxplot(column="Ventas", by="Producto", rot=45)
# plt.title("Distribucion de ventas por producto")
# plt.suptitle("")
# plt.ylabel("Ventas")
# plt.tight_layout()
# plt.show()
#
# Con este dataset, Laptop va a mostrar la dispersión más grande
# (por su precio alto) y probablemente algunos outliers hacia
# arriba: transacciones con Cantidad=2 en el mismo día de campaña.
