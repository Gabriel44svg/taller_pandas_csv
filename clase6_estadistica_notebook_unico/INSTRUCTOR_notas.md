# Notas para el instructor (no compartir con los equipos antes del reto)

## `experimento_marketing.csv` (script 07)

- Grupo A: n=215, media ≈ 822.3, mediana ≈ 822.8, std ≈ 118.6
- Grupo B: n=207, media ≈ 872.5, mediana ≈ 883.0, std ≈ 152.1
- Welch t-test: t ≈ -3.77, **p ≈ 0.0002** → se rechaza H0 con α = 0.05
- Diferencia de medias ≈ 50.2
- Cohen's d ≈ 0.37 (efecto pequeño-mediano)
- Conclusión esperada: sí hay evidencia estadística de una diferencia,
  y el tamaño del efecto es moderado — un buen resultado para discutir
  "significativo Y relevante", a diferencia del ejemplo de los "tres
  centavos" de la presentación.

## `campania_ab.csv` (script 09 — Statistical Detective Challenge)

Este es el dataset con trampas. La "solución" completa:

- Grupo A: n=950, media ≈ 409.9, mediana ≈ 339.1, std ≈ 293.0
- Grupo B: n=180, media ≈ 552.7, mediana ≈ 358.7, std ≈ 1062.5
  (¡la std de B es enorme comparada con A!)
- Welch t-test (con todos los datos): t ≈ -1.79, **p ≈ 0.075** → con
  α = 0.05 **no se rechaza H0** (no hay evidencia suficiente).
- Si se investigan los valores más altos de gasto (`sort_values`), se
  ve que un pequeño número de usuarios de B (~3% del grupo) tiene un
  gasto extremadamente alto ("ballenas") — eso es lo que dispara la
  media de B pero casi no mueve su mediana.
- Si se excluyen esas observaciones extremas de B (por ejemplo, todo
  lo que esté por arriba del percentil 97 del propio grupo B), la
  diferencia prácticamente desaparece: t ≈ 0.06, p ≈ 0.96, media de B
  sin outliers ≈ 408.6 (casi idéntica a la de A, 409.9).
- Las medianas de A y B (339 vs. 359) son mucho más parecidas entre sí
  que las medias — otra pista de que el "efecto" grande viene de los
  outliers y no de un cambio generalizado de comportamiento.
- Los tamaños de muestra también son muy distintos (950 vs. 180), lo
  cual conviene que los equipos noten y comenten como una limitación
  del diseño del experimento (no es un A/B test bien balanceado).

**Conclusión esperada del reto:** la afirmación de Marketing
("la campaña B es mejor") **no está bien respaldada** por los datos:
el test formal no alcanza significancia al 5%, y la diferencia de
medias que sí se observa está dominada por un puñado de outliers, no
por un cambio de comportamiento generalizado. Es un buen cierre para
reforzar las lecciones de "más datos no corrigen todo", "una muestra
enorme puede seguir representando mal" (aunque aquí es al revés: el
grupo pequeño es el que está distorsionado) y "significancia
estadística no implica relevancia práctica — y viceversa, la falta de
significancia con un dataset ruidoso no prueba que no haya efecto".

No hay una única "respuesta correcta" obligatoria — el objetivo es que
los equipos justifiquen su lectura con evidencia (media, mediana,
dispersión, outliers, tamaños de muestra, valor p).
