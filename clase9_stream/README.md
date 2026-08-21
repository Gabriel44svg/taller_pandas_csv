# Clase 9 — Introducción a Machine Learning

Material de apoyo para la sesión en vivo (la presentación ya la tienes en PDF).

## Estructura

```
clase9_ml/
├── data/
│   ├── viviendas.csv          # dataset del Live Coding (1000 filas)
│   └── viviendas_reto.csv     # dataset del ML Challenge (800 filas)
└── notebooks/
    ├── 01_primer_modelo_viviendas.ipynb        # Live Coding, Pasos 1–9 + evaluación + baseline
    └── 02_challenge_viviendas_reto.ipynb       # Machine Learning Challenge (misión de 10 puntos + preguntas)
```

## Datasets

**`viviendas.csv`** — columnas `metros`, `habitaciones`, `banios`, `antiguedad`, `precio`.
Coincide exactamente con las columnas usadas en el Live Coding de la presentación.
Incluye algunos `NaN` en `antiguedad` para que `df.isna().sum()` tenga algo que mostrar.

**`viviendas_reto.csv`** — columnas `metros`, `habitaciones`, `banios`, `antiguedad`,
`distancia_centro`, `precio`. Usado en el Machine Learning Challenge. Incluye `NaN`
en `banios` y 4 outliers de precio a propósito, para que la Pregunta 4 (dónde se
equivoca más el modelo) tenga sentido al revisarla en equipo.

Ambos se generaron sintéticamente con una relación lineal + ruido gaussiano
(ver `generar_datos.py`), así que un modelo de `LinearRegression` obtiene un
desempeño razonable pero no perfecto — bueno para ilustrar MAE/RMSE/R² y
comparación contra baseline.

## Notebooks

Cada celda de código está **comentada línea por línea**. La idea es que las
vayas descomentando en vivo, en el orden en que aparecen (que sigue el mismo
orden que la presentación en PDF), en lugar de tenerlas ya ejecutadas.

- `01_primer_modelo_viviendas.ipynb`: sigue Paso 1 a Paso 9 de la presentación
  (cargar → explorar → X → y → split → modelo → fit → predict → comparar),
  más MAE/RMSE/R², visualización, Train vs Test, baseline y predicción de una
  vivienda nueva.
- `02_challenge_viviendas_reto.ipynb`: sigue la misión de 10 puntos del reto,
  con celdas markdown para las Preguntas 1–4 del ejercicio en equipo.

## Regenerar los datos

Si quieres otra semilla o cambiar tamaños/distribuciones, corre:

```bash
python generar_datos.py
```

(usa `numpy` y `pandas`; `random_state`/`seed=42` para reproducibilidad, igual
que en la presentación).
