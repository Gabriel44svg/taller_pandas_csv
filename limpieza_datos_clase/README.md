# Limpieza de Datos - Dataset Corrupto
Diplomado en Analisis de Datos - Universidad Marista

## Estructura de la carpeta

```
limpieza_datos_clase/
├── datos/
│   ├── ventas_corruptas.csv      <- dataset para el LIVE CODING (demo)
│   └── ventas_challenge.csv      <- dataset para el CHALLENGE por equipos (distinto al de la demo)
│
├── scripts_generacion/
│   └── generar_dataset_corrupto.py   <- ya fue ejecutado; corre esto solo si quieres
│                                         regenerar los CSV o crear una variante nueva
│                                         (cambia SEED para otra version)
│
├── clase_live_coding/
│   └── clase_limpieza_datos.py   <- TODO el codigo del PDF, comentado por secciones.
│                                     Ve descomentando en vivo durante la sesion.
│
└── challenge_equipos/
    ├── challenge_dataset_corrupto.py     <- se entrega a los equipos (sin pistas)
    └── solucion_challenge_INSTRUCTOR.py  <- SOLO para ti, no compartir antes de tiempo
```

## Orden de uso sugerido

1. Antes de clase: los CSV en `datos/` ya estan generados, no necesitas correr nada.
2. Durante la sesion: abre `clase_live_coding/clase_limpieza_datos.py` y ve
   descomentando bloque por bloque (las secciones siguen el mismo orden que el PDF).
3. Para el Challenge: reparte `challenge_equipos/challenge_dataset_corrupto.py`
   junto con `datos/ventas_challenge.csv` a los equipos.
4. Al cerrar el Challenge: usa `challenge_equipos/solucion_challenge_INSTRUCTOR.py`
   para validar rapido lo que entreguen.

## Nota tecnica importante (mencionar en clase)

`ventas_corruptas.csv` y `ventas_challenge.csv` mezclan formatos de fecha
(dd/mm/yyyy, yyyy-mm-dd, mm-dd-yyyy, y mes en texto en espanol). Con pandas 2.x,
`pd.to_datetime()` sin `format="mixed"` falla en convertir casi todas las fechas.
La correccion (`format="mixed", dayfirst=True`) ya esta documentada dentro de
`clase_limpieza_datos.py`, en la seccion de Fechas y en el Paso 4.
