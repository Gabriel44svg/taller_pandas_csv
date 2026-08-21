# ============================================================
# LIMPIEZA DE DATOS - Dataset Corrupto
# Diplomado en Analisis de Datos - Universidad Marista
# ============================================================
#
# COMO USAR ESTE ARCHIVO EN CLASE:
#
# Todo el codigo real esta escrito pero COMENTADO (con "#").
# Cada bloque corresponde a una seccion/slide del PDF.
# Durante la sesion, ve descomentando linea por linea (o bloque
# por bloque) y ejecutando, para que el codigo "aparezca" en vivo.
#
# Sugerencia de flujo:
#   - Corre este archivo celda por celda si usas Jupyter/VSCode
#     (cada bloque "# %%" es una celda), o
#   - Cópialo en un notebook y descomenta ahí.
#
# El dataset "../datos/ventas_corruptas.csv" ya viene generado.
# ============================================================

import pandas as pd

# %% ==========================================================
# SECCION 1 - PRIMER CONTACTO CON EL DATASET
# ==============================================================

df = pd.read_csv("../datos/ventas_corruptas.csv")

#print(df.head())
#print(df.shape)
#print(df.columns)
#print(df.dtypes)

# Pregunta al grupo:
# ¿Que problemas pueden detectar solo observando esta salida?


# %% ==========================================================
# SECCION 2 - AUDITORIA (df.info, describe, value_counts)
# ==============================================================

#df.info()

# Estadistica descriptiva numerica
#df.describe()

# Estadistica descriptiva de columnas tipo texto/objeto
#df.describe(include="object")

# Revisar categorias de una columna categorica
#df["Region"].value_counts(dropna=False)

# Auditoria completa (lo que se usa en el Paso 2 del live coding)
#print(df.isnull().sum())
#print(df.duplicated().sum())
#print(df.describe(include="all"))
#print(df["Region"].value_counts(dropna=False))


# %% ==========================================================
# SECCION 3 - VALORES FALTANTES: DETECCION
# ==============================================================

# Conteo de nulos por columna
#df.isnull().sum()

# Porcentaje de nulos por columna
#porcentaje = df.isnull().mean() * 100
#print(porcentaje)


# %% ==========================================================
# SECCION 4 - VALORES FALTANTES: ELIMINAR
# ==============================================================

# Eliminar TODAS las filas con al menos un faltante (usar con cuidado)
# df_sin_na = df.dropna()

# Eliminar solo cuando falta una variable critica, ej. Ventas
#df_sin_na_ventas = df.dropna(subset=["Ventas"])

# Eliminar columnas completas (cuidado: se pierde informacion)
# df_sin_columnas_na = df.dropna(axis=1)


# %% ==========================================================
# SECCION 5 - VALORES FALTANTES: IMPUTACION
# ==============================================================

# Imputar con la media (ejemplo generico con una columna numerica)
#df["Edad"] = df["Edad"].fillna(df["Edad"].mean())

# Imputar con la mediana (mas robusta ante valores extremos)
#df["Precio"] = df["Precio"].fillna(df["Precio"].median())

# Imputar categorica con la moda
#moda = df["Region"].mode()[0]
#df["Region"] = df["Region"].fillna(moda)


# %% ==========================================================
# SECCION 6 - DUPLICADOS: DETECCION Y ELIMINACION
# ==============================================================

# Mascara booleana de duplicados
#df.duplicated()

# Contar duplicados exactos
#df.duplicated().sum()

# Ver las filas duplicadas
#df[df.duplicated()]

# Eliminar duplicados exactos
#df = df.drop_duplicates()

# Duplicados usando una clave especifica (ej. mismo ID)
#df.duplicated(subset=["ID"])

# Duplicados usando varias columnas como clave logica
#df.duplicated(subset=["Cliente", "Fecha", "Producto"])

# Conservar el registro mas reciente por ID
#df = df.sort_values("Fecha")
#df = df.drop_duplicates(subset=["ID"], keep="last")

# Pregunta al grupo:
# ¿Que define realmente un registro unico en este negocio?


# %% ==========================================================
# SECCION 7 - TEXTO INCONSISTENTE: NORMALIZACION BASICA
# ==============================================================

# Quitar espacios al inicio/final
# df["Region"] = df["Region"].str.strip()

# Todo a minusculas
# df["Region"] = df["Region"].str.lower()

# Todo a mayusculas
# df["Region"] = df["Region"].str.upper()

# Formato tipo "Titulo"
# df["Region"] = df["Region"].str.title()


# %% ==========================================================
# SECCION 8 - TEXTO: REEMPLAZAR CATEGORIAS EQUIVALENTES
# ==============================================================
# Ejemplo generico (adaptar los valores reales que aparezcan
# despues de inspeccionar value_counts en la columna Producto)

#mapa = {
#     "CDMX": "Ciudad de Mexico",
#     "DF": "Ciudad de Mexico",
#     "Mexico DF": "Ciudad de Mexico",
# }
# df["Ciudad"] = df["Ciudad"].replace(mapa)


# %% ==========================================================
# SECCION 9 - TEXTO: AUDITAR ANTES Y DESPUES
# ==============================================================

# Antes de limpiar
# df["Region"].value_counts()

# Limpiamos
# df["Region"] = (
#     df["Region"]
#     .str.strip()
#     .str.lower()
# )

# Despues de limpiar
# df["Region"].value_counts()


# %% ==========================================================
# SECCION 10 - TIPOS DE DATOS: CONVERSION SEGURA
# ==============================================================

# Esto puede FALLAR si hay texto no numerico como "desconocida":
#df["Edad"] = df["Edad"].astype(int, errors="ignore")  # no falla, pero deja la columna como object

# Estrategia segura: forzar a numerico, lo invalido se vuelve NaN
#df["Edad"] = pd.to_numeric(df["Edad"], errors="coerce")

# Igual con Precio (ojo: primero hay que quitar "$" y ",")
# df["Precio"] = (
#     df["Precio"]
#     .astype(str)
#     .str.replace("$", "", regex=False)
#     .str.replace(",", "", regex=False)
# )
# df["Precio"] = pd.to_numeric(df["Precio"], errors="coerce")


# %% ==========================================================
# SECCION 11 - FECHAS
# ==============================================================

#df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")

# Cuantas fechas no se pudieron convertir
#df["Fecha"].isnull().sum()

# --------------------------------------------------------------
# GOTCHA REAL para mostrar en vivo:
# Si esta columna mezcla formatos (dd/mm/yyyy, yyyy-mm-dd,
# mm-dd-yyyy...), pandas moderno (2.x) puede fallar en convertir
# la mayoria de las filas con la linea de arriba, porque intenta
# inferir UN SOLO formato para toda la columna.
#
# La correccion es indicar format="mixed" (y dayfirst=True si la
# mayoria de las fechas vienen en formato dia/mes/anio):
# --------------------------------------------------------------

# df["Fecha"] = pd.to_datetime(
#     df["Fecha"],
#     errors="coerce",
#     format="mixed",
#     dayfirst=True,
# )
# df["Fecha"].isnull().sum()

# Con esto, los unicos NaT que quedan son los realmente invalidos
# (fecha vacia, "32/13/2026", o el mes escrito en texto en
# espanol como "Agosto 10 2026", que pandas no reconoce).


# %% ==========================================================
# SECCION 12 - OUTLIERS: REGLAS DE NEGOCIO
# ==============================================================

# Filas con Edad negativa
# df[df["Edad"] < 0]

# Filas con Edad mayor a 120
# df[df["Edad"] > 120]

# Combinando reglas
#invalidos = df[
#     (df["Edad"] < 0) |
#     (df["Edad"] > 120)
# ]
#print(invalidos)


# %% ==========================================================
# SECCION 13 - OUTLIERS: METODO IQR
# ==============================================================

#Q1 = df["Ventas"].quantile(0.25)
#Q3 = df["Ventas"].quantile(0.75)
#IQR = Q3 - Q1

#lim_inf = Q1 - 1.5 * IQR
#lim_sup = Q3 + 1.5 * IQR

#outliers = df[
#     (df["Ventas"] < lim_inf) |
#     (df["Ventas"] > lim_sup)
# ]
#print(outliers)


# ==============================================================
# ==============================================================
#   LIVE CODING COMPLETO: "Dataset Corrupto"
#   (Pasos 1-8 tal como aparecen en el PDF, ya integrados
#    para correr de principio a fin sobre ../datos/ventas_corruptas.csv)
# ==============================================================
# ==============================================================

# %% --- Paso 1: cargar -----------------------------------------

# import pandas as pd
#
# df = pd.read_csv("../datos/ventas_corruptas.csv")
#
# print(df.head())
# print(df.shape)
#
# df.info()

# Pregunta al grupo:
# ¿Que problemas pueden detectar solamente observando la salida?


# %% --- Paso 2: auditoria ----------------------------------------

# print(df.isnull().sum())
#
# print(df.duplicated().sum())
#
# print(df.describe(include="all"))
#
# print(df["Region"].value_counts(dropna=False))

# Consejo: crear una lista de problemas antes de empezar a corregir.


# %% --- Paso 3: limpiar texto --------------------------------------

# df["Region"] = (
#     df["Region"]
#     .str.strip()
#     .str.lower()
# )
#
# df["Producto"] = (
#     df["Producto"]
#     .str.strip()
#     .str.title()
# )

# Volvemos a inspeccionar:
# print(df["Region"].value_counts())


# %% --- Paso 4: convertir variables ---------------------------------

# df["Edad"] = pd.to_numeric(df["Edad"], errors="coerce")
#
# df["Precio"] = (
#     df["Precio"]
#     .astype(str)
#     .str.replace("$", "", regex=False)
#     .str.replace(",", "", regex=False)
#     .str.strip()
# )
# df["Precio"] = pd.to_numeric(df["Precio"], errors="coerce")
#
# df["Fecha"] = pd.to_datetime(
#     df["Fecha"],
#     errors="coerce",
#     format="mixed",
#     dayfirst=True,
# )

# Observacion importante:
# Convertir tipos puede crear nuevos valores faltantes.
# Por eso debemos auditar nuevamente (repetir Paso 2).
#
# Nota sobre Fecha: si aqui usan pd.to_datetime SIN format="mixed",
# van a ver que casi todas las fechas se vuelven NaT porque la
# columna mezcla formatos (dd/mm/yyyy, yyyy-mm-dd, mm-dd-yyyy).
# Es un excelente momento para detenerse y discutirlo con el grupo.


# %% --- Paso 5: reglas de negocio ------------------------------------

# df.loc[
#     (df["Edad"] < 0) |
#     (df["Edad"] > 120),
#     "Edad"
# ] = pd.NA
#
# df.loc[
#     df["Precio"] <= 0,
#     "Precio"
# ] = pd.NA

# Ahora los valores imposibles pasan a ser problemas explicitos (NaN).


# %% --- Paso 6: imputar ------------------------------------------------

# mediana_edad = df["Edad"].median()
# df["Edad"] = df["Edad"].fillna(mediana_edad)
#
# df["Region"] = df["Region"].fillna("desconocida")

# Pregunta: ¿tiene sentido hacer esto para TODAS las columnas?
# No necesariamente (ej. Ventas o Precio quiza no deban imputarse
# igual, hay que decidirlo con criterio de negocio).


# %% --- Paso 7: duplicados -----------------------------------------------

# print("Antes:", df.shape)
#
# df = df.drop_duplicates()
#
# print("Despues:", df.shape)

# Si tenemos un identificador de negocio (ID), mejor usarlo como clave:
# df = df.drop_duplicates(subset=["ID"], keep="last")

# La decision depende de que representa el ID en este negocio.


# %% --- Paso 8: guardar --------------------------------------------------

df.to_csv("../datos/ventas_limpias.csv", index=False)

# ¿Terminamos? No. Falta VALIDAR.


# ==============================================================
# VALIDACION
# ==============================================================

# %% --- Validacion automatica --------------------------------------------

# print(df.shape)
# print(df.isnull().sum())
# print(df.duplicated().sum())
# print(df.dtypes)
# print(df.describe())

# Convertir reglas de negocio en pruebas automaticas:
# assert df["Edad"].between(0, 120).all()
# assert (df["Precio"] > 0).all()
# assert df.duplicated().sum() == 0


# %% --- Comparar antes vs despues -----------------------------------------

# filas_antes = 10300  # shape original de ../datos/ventas_corruptas.csv
# filas_despues = len(df)
# eliminadas = filas_antes - filas_despues
# print("Filas eliminadas:", eliminadas)


# ==============================================================
# DE NOTEBOOK A FUNCION (PIPELINE REPRODUCIBLE)
# ==============================================================

# %% --- Funcion limpiar_datos ---------------------------------------------

# def limpiar_datos(df):
#
#     df = df.copy()
#
#     # 1. Duplicados exactos
#     df = df.drop_duplicates()
#
#     # 2. Texto
#     df["Region"] = (
#         df["Region"]
#         .str.strip()
#         .str.lower()
#     )
#
#     # 3. Tipos
#     df["Edad"] = pd.to_numeric(df["Edad"], errors="coerce")
#     df["Precio"] = (
#         df["Precio"]
#         .astype(str)
#         .str.replace("$", "", regex=False)
#         .str.replace(",", "", regex=False)
#     )
#     df["Precio"] = pd.to_numeric(df["Precio"], errors="coerce")
#     df["Fecha"] = pd.to_datetime(
#         df["Fecha"], errors="coerce", format="mixed", dayfirst=True
#     )
#
#     # 4. Reglas de negocio
#     df.loc[~df["Edad"].between(0, 120), "Edad"] = pd.NA
#     df.loc[df["Precio"] <= 0, "Precio"] = pd.NA
#
#     # 5. Imputacion minima
#     df["Edad"] = df["Edad"].fillna(df["Edad"].median())
#     df["Region"] = df["Region"].fillna("desconocida")

#     return df


# %% --- Correr el pipeline completo ----------------------------------------

#df_raw = pd.read_csv("../datos/ventas_corruptas.csv")
#
#df_clean = limpiar_datos(df_raw)
#
#df_clean.to_csv("../datos/ventas_limpias.csv", index=False)

# Ventaja: si mañana llegan 100,000 registros nuevos, no hay que
# limpiarlos a mano, solo correr limpiar_datos(df_nuevo).
