# Paquete de datos y scripts — Visualización de Datos y Dashboard Analítico

Este paquete acompaña la presentación. Contiene el
dataset `ventas.csv` y un script por cada ejercicio de la sesión, **con
todo el código comentado**. La idea es que en clase vayas descomentando
línea por línea (o bloque por bloque) conforme avanzas por las
diapositivas, en vez de tener que escribir el código en vivo desde cero.

## Contenido

```
dashboard_taller/
├── 00_LEEME.md
├── data/
│   └── ventas.csv                     ← dataset (1,015 transacciones, ene–ago 2026)
├── generar_datos.py                   ← cómo se generó ventas.csv (no mostrar en clase)
├── 01_exploracion.py                  ← Paso 1 (slide "Paso 1: cargar y explorar")
├── 02_preparacion.py                  ← Paso 2 (slide "Paso 2: preparar los datos")
├── 03_kpis.py                         ← Paso 3 (slide "Paso 3: calcular KPIs")
├── 04_barras_producto.py              ← slide "Barras con Python" + Paso 4
├── 05_histograma.py                   ← slide "Histograma en Python"
├── 06_tendencia_temporal.py           ← Paso 5 (slide "tendencia temporal")
├── 07_ventas_region.py                ← Paso 6 (slide "ventas por región")
├── 08_dashboard_streamlit.py          ← slide "Dashboard rápido con Streamlit"
├── 09_dashboard_streamlit_filtros.py  ← slide "Agregar filtros" (versión final, con selectbox)
└── 10_notas_challenge_e_insights.md   ← notas para ti: insights reales que SÍ están en los datos
```

## Cómo usarlo 
Cada script `.py` de los ejercicios sigue el mismo patrón:

1. Un bloque de encabezado explica el objetivo y en qué diapositiva va.
2. Todo el código real está comentado con `#`.
3. Hay marcadores `# >>> DESCOMENTAR PASO A` (y B, C…) para que reveles
   el código en el orden en que lo vas explicando, en vez de todo de
   golpe.
4. Al final de cada bloque hay una pregunta de negocio (igual que en la
   diapositiva) para lanzarla al grupo antes de correr el código.

Solo necesitas: `pip install pandas matplotlib streamlit`.

Para los scripts de matplotlib: `python 04_barras_producto.py`.
Para los de Streamlit: `streamlit run 08_dashboard_streamlit.py`.

## Por qué los datos están "amarrados" a las conclusiones de las diapositivas

El dataset no es aleatorio puro: se calibró para que las conclusiones
que aparecen en las diapositivas (ej. "las ventas crecieron ~22% en
julio impulsadas por Laptop/Monitor en la región Centro", "la región
Sur cae sostenidamente en las últimas 4 semanas", "dos productos
concentran la mayoría del ingreso") **se puedan reproducir de verdad**
corriendo el código sobre `ventas.csv`. Ve `10_notas_challenge_e_insights.md`
para los números exactos que deberían salirte.
