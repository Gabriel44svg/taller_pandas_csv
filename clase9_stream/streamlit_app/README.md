# App interactiva (Streamlit) — Clase 9

Demo dinámica de Regresión Lineal para complementar el Live Coding y el Challenge
de la presentación. Todo se recalcula en vivo cuando cambias un control.

## Instalar y correr

```bash
cd streamlit_app
pip install -r requirements.txt
streamlit run app.py
```

Se abre en `http://localhost:8501`.

## Qué incluye

Barra lateral (controles):
- Elegir dataset: `viviendas.csv` (Live Coding) o `viviendas_reto.csv` (Challenge)
- Elegir qué features (X) usar — puedes quitar/agregar variables en vivo
- Ajustar `test_size` y `random_state` del `train_test_split`
- Activar/desactivar imputación de NaN (útil para mostrar por qué el EDA importa)

Pestañas:
1. **Datos** — head, `describe()`, NaN, matriz de correlación
2. **Train/Test** — tamaños de la partición y el código equivalente
3. **Modelo y métricas** — coeficientes, MAE/RMSE/R² en Test, gráfico real vs
   predicción, comparación contra baseline (predecir la media)
4. **Overfitting/Underfitting** — compara MAE/RMSE/R² de Train vs Test y da un
   diagnóstico automático (overfitting, underfitting o buena generalización)
5. **Predicción interactiva** — sliders para armar una vivienda nueva y ver el
   precio estimado en tiempo real

## Ideas para usarla en clase

- Cambia el dataset de `viviendas.csv` a `viviendas_reto.csv` frente al grupo y
  pide que interpreten cómo cambian las métricas.
- Quita `distancia_centro` de las features en el reto y muestra cómo baja el R².
- Sube `test_size` a 0.5 y pregunta qué le pasa a la confiabilidad de las métricas.
- Desactiva la imputación de NaN para mostrar el error que lanza sklearn y por
  qué el EDA (Paso 2 de la presentación) no es opcional.
