# Clase 6 — Estadística para Data Science
Diplomado de Python y Análisis de Datos — Universidad Marista

Esta carpeta acompaña la presentación (PDF) que ya tienes. Contiene los
**datos** y **todos los scripts de los ejercicios**, con el código
comentado (`#`) para que lo vayas descomentando en vivo durante la
clase.

## Estructura

```
clase6_estadistica/
├── README.md                 <- este archivo
├── INSTRUCTOR_notas.md       <- guía de respuestas (solo para ti)
├── data/
│   ├── datos_generales.csv
│   ├── experimento_marketing.csv
│   └── campania_ab.csv
└── scripts/
    ├── 00_setup.py
    ├── 01_tendencia_central.py
    ├── 02_dispersion.py
    ├── 03_percentiles_distribuciones.py
    ├── 04_zscore.py
    ├── 05_muestreo_clt.py
    ├── 06_intervalo_confianza.py
    ├── 07_experimento_ab_welch.py
    ├── 08_correlacion.py
    └── 09_statistical_detective_challenge.py
```

## Cómo usarlo en clase

1. Abre una terminal / Jupyter / VS Code dentro de `clase6_estadistica/`.
2. Instala dependencias si hace falta:
   ```
   pip install pandas numpy matplotlib seaborn scipy
   ```
3. Ve abriendo los scripts **en el orden numerado** conforme avanza la
   presentación (los números corresponden más o menos a las secciones
   del PDF). Cada script asume que ya corriste `00_setup.py` en la
   misma sesión (o notebook) para tener `df`, `pd`, `np`, `plt`, `sns`
   y `stats` disponibles — excepto `07` y `09`, que cargan su propio
   dataset y sus propios imports porque usan otro CSV.
4. Todo el código está comentado con `#`. Ve descomentando bloque por
   bloque (cada bloque está separado con una línea `# ---`) según lo
   que quieras mostrar en vivo.

## Datasets

### `datos_generales.csv` (2000 filas)
Dataset genérico usado en los ejemplos de tendencia central,
dispersión, percentiles, distribuciones, z-score, muestreo, CLT,
intervalos de confianza y correlación.

| Columna      | Descripción                                                             |
|--------------|--------------------------------------------------------------------------|
| id_cliente   | identificador                                                            |
| ingreso      | ingreso del cliente; **sesgo positivo a propósito** (para el ejemplo de media vs. mediana) |
| categoria    | Basico / Estandar / Premium / Empresarial (Basico es la moda, ~45%)     |
| publicidad   | inversión en publicidad (miles)                                         |
| ventas       | ventas; correlacionada con `publicidad` (r ≈ 0.8); tiene algunos NaN    |

### `experimento_marketing.csv` (422 filas)
Usado en el Live Coding (Welch t-test, pasos 1–7): Grupo A (experiencia
actual) vs. Grupo B (nueva experiencia). Diseñado para que **sí exista**
una diferencia real y significativa (gasto medio ≈ 822 vs. ≈ 873,
Welch p ≈ 0.0002), con varianzas distintas — de ahí que Welch (y no un
t-test clásico) sea la elección correcta.

| Columna     | Descripción              |
|-------------|---------------------------|
| id_usuario  | identificador             |
| grupo       | "A" o "B"                 |
| gasto       | gasto del usuario (tiene algunos NaN) |

### `campania_ab.csv` (1130 filas)
El dataset del **Statistical Detective Challenge**. Contiene trampas a
propósito: tamaños de grupo muy distintos (A=950, B=180) y un pequeño
grupo de "ballenas" (outliers de gasto muy alto) solo en el Grupo B,
que inflan su media sin mover tanto su mediana. Ver
`INSTRUCTOR_notas.md` para la lectura completa de resultados.

| Columna      | Descripción                                  |
|--------------|-----------------------------------------------|
| id_usuario   | identificador                                  |
| grupo        | "A" o "B"                                     |
| edad         | edad del usuario (algunos NaN)                |
| region       | Centro / Norte / Sur / Occidente / Sureste    |
| conversion   | 0/1                                            |
| gasto        | gasto del usuario                              |
| tiempo_sitio | tiempo en el sitio, segundos (algunos NaN)    |

Todos los datos son **sintéticos**, generados con `numpy`/`pandas` para
esta clase (no corresponden a una empresa real).
