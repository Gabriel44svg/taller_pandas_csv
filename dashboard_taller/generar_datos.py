"""
generar_datos.py
-----------------
Genera el archivo ventas.csv que se usa en TODOS los ejercicios de la
sesión (Live Coding, Dashboard Challenge, Streamlit).

No es necesario mostrar este script en clase: es solo la "fábrica" de
datos. Lo que los alumnos deben ver y trabajar es ventas.csv.

Diseño intencional de los datos (para que las conclusiones de las
diapositivas SÍ se puedan reproducir con el CSV real):

  1. Tendencia general de crecimiento mes a mes (~3% mensual).
  2. Salto de ventas en julio 2026 (~ +22%) impulsado por una campaña,
     concentrado sobre todo en Laptop y Monitor, región Centro.
  3. Caída sostenida de la región Sur en las últimas 4 semanas del
     periodo (para el ejercicio de "insight" y la conclusión ejecutiva).
  4. Dos productos (Laptop y Monitor) concentran la mayoría del ingreso,
     para poder discutir "dependencia excesiva de productos líderes".

Rango de fechas: 2026-01-01 a 2026-08-10.
"""

import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)

# ---------------------------------------------------------------
# Catálogo de productos, regiones y vendedores
# ---------------------------------------------------------------
PRODUCTOS = {
    "Laptop":     15000,
    "Monitor":     4200,
    "Teclado":      850,
    "Mouse":        450,
    "Audifonos":    600,
    "Impresora":   3200,
}

# Peso relativo de cada producto en el volumen de transacciones
# (Laptop y Monitor concentran más ingreso aunque no sean los de
# mayor volumen -> "dos productos líderes")
PESOS_PRODUCTO = {
    "Laptop":     0.16,
    "Monitor":    0.17,
    "Teclado":    0.22,
    "Mouse":      0.24,
    "Audifonos":  0.14,
    "Impresora":  0.07,
}

REGIONES = ["Norte", "Centro", "Sur", "Este"]
PESOS_REGION_BASE = {"Norte": 0.27, "Centro": 0.33, "Sur": 0.22, "Este": 0.18}

VENDEDORES_POR_REGION = {
    "Norte":  ["Maria", "Jorge"],
    "Centro": ["Ana", "Sofia"],
    "Sur":    ["Carlos", "Paula"],
    "Este":   ["Luis", "Diego"],
}

FECHA_INICIO = pd.Timestamp("2026-01-01")
FECHA_FIN = pd.Timestamp("2026-08-10")
ULTIMAS_4_SEMANAS_INICIO = FECHA_FIN - pd.Timedelta(weeks=4)
CAMPANA_INICIO = pd.Timestamp("2026-07-01")
CAMPANA_FIN = pd.Timestamp("2026-07-21")


def factor_mes(fecha: pd.Timestamp) -> float:
    """Tendencia de crecimiento general ~3% mensual desde enero."""
    meses_transcurridos = (fecha.year - 2026) * 12 + (fecha.month - 1)
    return 1 + 0.03 * meses_transcurridos


def factor_region(region: str, fecha: pd.Timestamp) -> float:
    """Aplica la caída sostenida de la región Sur en las últimas 4 semanas."""
    if region == "Sur" and fecha >= ULTIMAS_4_SEMANAS_INICIO:
        # Caída progresiva: entre -10% y -45% según qué tan cerca del final
        semanas_dentro = (fecha - ULTIMAS_4_SEMANAS_INICIO).days / 7
        return max(0.55, 1 - 0.10 * semanas_dentro)
    return 1.0


def factor_campana(producto: str, region: str, fecha: pd.Timestamp) -> float:
    """Boost de campaña en julio, concentrado en Laptop/Monitor y Centro."""
    if CAMPANA_INICIO <= fecha <= CAMPANA_FIN:
        boost = 1.0
        if producto in ("Laptop", "Monitor"):
            boost *= 1.55
        if region == "Centro":
            boost *= 1.35
        return boost
    return 1.0


filas = []

fecha_actual = FECHA_INICIO
while fecha_actual <= FECHA_FIN:
    # Menos transacciones fin de semana, más entre semana
    es_finde = fecha_actual.dayofweek >= 5
    n_transacciones_base = RNG.integers(4, 8) if not es_finde else RNG.integers(1, 4)

    for _ in range(n_transacciones_base):
        producto = RNG.choice(list(PESOS_PRODUCTO.keys()), p=list(PESOS_PRODUCTO.values()))

        # Ajusta pesos de región dinámicamente por la caída del Sur
        pesos_region = np.array([
            PESOS_REGION_BASE[r] * factor_region(r, fecha_actual) for r in REGIONES
        ])
        pesos_region = pesos_region / pesos_region.sum()
        region = RNG.choice(REGIONES, p=pesos_region)

        vendedor = RNG.choice(VENDEDORES_POR_REGION[region])

        cantidad = int(RNG.integers(1, 6))
        if producto in ("Laptop", "Monitor"):
            cantidad = int(RNG.integers(1, 3))

        precio_base = PRODUCTOS[producto]
        ruido_precio = RNG.normal(1.0, 0.03)
        precio = round(precio_base * ruido_precio, 2)

        mult = (
            factor_mes(fecha_actual)
            * factor_region(region, fecha_actual)
            * factor_campana(producto, region, fecha_actual)
        )
        # El multiplicador afecta la probabilidad de "venta extra" en vez de
        # inflar artificialmente cantidades no enteras
        if RNG.random() < (mult - 1.0) and mult > 1.0:
            cantidad += 1
        elif mult < 1.0 and RNG.random() < (1.0 - mult):
            cantidad = max(1, cantidad - 1)

        ventas = round(cantidad * precio, 2)

        filas.append({
            "Fecha": fecha_actual.strftime("%Y-%m-%d"),
            "Producto": producto,
            "Region": region,
            "Vendedor": vendedor,
            "Cantidad": cantidad,
            "Precio": precio,
            "Ventas": ventas,
        })

    fecha_actual += pd.Timedelta(days=1)

df = pd.DataFrame(filas)
df = df.sort_values("Fecha").reset_index(drop=True)

df.to_csv("data/ventas.csv", index=False, encoding="utf-8")

print(f"Filas generadas: {len(df)}")
print(f"Rango de fechas: {df['Fecha'].min()} a {df['Fecha'].max()}")
print(f"Ventas totales: {df['Ventas'].sum():,.2f}")
print("\nVentas por producto:")
print(df.groupby("Producto")["Ventas"].sum().sort_values(ascending=False))
print("\nVentas por region:")
print(df.groupby("Region")["Ventas"].sum().sort_values(ascending=False))
