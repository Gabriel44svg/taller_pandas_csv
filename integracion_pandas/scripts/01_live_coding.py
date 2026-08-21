# ============================================================
# 01_live_coding.py
# Sección: "Live Coding" de la presentación
# Caso de negocio: clientes + ventas + productos
#
# INSTRUCCIONES PARA EL INSTRUCTOR:
# Todo el código está comentado. Ve descomentando bloque por
# bloque (cada bloque corresponde a un slide) y ejecutando con
# los alumnos. Los datos ya están generados en:
#   ../data/live_coding/clientes.csv
#   ../data/live_coding/ventas.csv
#   ../data/live_coding/productos.csv
# ============================================================


# ------------------------------------------------------------
# PASO 1: Cargar las tablas  (slide "Paso 1: cargar")
# ------------------------------------------------------------
import pandas as pd
#
clientes = pd.read_csv("../data/live_coding/clientes.csv")
ventas = pd.read_csv("../data/live_coding/ventas.csv")
productos = pd.read_csv("../data/live_coding/productos.csv")
#
print(clientes.shape)
print(ventas.shape)
print(productos.shape)


# ------------------------------------------------------------
# PASO 2: Revisar claves  (slide "Paso 2: revisar claves")
# ------------------------------------------------------------
print(clientes["id_cliente"].duplicated().sum())
print(productos["id_producto"].duplicated().sum())
#
# Pregunta para el grupo:
# ¿Esperamos 0 duplicados en ambas? ¿Por qué?


# ------------------------------------------------------------
# PASO 3: ventas + clientes  (slide "Paso 3: ventas + clientes")
# ------------------------------------------------------------
df = ventas.merge(
     clientes,
     on="id_cliente",
     how="left",
     validate="many_to_one"
 )

# Pregunta: ¿por qué many_to_one y no one_to_one?
# Porque muchas ventas pueden pertenecer a un solo cliente.


# ------------------------------------------------------------
# PASO 4: Validar filas  (slide "Paso 4: validar filas")
# ------------------------------------------------------------
print(ventas.shape[0])
print(df.shape[0])
#
# Regla: si la relación es many_to_one, el número de filas
# de "ventas" debería mantenerse igual después del merge.


# ------------------------------------------------------------
# PASO 5: Auditar coincidencias  (slide "Paso 5: auditar coincidencias")
# ------------------------------------------------------------
auditoria = ventas.merge(
     clientes,
     on="id_cliente",
     how="left",
     indicator=True
)
#
print(auditoria["_merge"].value_counts())
#
# NOTA: en este dataset hay ventas con id_cliente inventado
# a propósito -> deben aparecer filas "left_only".
# Pídele al grupo que las inspeccione:
# print(auditoria[auditoria["_merge"] == "left_only"])


# ------------------------------------------------------------
# PASO 6: Integrar productos  (slide "Paso 6: integrar productos")
# ------------------------------------------------------------
df = df.merge(
     productos,
     on="id_producto",
     how="left",
     validate="many_to_one"
 )
#
# Ahora df tiene: venta + cliente + producto + precio + categoría


# ------------------------------------------------------------
# PASO 7: Crear la columna "ingreso"  (slide "Paso 7: crear ingreso")
# ------------------------------------------------------------
df["ingreso"] = df["cantidad"] * df["precio"]
#
# NOTA: este dataset también tiene id_producto inventados
# a propósito -> algunos "precio" e "ingreso" quedarán NaN.
# Es el gancho perfecto hacia "Validación 3: nulos".
# print(df["precio"].isna().sum())


# ------------------------------------------------------------
# PREGUNTA 1: ventas por ciudad  (slide "Pregunta 1")
# ------------------------------------------------------------
ventas_ciudad = (
     df.groupby("ciudad")["ingreso"]
       .sum()
       .sort_values(ascending=False)
 )
print(ventas_ciudad)


# ------------------------------------------------------------
# PREGUNTA 2: categoría más importante  (slide "Pregunta 2")
# ------------------------------------------------------------
ventas_categoria = (
     df.groupby("categoria")["ingreso"]
       .sum()
       .sort_values(ascending=False)
 )
print(ventas_categoria)


# ------------------------------------------------------------
# PREGUNTA 3: mejores clientes  (slide "Pregunta 3")
# ------------------------------------------------------------
top_clientes = (
     df.groupby(["id_cliente", "nombre"])["ingreso"]
       .sum()
       .sort_values(ascending=False)
       .head(10)
 )
print(top_clientes)


# ------------------------------------------------------------
# EXTRA : guardar el resultado integrado
# ------------------------------------------------------------
df.to_csv("../data/live_coding/dataset_integrado_live.csv", index=False)
