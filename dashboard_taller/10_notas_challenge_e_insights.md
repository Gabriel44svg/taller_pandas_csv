# Notas para el instructor — insights reales en `ventas.csv`

Estos son los números que en verdad salen del dataset (verificados
corriendo el código, no inventados). Úsalos para guiar la discusión y
para validar lo que los equipos encuentren en el Dashboard Challenge.

## Datos generales
- 1,015 transacciones, del 2026-01-01 al 2026-08-10.
- Ventas totales del periodo: **$7,574,923**.
- Columnas: `Fecha, Producto, Region, Vendedor, Cantidad, Precio, Ventas`.

## 1. Dos productos concentran el ingreso
Laptop + Monitor representan ~**78% de las ventas totales**.
Laptop sola concentra más de la mitad. Bueno para la discusión de
"dependencia excesiva de productos líderes" (igual que la conclusión
ejecutiva de la diapositiva final).

## 2. Julio tiene un salto real de ventas
Ventas por mes (aprox.):
- Junio: ~$962K
- Julio: ~$1,558K (**+62% vs junio**)
- Agosto (parcial, solo hasta el día 10): ~$235K

Nota: el salto real (~62%) es más grande que el "22%" que aparece como
ejemplo genérico en la diapositiva "Ejemplo: de gráfica a historia" —
son dos cosas distintas (la diapositiva usa un número ilustrativo). Si
quieres que el número hablado coincida exactamente con la diapositiva,
puedes decir "las ventas de julio crecieron con fuerza, muy por encima
del resto de meses" en vez del 22% literal, o ajustar el multiplicador
de campaña en `generar_datos.py` (busca `factor_campana`) y
regenerar el CSV.

El salto de julio está concentrado en Laptop/Monitor y en la región
Centro (así se diseñó en `generar_datos.py`), así que si un equipo
filtra por esas dos condiciones debería ver el efecto más claro
todavía.

## 3. Región Sur: caída sostenida en las últimas 4 semanas
Ventas semanales de la región Sur, últimas semanas del periodo:

| Semana (termina en) | Ventas Sur |
|---|---|
| 2026-07-12 | ~$167K |
| 2026-07-19 | ~$77K |
| 2026-07-26 | ~$76K |
| 2026-08-02 | ~$33K |
| 2026-08-09 | ~$11K |

Es una caída clara y sostenida, semana tras semana. En el TOTAL
acumulado del periodo, Sur no es la región más débil (arrancó fuerte),
así que este insight **solo aparece si se mira la evolución semanal
por región**, no con una barra de totales. Es el ejemplo perfecto para
la diapositiva "El error frecuente: crear primero las gráficas y
después intentar descubrir para qué sirven" — aquí es al revés: la
pregunta correcta (¿cómo evoluciona cada región?) lleva a la gráfica
correcta.

## 4. Conclusión ejecutiva sugerida (para modelar el "Pitch final")
Puedes usar esto como ejemplo de referencia, parecido al de la
diapositiva "Ejemplo de conclusión ejecutiva":

> "Las ventas crecieron con fuerza en julio, impulsadas principalmente
> por Laptop y Monitor en la región Centro; sin embargo, la región Sur
> muestra una caída sostenida durante las últimas cuatro semanas del
> periodo. Recomendamos investigar la caída de Sur antes de aumentar
> la inversión comercial, y evaluar la dependencia del negocio en solo
> dos productos."

## Checklist rápido para calificar el Dashboard Challenge
Con este dataset, un equipo que hizo bien el análisis debería mencionar
al menos DOS de estos tres hallazgos:
- [ ] Laptop (y/o Monitor) domina las ventas totales.
- [ ] Julio tuvo un salto de ventas fuera de lo normal.
- [ ] La región Sur cae de forma sostenida en las últimas semanas.

Si un equipo solo reporta totales generales sin haber mirado la
evolución en el tiempo, probablemente se perdió el insight de Sur —
buen momento para regresarlos a la diapositiva "Jerarquía visual"
(¿Cómo estamos? → ¿Qué está ocurriendo? → ¿Dónde ocurre?).
