"""
mi_analisis.py
Taller: Análisis de Datos con Pandas y CSV

Aquí trabajarás durante la práctica guiada y los ejercicios.
Ejecuta este archivo desde la raíz del proyecto con:

    python mi_analisis.py

(recuerda tener el entorno virtual activado)
"""

import pandas as pd

print("\n" + "="*50)
print("INICIANDO PRÁCTICA GUIADA Y EJERCICIOS")
print("="*50)

# Paso 1: Cargar los datos
df = pd.read_csv("datos/dataset_practica.csv")

#print("\n--- Primeras 5 filas del dataset ---")
#print(df.head())

# EJERCICIO 1: Exploración
#print("\n--- Primeras 10 y últimas 5 filas ---")
#print(df.head(10))
#print(df.tail(5))

#print("\n--- Dimensiones ---")
#print(df.shape)

#print("\n--- Columnas y Tipos de datos ---")
#print(df.columns)
#print(df.dtypes)

#print("\n--- Información General ---")
#df.info()

#print("\n--- Estadística Descriptiva ---")
#print(df.describe())

# ============================================================
# CALIDAD DE DATOS (Previo a la limpieza)
# ============================================================
# print("\n--- Valores Nulos ---")
# print(df.isna().sum())

# print("\n--- Registros Duplicados ---")
# print(df.duplicated().sum())

# ============================================================
# EJERCICIO 4: Limpieza
# ============================================================
# 1. Eliminar registros sin correo
# df = df.dropna(subset=["Email"])

# 2. Imputar variable numérica (Edad) utilizando la media
# df["Edad"] = df["Edad"].fillna(df["Edad"].mean())

# 3. Eliminar duplicados
# df = df.drop_duplicates()

#print("\n--- Revisión post-limpieza ---")
#print(df.isna().sum())
#print(f"Duplicados restantes: {df.duplicated().sum()}")
#print(f"Nuevas dimensiones: {df.shape}")

# ============================================================
# EJERCICIO 2: Selección
# ============================================================
# subset_gastos = df[["Nombre", "Ciudad", "Total_Gastado"]]
# print("\n--- Subset Seleccionado (Primeras 10 filas) ---")
# print(subset_gastos.head(10))

# gasto_prom = subset_gastos["Total_Gastado"].mean()
# gasto_max = subset_gastos["Total_Gastado"].max()
# print(f"\nGasto Promedio: ${gasto_prom:.2f}")
# print(f"Gasto Máximo: ${gasto_max:.2f}")

# ============================================================
# EJERCICIO 3: Filtros
# ============================================================
#compras_altas = df[df["Num_Compras"] > 5]
#print(compras_altas.head())

#gasto_alto = df[df["Total_Gastado"] > 3000]
#print(gasto_alto.head())

#clientes_cdmx = df[df["Ciudad"] == "CDMX"]
#print(clientes_cdmx.head())

#Filtro Combinado: Más de 5 compras Y gasto mayor a $3000
#filtro_combinado = df[(df["Num_Compras"] > 5) & (df["Total_Gastado"] > 3000)]
#print("\n--- Clientes estrella (Filtro combinado) ---")
#print(filtro_combinado.head())

# ============================================================
# EJERCICIO 5: Groupby
# ============================================================
# 1. Gasto promedio por membresía
gasto_membresia = df.groupby("Membresia")["Total_Gastado"].mean().sort_values(ascending=False)
print("\n--- Gasto promedio por membresía ---")
print(gasto_membresia)

# 2. Número de clientes por ciudad
# clientes_ciudad = df.groupby("Ciudad")["ID_Cliente"].count().sort_values(ascending=False)
# print("\n--- Clientes por ciudad ---")
# print(clientes_ciudad)

# 3. Gasto total por ciudad
# gasto_total_ciudad = df.groupby("Ciudad")["Total_Gastado"].sum().sort_values(ascending=False)
# print("\n--- Ingresos totales por ciudad ---")
# print(gasto_total_ciudad)


# ============================================================
# ============================================================
# RETO FINAL: DATA CHALLENGE (ventas_corruptas.csv)
# ============================================================
# ============================================================

# print("\n" + "="*50)
# print("INICIANDO RETO FINAL: VENTAS CORRUPTAS")
# print("="*50)

# df_reto = pd.read_csv("datos/ventas_corruptas.csv")

# ------------------------------------------------------------
# Reto Parte 1: Inspección Inicial
# ------------------------------------------------------------
# print("\n--- Dimensiones y Nulos iniciales del Reto ---")
# print(df_reto.shape)
# print(df_reto.isna().sum())
# print(f"Duplicados encontrados: {df_reto.duplicated().sum()}")

# ------------------------------------------------------------
# Reto Parte 2: Limpieza
# ------------------------------------------------------------
# 1. Rellenar Unidades_Vendidas con 0
# df_reto["Unidades_Vendidas"] = df_reto["Unidades_Vendidas"].fillna(0)

# 2. Eliminar registros con ID_Cliente nulo
# df_reto = df_reto.dropna(subset=["ID_Cliente"])

# 3. Eliminar duplicados
# df_reto = df_reto.drop_duplicates()

# print("\n--- Nulos después de la limpieza ---")
# print(df_reto.isna().sum())

# ------------------------------------------------------------
# Reto Parte 3: Filtro > $500
# ------------------------------------------------------------
# ganancias_altas = df_reto[df_reto["Ganancia"] > 500]
# print(f"\nTransacciones con ganancia > $500: {len(ganancias_altas)}")

# ------------------------------------------------------------
# Reto Parte 4: Agrupación (Ingresos por región)
# ------------------------------------------------------------
# TRUCO DE LIMPIEZA DE TEXTO: Las regiones vienen sucias (espacios, mayúsculas)
# Observa lo que pasa si agrupamos directamente vs si limpiamos primero:

# print("\n--- Ingresos por región (SIN LIMPIAR TEXTO) ---")
# agrupacion_sucia = df_reto.groupby("Region")["Ingresos"].sum().sort_values(ascending=False)
# print(agrupacion_sucia)

# Limpiamos quitando espacios en blanco (strip) y estandarizando a capital (capitalize)
# df_reto["Region"] = df_reto["Region"].str.strip().str.capitalize()

# print("\n--- Ingresos por región (TEXTO LIMPIO) ---")
# ingresos_region = df_reto.groupby("Region")["Ingresos"].sum().sort_values(ascending=False)
# print(ingresos_region)