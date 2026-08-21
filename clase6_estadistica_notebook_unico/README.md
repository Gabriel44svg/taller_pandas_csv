# Clase 6 — Estadística para Data Science (un solo notebook)
Diplomado de Python y Análisis de Datos — Universidad Marista

Versión de **un único notebook** (`Clase6_Estadistica.ipynb`) con todos
los bloques de la clase (00 a 09) en orden, para que `df` y las demás
variables se mantengan disponibles de principio a fin sin tener que
saltar entre archivos ni volver a cargar nada a mano.

## Estructura

```
clase6_estadistica_notebook_unico/
├── README.md
├── INSTRUCTOR_notas.md         <- guía de respuestas (solo para ti)
├── Clase6_Estadistica.ipynb    <- el notebook de la clase completa
└── data/
    ├── datos_generales.csv
    ├── experimento_marketing.csv
    └── campania_ab.csv
```

## Cómo usarlo en clase

1. Instala dependencias si hace falta:
   ```
   pip install pandas numpy matplotlib seaborn scipy jupyterlab
   ```
2. Abre `Clase6_Estadistica.ipynb` **desde esta carpeta** (el notebook
   está en el mismo nivel que `data/`, así que las rutas
   `"data/archivo.csv"` funcionan tal cual, sin `../`).
3. Corre las celdas **en orden, de arriba hacia abajo**. La primera
   celda de código (bloque 00 — Setup) deja listos `pd`, `np`, `plt`,
   `sns`, `stats` y `df` (cargado desde `datos_generales.csv`).
4. Cada celda de código está comentada con `#`. Ve descomentando
   bloque por bloque conforme avanzas en la presentación.

### Por qué un solo notebook resuelve el `NameError: name 'df' is not defined`

Cada notebook de Jupyter tiene su propio kernel (su propia "memoria").
Si abrías un notebook distinto por cada bloque, `df` se perdía al
cambiar de archivo porque cada uno arrancaba con un kernel nuevo. Al
tener todo en un solo notebook y correr las celdas en orden, `df`
(y `grupo_a`, `t_stat`, etc.) se mantienen disponibles para las celdas
siguientes durante toda la clase.

### Sobre los datasets del experimento A/B y el reto final

Los bloques **07** (Experimento A/B, Welch t-test) y **09** (Statistical
Detective Challenge) cargan **su propio dataset** en variables
separadas — `df_exp` y `df_camp` respectivamente — en lugar de
reutilizar `df`. Esto es a propósito: así el `df` general (de
`datos_generales.csv`) sigue disponible después, por ejemplo para el
bloque **08** (Correlación), que va justo después del bloque 07 en la
presentación.

## Datasets

Los mismos tres CSV de las versiones anteriores — el detalle de cada
columna, y el diseño de las "trampas" del reto final, está en
`INSTRUCTOR_notas.md`.

- `datos_generales.csv` → variable `df` (bloques 01–06, 08)
- `experimento_marketing.csv` → variable `df_exp` (bloque 07)
- `campania_ab.csv` → variable `df_camp` (bloque 09)

Todos los datos son **sintéticos**, generados para esta clase.
