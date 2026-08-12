"""
Generador de datasets para el Taller "Análisis de Datos con Pandas y CSV".

Crea los 3 archivos que se usan a lo largo de la presentación:

    datos/dataset_practica.csv   -> Práctica guiada + Ejercicios 1-6
    datos/ecommerce_data.csv     -> Live Coding (Parte VI)
    datos/ventas_corruptas.csv   -> Reto final (Parte IX)

Cada dataset incluye intencionalmente los problemas de calidad que la
presentación pide detectar y resolver (nulos, duplicados, e-mails
faltantes, inconsistencias de captura, etc.), para que los ejercicios
tengan una respuesta real y no artificial.
"""

import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

# ------------------------------------------------------------------
# 1) dataset_practica.csv
#    Usado en: "Práctica guiada" y Ejercicios 1-6
#    Columnas requeridas por las diapositivas:
#      Nombre, Ciudad, Total_Gastado (Ejercicio 2)
#      Num_Compras, Total_Gastado    (Ejercicio 3)
#      Email                         (Ejercicio 4: eliminar sin correo)
#      variable numérica con nulos   (Ejercicio 4: imputar con media)
#      Membresia, Ciudad             (Ejercicio 5: groupby)
# ------------------------------------------------------------------

n_practica = 250
ciudades = ["CDMX", "Guadalajara", "Monterrey", "Puebla", "Toluca", "Queretaro"]
membresias = ["Bronce", "Plata", "Oro"]
# Probabilidades para que el groupby del Ejercicio 6 tenga sentido de negocio:
# Oro = pocos clientes pero gasto alto; Bronce = muchos clientes, gasto bajo.
membresia_probs = [0.55, 0.30, 0.15]

nombres_pool = [
    "Ana", "Luis", "Sofia", "Carlos", "Maria", "Jorge", "Fernanda", "Diego",
    "Paola", "Ricardo", "Valentina", "Andres", "Camila", "Sergio", "Daniela",
    "Miguel", "Renata", "Pablo", "Ximena", "Hector", "Karla", "Ivan",
    "Lorena", "Emilio", "Natalia",
]

ids_practica = np.arange(1, n_practica + 1)
nombre = rng.choice(nombres_pool, n_practica)
apellido_inicial = rng.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), n_practica)
nombre_completo = [f"{n} {a}." for n, a in zip(nombre, apellido_inicial)]

ciudad = rng.choice(ciudades, n_practica)
edad = rng.integers(18, 65, n_practica).astype(float)

membresia = rng.choice(membresias, n_practica, p=membresia_probs)

# Num_Compras y Total_Gastado correlacionados con la membresía
base_compras = {"Bronce": 3, "Plata": 6, "Oro": 12}
base_gasto = {"Bronce": 900, "Plata": 2200, "Oro": 5000}

num_compras = np.array([
    max(0, int(rng.normal(base_compras[m], 2.5))) for m in membresia
])
total_gastado = np.array([
    max(0, round(rng.normal(base_gasto[m], base_gasto[m] * 0.25), 2))
    for m in membresia
])

email = [
    f"{n.lower()}.{a.lower()}{i}@correo.com" for n, a, i in
    zip(nombre, apellido_inicial, ids_practica)
]

df_practica = pd.DataFrame({
    "ID_Cliente": ids_practica,
    "Nombre": nombre_completo,
    "Ciudad": ciudad,
    "Edad": edad,
    "Email": email,
    "Membresia": membresia,
    "Num_Compras": num_compras,
    "Total_Gastado": total_gastado,
})

# --- Problemas de calidad intencionales ---
# 1) Edad faltante (~6%) -> para practicar fillna(mean)
mask_edad_nula = rng.choice(n_practica, size=int(n_practica * 0.06), replace=False)
df_practica.loc[mask_edad_nula, "Edad"] = np.nan

# 2) Email faltante (~5%) -> para practicar dropna(subset=["Email"])
mask_email_nulo = rng.choice(n_practica, size=int(n_practica * 0.05), replace=False)
df_practica.loc[mask_email_nulo, "Email"] = np.nan

# 3) Duplicados exactos (10 filas repetidas) -> para practicar duplicated()/drop_duplicates()
dup_rows = df_practica.sample(10, random_state=1)
df_practica = pd.concat([df_practica, dup_rows], ignore_index=True)

df_practica = df_practica.sample(frac=1, random_state=7).reset_index(drop=True)
df_practica.to_csv("datos/dataset_practica.csv", index=False)

# ------------------------------------------------------------------
# 2) ecommerce_data.csv
#    Usado en: Live Coding (Parte VI)
#    Columnas requeridas por las diapositivas:
#      Unidades (con nulos -> fillna(0))
#      Total_Gastado (clientes_alto_gasto > 5000)
#      Region, Ingresos (groupby -> region con más ingresos)
# ------------------------------------------------------------------

n_ecommerce = 400
regiones = ["Norte", "Sur", "Centro", "Este", "Oeste"]
region_probs = [0.22, 0.18, 0.30, 0.15, 0.15]
categorias = ["Electronica", "Ropa", "Hogar", "Deportes", "Belleza"]

ids_ecom = np.arange(1, n_ecommerce + 1)
id_cliente_ecom = rng.integers(1000, 1200, n_ecommerce)
region = rng.choice(regiones, n_ecommerce, p=region_probs)
categoria = rng.choice(categorias, n_ecommerce)

unidades = rng.integers(1, 12, n_ecommerce).astype(float)
precio_unitario = np.round(rng.uniform(80, 2500, n_ecommerce), 2)

ingresos = np.round(unidades * precio_unitario, 2)
# Total_Gastado acumulado "por transacción" (para el filtro > 5000 del live coding)
total_gastado = np.round(ingresos * rng.uniform(1.0, 1.8, n_ecommerce), 2)

fechas = pd.to_datetime("2025-01-01") + pd.to_timedelta(
    rng.integers(0, 300, n_ecommerce), unit="D"
)

df_ecommerce = pd.DataFrame({
    "ID_Transaccion": ids_ecom,
    "ID_Cliente": id_cliente_ecom,
    "Region": region,
    "Categoria": categoria,
    "Unidades": unidades,
    "Precio_Unitario": precio_unitario,
    "Ingresos": ingresos,
    "Total_Gastado": total_gastado,
    "Fecha": fechas.strftime("%Y-%m-%d"),
})

# --- Problemas de calidad intencionales ---
# 1) Unidades faltante (~7%) -> df["Unidades"] = df["Unidades"].fillna(0)
mask_unidades_nulas = rng.choice(n_ecommerce, size=int(n_ecommerce * 0.07), replace=False)
df_ecommerce.loc[mask_unidades_nulas, "Unidades"] = np.nan
# Cuando Unidades es nulo, Ingresos también queda como NaN (dato incompleto real)
df_ecommerce.loc[mask_unidades_nulas, "Ingresos"] = np.nan

# 2) Duplicados exactos (15 filas) -> para diagnosticar con duplicated()
dup_rows_ecom = df_ecommerce.sample(15, random_state=2)
df_ecommerce = pd.concat([df_ecommerce, dup_rows_ecom], ignore_index=True)

df_ecommerce = df_ecommerce.sample(frac=1, random_state=9).reset_index(drop=True)
df_ecommerce.to_csv("datos/ecommerce_data.csv", index=False)

# ------------------------------------------------------------------
# 3) ventas_corruptas.csv
#    Usado en: Reto final (Parte IX) - Data Challenge
#    Columnas requeridas por las diapositivas:
#      Unidades_Vendidas (fillna(0))
#      ID_Cliente (dropna -> eliminar registros nulos)
#      Ganancia > 500
#      Region (groupby -> ingresos totales por región)
#    Este archivo debe llegar "sucio" a propósito: nulos, duplicados,
#    inconsistencias de captura (mayúsculas/espacios), tipos mixtos.
# ------------------------------------------------------------------

n_corruptas = 350
sucursales_bien = ["Norte", "Sur", "Centro", "Este", "Oeste"]

ids_corruptas = np.arange(1, n_corruptas + 1)
id_cliente_corr = rng.integers(2000, 2200, n_corruptas).astype(float)
region_corr = rng.choice(sucursales_bien, n_corruptas)
categoria_corr = rng.choice(categorias, n_corruptas)

unidades_vendidas = rng.integers(1, 20, n_corruptas).astype(float)
precio_unitario_corr = np.round(rng.uniform(50, 3000, n_corruptas), 2)
ingresos_corr = np.round(unidades_vendidas * precio_unitario_corr, 2)
costo_corr = np.round(ingresos_corr * rng.uniform(0.5, 0.85, n_corruptas), 2)
ganancia_corr = np.round(ingresos_corr - costo_corr, 2)

fechas_corr = pd.to_datetime("2025-01-01") + pd.to_timedelta(
    rng.integers(0, 300, n_corruptas), unit="D"
)

df_corruptas = pd.DataFrame({
    "ID_Venta": ids_corruptas,
    "ID_Cliente": id_cliente_corr,
    "Region": region_corr,
    "Categoria": categoria_corr,
    "Unidades_Vendidas": unidades_vendidas,
    "Precio_Unitario": precio_unitario_corr,
    "Ingresos": ingresos_corr,
    "Ganancia": ganancia_corr,
    "Fecha": fechas_corr.strftime("%Y-%m-%d"),
})

# --- "Corrupción" intencional de los datos (el reto es detectarla) ---

# 1) ID_Cliente nulo (~4%) -> eliminar con dropna(subset=["ID_Cliente"])
mask_id_nulo = rng.choice(n_corruptas, size=int(n_corruptas * 0.04), replace=False)
df_corruptas.loc[mask_id_nulo, "ID_Cliente"] = np.nan

# 2) Unidades_Vendidas nulo (~8%) -> fillna(0)
mask_unid_nulo = rng.choice(n_corruptas, size=int(n_corruptas * 0.08), replace=False)
df_corruptas.loc[mask_unid_nulo, "Unidades_Vendidas"] = np.nan
df_corruptas.loc[mask_unid_nulo, ["Ingresos", "Ganancia"]] = np.nan

# 3) Inconsistencias de captura en Region (mayúsculas/espacios) -> discusión en clase
idx_sucio = rng.choice(n_corruptas, size=25, replace=False)
variantes = {
    "Norte": [" norte", "NORTE ", "Norte "],
    "Sur": ["sur", "SUR"],
    "Centro": ["centro ", " Centro"],
    "Este": ["este"],
    "Oeste": ["OESTE"],
}
for i in idx_sucio:
    region_original = df_corruptas.loc[i, "Region"]
    opciones = variantes.get(region_original, [region_original.lower()])
    df_corruptas.loc[i, "Region"] = rng.choice(opciones)

# 4) Duplicados exactos (20 filas) -> drop_duplicates()
dup_rows_corr = df_corruptas.sample(20, random_state=3)
df_corruptas = pd.concat([df_corruptas, dup_rows_corr], ignore_index=True)

df_corruptas = df_corruptas.sample(frac=1, random_state=11).reset_index(drop=True)
df_corruptas.to_csv("datos/ventas_corruptas.csv", index=False)

# ------------------------------------------------------------------
print("Listo. Archivos generados en datos/:")
print(" - dataset_practica.csv  ", df_practica.shape)
print(" - ecommerce_data.csv    ", df_ecommerce.shape)
print(" - ventas_corruptas.csv  ", df_corruptas.shape)
