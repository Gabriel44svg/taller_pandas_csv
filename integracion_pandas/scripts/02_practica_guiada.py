# ============================================================
# 02_practica_guiada.py
# Sección: "Práctica guiada" de la presentación
# Caso académico: alumnos + inscripciones + cursos
#
# INSTRUCCIONES PARA EL INSTRUCTOR:
# El slide dice explícitamente: "No se les dará el tipo de
# JOIN. Deben elegirlo según la pregunta." Por eso este script
# trae, comentado, un posible camino de solución para cada una
# de las 5 preguntas de práctica. Úsalo como respuesta modelo
# o para ir revelando pistas si el grupo se atora.
#
# Datos en:
#   ../data/practica_guiada/alumnos.csv
#   ../data/practica_guiada/inscripciones.csv
#   ../data/practica_guiada/cursos.csv
# ============================================================


# ------------------------------------------------------------
# PASO 0: Cargar tablas
# ------------------------------------------------------------
import pandas as pd
#
alumnos = pd.read_csv("../data/practica_guiada/alumnos.csv")
inscripciones = pd.read_csv("../data/practica_guiada/inscripciones.csv")
cursos = pd.read_csv("../data/practica_guiada/cursos.csv")
#
print(alumnos.shape, inscripciones.shape, cursos.shape)


# ------------------------------------------------------------
# PASO 1: Explorar claves antes de unir (buena práctica)
# ------------------------------------------------------------
print(alumnos["id_alumno"].duplicated().sum())
print(cursos["id_curso"].duplicated().sum())


# ------------------------------------------------------------
# PREGUNTA 1: ¿Qué curso tiene mayor promedio?
# ------------------------------------------------------------
# Aquí SÍ nos interesa solo lo que tiene inscripción y curso
# válidos -> INNER es razonable, pero LEFT desde inscripciones
# también funciona porque calificacion vive ahí.
#
df_cursos = inscripciones.merge(
     cursos,
     on="id_curso",
     how="inner",
     validate="many_to_one"
 )
#
promedio_curso = (
     df_cursos.groupby("curso")["calificacion"]
     .mean()
     .sort_values(ascending=False)
 )
print(promedio_curso)


# ------------------------------------------------------------
# PREGUNTA 2: ¿Qué carrera tiene mejor promedio?
# ------------------------------------------------------------
# Necesitamos inscripciones + alumnos (para la carrera).
# Usamos LEFT desde inscripciones para poder detectar en la
# Pregunta 4 los registros sin alumno asociado.
#
df_carrera = inscripciones.merge(
     alumnos,
     on="id_alumno",
     how="left",
     validate="many_to_one"
 )
#
promedio_carrera = (
     df_carrera.groupby("carrera")["calificacion"]
     .mean()
     .sort_values(ascending=False)
 )
print(promedio_carrera)


# ------------------------------------------------------------
# PREGUNTA 3: ¿Cuántos alumnos tiene cada curso?
# ------------------------------------------------------------
# Aquí queremos TODOS los cursos, incluso los que no tienen
# inscripciones -> LEFT desde cursos.
#
conteo_cursos = (
     cursos.merge(
         inscripciones,
         on="id_curso",
         how="left"
    )
     .groupby("curso")["id_alumno"]
     .nunique()
     .sort_values(ascending=False)
)
print(conteo_cursos)


# ------------------------------------------------------------
# PREGUNTA 4: ¿Hay inscripciones sin alumno asociado?
# ------------------------------------------------------------
# Usamos indicator=True para auditar.
#
auditoria_alumnos = inscripciones.merge(
     alumnos,
     on="id_alumno",
     how="left",
     indicator=True
)
#
print(auditoria_alumnos["_merge"].value_counts())
print(auditoria_alumnos[auditoria_alumnos["_merge"] == "left_only"])


# ------------------------------------------------------------
# PREGUNTA 5: ¿Existen cursos sin estudiantes?
# ------------------------------------------------------------
auditoria_cursos = cursos.merge(
     inscripciones,
     on="id_curso",
     how="left",
     indicator=True
)
#
cursos_sin_alumnos = (
     auditoria_cursos[auditoria_cursos["_merge"] == "left_only"]
     [["id_curso", "curso"]]
     .drop_duplicates()
)
print(cursos_sin_alumnos)


# ------------------------------------------------------------
# EXTRA: guardar el dataset académico integrado
# ------------------------------------------------------------
dataset_academico = inscripciones.merge(
     alumnos, on="id_alumno", how="left"
 ).merge(
     cursos, on="id_curso", how="left"
 )

dataset_academico.to_csv(
     "../data/practica_guiada/dataset_academico_integrado.csv",
     index=False
)
