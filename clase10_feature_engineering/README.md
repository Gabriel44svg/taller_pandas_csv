# Clase 10 — Feature Engineering
Diplomado de Python y Análisis de Datos · Universidad Marista

Material de apoyo para la presentación (`clase10_feature_engineering.pdf`).
Todo el código de los notebooks está **comentado a propósito**: la idea es
que vayas quitando el `#` de cada línea, celda por celda, conforme avanzas
en la presentación durante la sesión en vivo.

## Estructura

```
clase10_feature_engineering/
├── data/
│   ├── viviendas_features.csv   (600 filas)
│   └── clientes_features.csv    (700 filas)
└── notebooks/
    ├── 01_viviendas_live_coding.ipynb
    └── 02_clientes_challenge.ipynb
```

Los notebooks referencian los CSV con ruta relativa `../data/...`, así que
consérvalos dentro de esta misma estructura de carpetas (o ajusta la ruta
si los mueves).

## `01_viviendas_live_coding.ipynb`

Cubre, en orden:
- Demo de escalas distintas, `StandardScaler`, `MinMaxScaler`
- Por qué NO codificar `zona` como 1,2,3 (mala idea)
- One-Hot Encoding (Pandas y Scikit-learn, con `handle_unknown="ignore"`)
- Ordinal Encoding (ejemplo conceptual con datos de juguete)
- Binning de `antiguedad`
- Transformación logarítmica de `precio`
- `PolynomialFeatures` con `metros` y `antiguedad`
- **Live Coding oficial (Pasos 1–11 de la presentación):** limpieza de
  fecha, variables temporales, ratios, validación, split, `ColumnTransformer`,
  `Pipeline`, predicción y evaluación
- Comparación **Modelo A (básico) vs Modelo B (con Feature Engineering)**
- `Feature Importance` con `RandomForestRegressor`
- Preguntas de salida

El dataset está diseñado para que el Modelo B mejore de forma muy notoria
sobre el Modelo A (la variable `zona` y `tipo_vivienda` tienen un efecto
fuerte en `precio` que el Modelo A no puede capturar). Hay 2 filas con
`habitaciones = 0` a propósito, para la discusión de división entre cero.

## `02_clientes_challenge.ipynb`

Es el **Feature Engineering Challenge**: todos usan `LinearRegression` y
solo pueden modificar `X`. Sigue las Fases 1–5 de la presentación:

1. Modelo base (`edad`, `ingreso`, `visitas`, `compras`, `gasto_total`)
2. Crear 4 tipos de feature: ratio, temporal, transformación, categórica
3. Pipeline con `StandardScaler` + `OneHotEncoder` + `LinearRegression`
4. Comparar `MAE_base` vs `MAE_features`
5. Discusión en equipo (preguntas abiertas, sin código) + una función
   opcional (`evaluar_con_extra`) para medir la contribución individual
   de cada feature nueva, útil si algún equipo quiere profundizar

Hay 5 filas con `compras = 0` a propósito, para forzar la discusión de
división entre cero al construir `gasto_por_compra`. La mejora de
Fase 2 sobre Fase 1 es moderada (no exagerada), lo cual da pie a la
discusión real de "qué feature ayudó más / cuál no ayudó".

## Nota sobre los datos

Ambos CSV son **sintéticos**, generados con relaciones controladas para
que los resultados numéricos respalden el discurso de la presentación.
No son datos reales de ninguna inmobiliaria ni empresa.
