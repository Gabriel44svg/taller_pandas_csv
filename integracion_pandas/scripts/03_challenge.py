# ============================================================
# 03_challenge.py
# Sección: "Data Integration Challenge"
# Reporte nacional de ventas: clientes + ventas + productos + sucursales
#
# INSTRUCCIONES PARA EL INSTRUCTOR:
# Esta es la CLAVE DE RESPUESTAS del challenge, no el material
# que se entrega a los equipos (ellos solo reciben los 4 CSV
# en ../data/challenge/). Está comentada por bloques para que
# la vayas revelando como apoyo, o para resolverlo tú en vivo
# al final si el tiempo lo permite.
#
# El dataset de challenge tiene errores sembrados a propósito:
#   - clientes duplicados (misma fila repetida)
#   - ventas con id_cliente inexistente
#   - ventas con id_producto inexistente
#   - sucursales sin ventas
#   - clientes que nunca compraron
# ============================================================


# ------------------------------------------------------------
# PASO 0: Cargar las 4 fuentes
# ------------------------------------------------------------
# import pandas as pd
#
# clientes = pd.read_csv("../data/challenge/clientes.csv")
# ventas = pd.read_csv("../data/challenge/ventas.csv")
# productos = pd.read_csv("../data/challenge/productos.csv")
# sucursales = pd.read_csv("../data/challenge/sucursales.csv")
#
# print(clientes.shape, ventas.shape, productos.shape, sucursales.shape)


# ------------------------------------------------------------
# PASO 1: Auditar clientes duplicados
# ------------------------------------------------------------
# print(clientes["id_cliente"].duplicated().sum())
# print(clientes[clientes["id_cliente"].duplicated(keep=False)])
#
# clientes_limpios = clientes.drop_duplicates(subset="id_cliente")
# print(clientes_limpios.shape)


# ------------------------------------------------------------
# PASO 2: Auditar ventas con clientes inexistentes
# ------------------------------------------------------------
# auditoria_cli = ventas.merge(
#     clientes_limpios,
#     on="id_cliente",
#     how="left",
#     indicator=True
# )
# print(auditoria_cli["_merge"].value_counts())
#
# ventas_cliente_fantasma = auditoria_cli[
#     auditoria_cli["_merge"] == "left_only"
# ]
# print(ventas_cliente_fantasma[["id_venta", "id_cliente"]])


# ------------------------------------------------------------
# PASO 3: Auditar ventas con productos inexistentes
# ------------------------------------------------------------
# auditoria_prod = ventas.merge(
#     productos,
#     on="id_producto",
#     how="left",
#     indicator=True
# )
# print(auditoria_prod["_merge"].value_counts())
#
# ventas_producto_fantasma = auditoria_prod[
#     auditoria_prod["_merge"] == "left_only"
# ]
# print(ventas_producto_fantasma[["id_venta", "id_producto"]])


# ------------------------------------------------------------
# PASO 4: Construir el dataset integrado (con validate)
# ------------------------------------------------------------
# df = (
#     ventas
#     .merge(clientes_limpios, on="id_cliente", how="left", validate="many_to_one")
#     .merge(productos, on="id_producto", how="left", validate="many_to_one")
#     .merge(sucursales, on="id_sucursal", how="left", validate="many_to_one")
# )
#
# df["ingreso"] = df["cantidad"] * df["precio"]
#
# print(ventas.shape[0], df.shape[0])
# Regla: si todo fue many_to_one, las filas de ventas deben
# mantenerse igual (aunque algunas columnas queden con NaN).


# ------------------------------------------------------------
# PASO 5: Validar nulos introducidos
# ------------------------------------------------------------
# print(df.isna().sum())
#
# Interpretación:
# - nombre / ciudad NaN -> ventas con cliente inexistente
# - producto / categoria / precio NaN -> ventas con producto inexistente


# ------------------------------------------------------------
# PREGUNTA 1: ¿Qué región genera más ingresos?
# ------------------------------------------------------------
# ingresos_region = (
#     df.groupby("region")["ingreso"]
#       .sum()
#       .sort_values(ascending=False)
# )
# print(ingresos_region)


# ------------------------------------------------------------
# PREGUNTA 2: ¿Qué categoría vende más?
# ------------------------------------------------------------
# ingresos_categoria = (
#     df.groupby("categoria")["ingreso"]
#       .sum()
#       .sort_values(ascending=False)
# )
# print(ingresos_categoria)


# ------------------------------------------------------------
# PREGUNTA 3: ¿Cuáles son los 5 clientes con mayor gasto?
# ------------------------------------------------------------
# top5_clientes = (
#     df.groupby(["id_cliente", "nombre"])["ingreso"]
#       .sum()
#       .sort_values(ascending=False)
#       .head(5)
# )
# print(top5_clientes)


# ------------------------------------------------------------
# PREGUNTA 4: ¿Cuántos clientes nunca compraron?
# ------------------------------------------------------------
# clientes_sin_compra = clientes_limpios.merge(
#     ventas[["id_cliente"]].drop_duplicates(),
#     on="id_cliente",
#     how="left",
#     indicator=True
# )
#
# nunca_compraron = clientes_sin_compra[
#     clientes_sin_compra["_merge"] == "left_only"
# ]
# print("Clientes que nunca compraron:", nunca_compraron.shape[0])
# print(nunca_compraron[["id_cliente", "nombre"]])


# ------------------------------------------------------------
# PREGUNTA 5: ¿Existen ventas asociadas a clientes inexistentes?
# ------------------------------------------------------------
# (ya lo calculamos en el PASO 2: ventas_cliente_fantasma)
# print("Ventas con cliente inexistente:", ventas_cliente_fantasma.shape[0])


# ------------------------------------------------------------
# PREGUNTA 6: ¿Qué sucursales nunca realizaron ventas?
# ------------------------------------------------------------
# sucursales_sin_ventas = sucursales.merge(
#     ventas[["id_sucursal"]].drop_duplicates(),
#     on="id_sucursal",
#     how="left",
#     indicator=True
# )
#
# sin_ventas = sucursales_sin_ventas[
#     sucursales_sin_ventas["_merge"] == "left_only"
# ]
# print(sin_ventas[["id_sucursal", "sucursal"]])


# ------------------------------------------------------------
# PASO FINAL: guardar el dataset integrado
# ------------------------------------------------------------
# df.to_csv("../data/challenge/dataset_integrado.csv", index=False)
# print("Archivo guardado: dataset_integrado.csv")


# ------------------------------------------------------------
# RÚBRICA DE REFERENCIA (ver slide "Evaluación del Challenge")
# ------------------------------------------------------------
# Comprensión de tablas        10 pts
# Identificación de claves     15 pts
# Elección correcta del JOIN   15 pts
# Integración                  15 pts
# Registros huérfanos          10 pts
# Cardinalidad                 10 pts
# Preguntas de negocio         15 pts
# Interpretación               10 pts
# Total                       100 pts
