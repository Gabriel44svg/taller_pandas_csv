"""
00_generar_datos.py
--------------------------------------------------------
Genera TODOS los CSV que usa la presentación "Integración
de Datos con Pandas" (Clase 5).

No se comenta: es el script que TÚ corres antes de la clase
para producir los archivos en /data. Los alumnos y tú
trabajarán sobre esos CSV, no sobre este script.

Ejecutar:
    python 00_generar_datos.py

Genera tres carpetas dentro de ../data:
    live_coding/      -> clientes.csv, ventas.csv, productos.csv
    practica_guiada/  -> alumnos.csv, inscripciones.csv, cursos.csv
    challenge/        -> clientes.csv, ventas.csv, productos.csv, sucursales.csv

Los datasets de "challenge" incluyen errores intencionales
(descritos en el slide "Errores ocultos") para que los
equipos los descubran auditando, tal como pide la clase.
--------------------------------------------------------
"""

import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(42)

BASE = Path(__file__).resolve().parent.parent / "data"
LIVE = BASE / "live_coding"
PRAC = BASE / "practica_guiada"
CHAL = BASE / "challenge"

for p in [LIVE, PRAC, CHAL]:
    p.mkdir(parents=True, exist_ok=True)

CIUDADES = ["CDMX", "Guadalajara", "Monterrey", "Puebla", "Mérida", "Querétaro"]
SEGMENTOS = ["Regular", "Premium", "Corporativo"]
CATEGORIAS = ["Electrónica", "Hogar", "Ropa", "Deportes", "Alimentos"]

# ============================================================
# 1) LIVE CODING  ->  clientes / ventas / productos
# ============================================================

n_clientes = 30
clientes_live = pd.DataFrame({
    "id_cliente": range(1, n_clientes + 1),
    "nombre": [f"Cliente_{i}" for i in range(1, n_clientes + 1)],
    "segmento": rng.choice(SEGMENTOS, n_clientes),
    "ciudad": rng.choice(CIUDADES, n_clientes),
})

n_productos = 15
productos_live = pd.DataFrame({
    "id_producto": range(101, 101 + n_productos),
    "producto": [f"Producto_{i}" for i in range(1, n_productos + 1)],
    "categoria": rng.choice(CATEGORIAS, n_productos),
    "precio": rng.integers(50, 20000, n_productos),
})

n_ventas = 300
ventas_live = pd.DataFrame({
    "id_venta": range(1001, 1001 + n_ventas),
    "id_cliente": rng.choice(clientes_live["id_cliente"], n_ventas),
    "id_producto": rng.choice(productos_live["id_producto"], n_ventas),
    "fecha": pd.to_datetime("2025-01-01") + pd.to_timedelta(
        rng.integers(0, 180, n_ventas), unit="D"
    ),
    "cantidad": rng.integers(1, 6, n_ventas),
})

# Sembramos a propósito 8 ventas con id_cliente que NO existe en clientes
# -> sirven para el paso de indicator=True y ver "left_only"
ids_fantasma_cliente = rng.choice(range(9000, 9010), 8, replace=False)
idx_fantasma = rng.choice(ventas_live.index, 8, replace=False)
ventas_live.loc[idx_fantasma, "id_cliente"] = ids_fantasma_cliente

# Sembramos 5 ventas con id_producto que NO existe en productos
# -> sirven para "Validación 3: nulos" al hacer merge con productos
ids_fantasma_prod = rng.choice(range(500, 510), 5, replace=False)
idx_fantasma_prod = rng.choice(
    ventas_live.index.difference(idx_fantasma), 5, replace=False
)
ventas_live.loc[idx_fantasma_prod, "id_producto"] = ids_fantasma_prod

clientes_live.to_csv(LIVE / "clientes.csv", index=False)
ventas_live.to_csv(LIVE / "ventas.csv", index=False)
productos_live.to_csv(LIVE / "productos.csv", index=False)

# ============================================================
# 2) PRÁCTICA GUIADA  ->  alumnos / inscripciones / cursos
# ============================================================

CARRERAS = ["Ing. Sistemas", "Actuaría", "Administración", "Psicología", "Diseño"]

n_alumnos = 25
alumnos = pd.DataFrame({
    "id_alumno": range(1, n_alumnos + 1),
    "nombre": [f"Alumno_{i}" for i in range(1, n_alumnos + 1)],
    "carrera": rng.choice(CARRERAS, n_alumnos),
})

n_cursos = 8
cursos = pd.DataFrame({
    "id_curso": range(201, 201 + n_cursos),
    "curso": [
        "Estadística I", "Programación I", "Bases de Datos", "Cálculo II",
        "Machine Learning", "Ética Profesional", "Álgebra Lineal", "Redes",
    ],
    "profesor": [f"Prof_{i}" for i in range(1, n_cursos + 1)],
})

n_inscripciones = 90
inscripciones = pd.DataFrame({
    "id_alumno": rng.choice(alumnos["id_alumno"], n_inscripciones),
    # dejamos fuera a propósito el último curso (sin inscripciones)
    "id_curso": rng.choice(cursos["id_curso"][:-1], n_inscripciones),
    "calificacion": rng.integers(60, 100, n_inscripciones),
})

# 4 inscripciones de alumnos que NO existen en alumnos.csv
# -> pregunta "¿Hay inscripciones sin alumno asociado?"
ids_fantasma_alumno = rng.choice(range(900, 910), 4, replace=False)
idx_fant = rng.choice(inscripciones.index, 4, replace=False)
inscripciones.loc[idx_fant, "id_alumno"] = ids_fantasma_alumno

alumnos.to_csv(PRAC / "alumnos.csv", index=False)
inscripciones.to_csv(PRAC / "inscripciones.csv", index=False)
cursos.to_csv(PRAC / "cursos.csv", index=False)

# ============================================================
# 3) DATA INTEGRATION CHALLENGE
#    clientes / ventas / productos / sucursales (con errores)
# ============================================================

REGIONES = ["Norte", "Sur", "Centro", "Bajío", "Sureste"]

n_cli_chal = 60
clientes_chal = pd.DataFrame({
    "id_cliente": range(1, n_cli_chal + 1),
    "nombre": [f"Cliente_{i}" for i in range(1, n_cli_chal + 1)],
    "segmento": rng.choice(SEGMENTOS, n_cli_chal),
    "ciudad": rng.choice(CIUDADES, n_cli_chal),
})
# Error 1: clientes duplicados (misma fila repetida -> rompe unicidad de PK)
duplicados = clientes_chal.sample(4, random_state=1)
clientes_chal = pd.concat([clientes_chal, duplicados], ignore_index=True)

n_prod_chal = 20
productos_chal = pd.DataFrame({
    "id_producto": range(101, 101 + n_prod_chal),
    "producto": [f"Producto_{i}" for i in range(1, n_prod_chal + 1)],
    "categoria": rng.choice(CATEGORIAS, n_prod_chal),
    "precio": rng.integers(50, 25000, n_prod_chal),
})

n_suc_chal = 10
sucursales_chal = pd.DataFrame({
    "id_sucursal": range(1, n_suc_chal + 1),
    "sucursal": [f"Sucursal_{i}" for i in range(1, n_suc_chal + 1)],
    "region": rng.choice(REGIONES, n_suc_chal),
})

n_ventas_chal = 500
ventas_chal = pd.DataFrame({
    "id_venta": range(5001, 5001 + n_ventas_chal),
    # dejamos fuera a propósito 8 clientes (nunca compraron)
    "id_cliente": rng.choice(clientes_chal["id_cliente"].unique()[:-8], n_ventas_chal),
    "id_producto": rng.choice(productos_chal["id_producto"], n_ventas_chal),
    # dejamos fuera a propósito 2 sucursales (nunca vendieron)
    "id_sucursal": rng.choice(sucursales_chal["id_sucursal"][:-2], n_ventas_chal),
    "fecha": pd.to_datetime("2025-01-01") + pd.to_timedelta(
        rng.integers(0, 300, n_ventas_chal), unit="D"
    ),
    "cantidad": rng.integers(1, 8, n_ventas_chal),
})

# Error 2: ventas con clientes inexistentes
ids_fant_cli = rng.choice(range(9000, 9020), 12, replace=False)
idx1 = rng.choice(ventas_chal.index, 12, replace=False)
ventas_chal.loc[idx1, "id_cliente"] = ids_fant_cli

# Error 3: ventas con productos inexistentes
ids_fant_prod = rng.choice(range(700, 720), 9, replace=False)
idx2 = rng.choice(ventas_chal.index.difference(idx1), 9, replace=False)
ventas_chal.loc[idx2, "id_producto"] = ids_fant_prod

clientes_chal.to_csv(CHAL / "clientes.csv", index=False)
ventas_chal.to_csv(CHAL / "ventas.csv", index=False)
productos_chal.to_csv(CHAL / "productos.csv", index=False)
sucursales_chal.to_csv(CHAL / "sucursales.csv", index=False)

print("Datos generados correctamente en:", BASE)
for f in sorted(BASE.rglob("*.csv")):
    print(" -", f.relative_to(BASE))
