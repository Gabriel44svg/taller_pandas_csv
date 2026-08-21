# Clase 7 · Series Temporales I — Diplomado de Python y Análisis de Datos

Material de apoyo para la sesión (acompaña al PDF de la presentación).

## Estructura

```
clase7_series_temporales/
├── datos/
│   ├── generar_datos.py         # script que generó los dos CSV (ya ejecutado)
│   ├── ventas_historicas.csv    # dataset del Live Coding (731 filas, 2024-2025)
│   └── ventas_tienda.csv        # dataset de la práctica en equipos (359 filas, 2025)
├── notebooks/
│   ├── 01_live_coding_ventas_historicas.ipynb
│   └── 02_practica_ventas_tienda.ipynb
└── README.md
```

## Cómo usar los notebooks en clase

Todas las celdas de código están **comentadas** (cada línea empieza con `#`),
en el mismo orden en que aparecen en la presentación. La idea es que las
vayan descomentando en vivo conforme avanza cada sección:

1. Abran el notebook correspondiente.
2. Corran la celda de imports (esa sí está activa).
3. En cada bloque, seleccionen todas las líneas comentadas y quiten el `#`
   (en Jupyter/VS Code: `Ctrl + /` o `Cmd + /` con el bloque seleccionado).
4. Ejecuten la celda.

## Contenido de cada notebook

- **01_live_coding_ventas_historicas.ipynb**: cubre fechas con Pandas,
  índice temporal, resampling, descomposición, ventanas móviles, lag,
  autocorrelación, ACF/PACF, prueba ADF, los 10 pasos del "Live Coding"
  y el "Time Series Detective Challenge".
- **02_practica_ventas_tienda.ipynb**: las 3 partes de la práctica guiada
  en equipos (limpieza/índice temporal, resampling y ventanas móviles,
  preguntas de interpretación con celdas de apoyo), más una extensión
  opcional de autocorrelación/ADF por si algún equipo termina antes.

## Sobre los datos

Ambos CSV son sintéticos pero están construidos a propósito para que los
ejercicios "funcionen" pedagógicamente:

- Tendencia creciente en ambas series.
- Estacionalidad semanal (viernes/sábado más altos) — útil para `lag=7`,
  `autocorr` y ACF/PACF.
- Estacionalidad anual con pico en diciembre.
- Ruido aleatorio y algunos outliers/promociones.
- `ventas_historicas.csv` incluye NaN a propósito (para `df.isna().sum()`).
- `ventas_tienda.csv` tiene días faltantes a propósito (para practicar la
  detección de fechas faltantes en la Parte 1).

Si quieren regenerar los datos con otra semilla o rango de fechas, editen
`datos/generar_datos.py` (variable `SEED` y `fecha_inicio`/`fecha_fin`) y
vuelvan a correrlo desde la carpeta `datos/`:

```bash
cd datos
python generar_datos.py
```
