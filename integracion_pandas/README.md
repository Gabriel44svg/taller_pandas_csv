# Integración de Datos con Pandas — Clase 5

Material de apoyo para la presentación (la tienes en PDF aparte).
Incluye los datasets ya generados y los scripts comentados de
cada sección para que los vayas descomentando en vivo.

## Estructura

```
integracion_pandas/
├── data/
│   ├── live_coding/         clientes.csv, ventas.csv, productos.csv
│   ├── practica_guiada/     alumnos.csv, inscripciones.csv, cursos.csv
│   └── challenge/           clientes.csv, ventas.csv, productos.csv, sucursales.csv
└── scripts/
    ├── 00_generar_datos.py     genera todo lo de /data (ya ejecutado)
    ├── 01_live_coding.py       sección "Live Coding" — comentado
    ├── 02_practica_guiada.py   sección "Práctica guiada" — clave de respuestas, comentado
    └── 03_challenge.py         "Data Integration Challenge" — clave de respuestas, comentado
```

## Cómo usar los scripts en clase

Los tres scripts de `scripts/01…03` están **100% comentados**
(cada línea empieza con `#`). Cada bloque corresponde a un
slide específico — el título del bloque coincide con el título
del slide. Ve descomentando bloque por bloque conforme avanzas
en la presentación y ejecuta con los alumnos.

- `01_live_coding.py` → sigue exactamente los "Pasos 1–7" y las
  "Preguntas 1–3" del Live Coding.
- `02_practica_guiada.py` → **no se les entrega a los alumnos**,
  es tu clave de respuestas. A ellos solo dales los 3 CSV de
  `data/practica_guiada/` y el enunciado del slide "Preguntas de
  práctica" (deben elegir el JOIN sin ayuda).
- `03_challenge.py` → tampoco se entrega a los equipos. Ellos
  reciben los 4 CSV de `data/challenge/`. Úsalo para armar la
  clave, dar pistas, o resolverlo en vivo al cierre.

## Errores sembrados a propósito en los datos

Para que las auditorías (`indicator=True`, `validate=...`,
`isna().sum()`) tengan algo real que encontrar:

**`live_coding/`**
- 8 ventas con `id_cliente` inexistente → aparecen como
  `left_only` al usar `indicator=True` en el Paso 5.
- 5 ventas con `id_producto` inexistente → generan `NaN` en
  `precio`/`categoria` tras el merge con productos (gancho para
  Validación 3: nulos).

**`practica_guiada/`**
- 4 inscripciones con `id_alumno` inexistente (Pregunta 4).
- El último curso del catálogo no tiene ninguna inscripción
  (Pregunta 5).

**`challenge/`**
- 4 filas de clientes duplicadas exactamente (rompen la
  unicidad de `id_cliente`).
- 12 ventas con `id_cliente` inexistente.
- 9 ventas con `id_producto` inexistente.
- 2 sucursales que nunca aparecen en ventas.
- 8 clientes que nunca compraron.

Estos números pueden confirmarse corriendo `00_generar_datos.py`
de nuevo (usa semilla fija `42`, así que los mismos "errores"
siempre caen en los mismos lugares si necesitas reproducibilidad
entre grupos o semestres). Si quieres datos distintos cada vez,
cambia la línea `rng = np.random.default_rng(42)`.

## Regenerar los datos

```bash
cd scripts
python3 00_generar_datos.py
```

Esto sobrescribe todo lo que haya en `data/`.
