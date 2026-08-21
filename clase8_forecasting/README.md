# Clase 8 — Series Temporales II: Forecasting

Material de apoyo para la clase (Diplomado de Python y Análisis de Datos,
Universidad Marista). La presentación ya la tienes en PDF; esta carpeta
trae los **datos** y los **notebooks** con el código de todos los
ejercicios.

## Estructura

```
clase8_forecasting/
├── data/
│   ├── ventas_mensuales.csv   # 60 meses -> usado en el Live Coding (torneo)
│   └── ventas_forecast.csv    # 48 meses -> usado en el Forecasting Challenge
└── notebooks/
    ├── 01_live_coding_ventas_mensuales.ipynb
    └── 02_challenge_ventas_forecast.ipynb
```

## Datos

Ambos CSV son **sintéticos** (generados con tendencia + estacionalidad +
ruido para que se comporten de forma realista) y tienen las columnas:

- `fecha` — mensual, formato `YYYY-MM-DD`
- `ventas` — variable objetivo
- `promociones` — indicador binario (0/1)
- `unidades` — unidades vendidas

`ventas_mensuales.csv` tiene estacionalidad aditiva y una tendencia suave
(bueno para comparar SES / Holt / Holt-Winters aditivo). `ventas_forecast.csv`
tiene una temporada alta marcada en Nov–Dic (estacionalidad más
multiplicativa), pensada para el reto final.

## Notebooks

Ambos notebooks siguen el mismo criterio: **el código de cada paso está
comentado línea por línea**. La idea es que tú (instructor) vayas
descomentando cada bloque en vivo, en el orden en que aparece en la
presentación, en lugar de mostrar el código ya resuelto.

- **`01_live_coding_ventas_mensuales.ipynb`**
  Sigue exactamente los "Pasos 1–9" del bloque de Live Coding de la
  presentación: cargar, visualizar, Train/Test, Naive, Seasonal Naive,
  media móvil, SES, Holt, Holt-Winters, ARIMA, tabla comparativa
  (MAE/RMSE/MAPE), gráfica real vs pronóstico y análisis de residuos.

- **`02_challenge_ventas_forecast.ipynb`**
  Estructura para el "Forecasting Challenge": EDA, Train/Test (12 meses
  de test), los 4 modelos obligatorios (Naive, Seasonal Naive, Holt,
  Holt-Winters) + ARIMA como bonus, tabla de métricas, gráfica de
  pronósticos, residuos y preguntas de cierre para que cada equipo
  responda directamente en el notebook.

## Requisitos

```
pandas
numpy
matplotlib
scikit-learn
statsmodels
```

Instalación rápida:

```bash
pip install pandas numpy matplotlib scikit-learn statsmodels
```
