"""
Clase 9 - Introducción a Machine Learning
App interactiva en Streamlit: Train/Test Split, Regresión Lineal,
métricas de evaluación, overfitting/underfitting y predicción en vivo.

Ejecutar con:
    streamlit run app.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# ------------------------------------------------------------
# Configuración general
# ------------------------------------------------------------

st.set_page_config(
    page_title="Clase 9 · Introducción a Machine Learning",
    page_icon="🏠",
    layout="wide",
)

DATASETS = {
    "viviendas.csv (Live Coding)": "data/viviendas.csv",
    "viviendas_reto.csv (Challenge)": "data/viviendas_reto.csv",
}

TARGET_COL = "precio"

# ------------------------------------------------------------
# Sidebar: controles
# ------------------------------------------------------------

st.sidebar.title("⚙️ Controles del experimento")

dataset_label = st.sidebar.selectbox("Dataset", list(DATASETS.keys()))
data_path = DATASETS[dataset_label]

df_raw = pd.read_csv(data_path)
all_features = [c for c in df_raw.columns if c != TARGET_COL]

st.sidebar.markdown("---")
st.sidebar.subheader("Features (X)")
selected_features = st.sidebar.multiselect(
    "Variables predictoras a usar",
    options=all_features,
    default=all_features,
)

st.sidebar.markdown("---")
st.sidebar.subheader("Train / Test Split")
test_size = st.sidebar.slider("test_size", 0.10, 0.50, 0.20, 0.05)
random_state = st.sidebar.number_input("random_state", value=42, step=1)

st.sidebar.markdown("---")
impute = st.sidebar.checkbox(
    "Imputar NaN con la mediana (Train)", value=True,
    help="El dataset tiene algunos valores faltantes a propósito. "
         "Si lo desactivas, sklearn arrojará un error — útil para "
         "mostrar por qué el EDA importa antes de modelar.",
)

st.sidebar.markdown("---")
st.sidebar.caption(
    "Cambia cualquier control y todo el flujo — split, modelo, "
    "métricas y gráficas — se vuelve a calcular automáticamente."
)

# ------------------------------------------------------------
# Encabezado
# ------------------------------------------------------------

st.title("🏠 Introducción a Machine Learning")
st.subheader("Regresión Lineal para predecir precio de vivienda — demo en vivo")

st.markdown(
    f"**Dataset activo:** `{data_path}`  ·  **Target (y):** `{TARGET_COL}`  ·  "
    f"**Filas:** {df_raw.shape[0]}  ·  **Columnas:** {df_raw.shape[1]}"
)

tabs = st.tabs([
    "1️⃣ Datos",
    "2️⃣ Train/Test",
    "3️⃣ Modelo y métricas",
    "4️⃣ Overfitting / Underfitting",
    "5️⃣ Predicción interactiva",
])

# ------------------------------------------------------------
# TAB 1: Exploración de datos
# ------------------------------------------------------------

with tabs[0]:
    st.markdown("### Vista previa")
    st.dataframe(df_raw.head(10), use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Estadísticas descriptivas")
        st.dataframe(df_raw.describe(), use_container_width=True)

    with col2:
        st.markdown("### Valores faltantes")
        na_counts = df_raw.isna().sum()
        na_counts.name = "NaN"
        st.dataframe(na_counts, use_container_width=True)
        if na_counts.sum() == 0:
            st.info("No hay valores faltantes en este dataset.")

    st.markdown("### Matriz de correlación")
    corr = df_raw.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(5, 4))
    im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=45, ha="right")
    ax.set_yticks(range(len(corr.columns)))
    ax.set_yticklabels(corr.columns)
    for i in range(len(corr.columns)):
        for j in range(len(corr.columns)):
            ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center", fontsize=7)
    fig.colorbar(im, ax=ax, shrink=0.8)
    st.pyplot(fig)

# ------------------------------------------------------------
# Preparar X, y (usado en el resto de los tabs)
# ------------------------------------------------------------

if len(selected_features) == 0:
    st.warning("Selecciona al menos una feature en la barra lateral para continuar.")
    st.stop()

df = df_raw.copy()

if impute:
    for col in selected_features:
        if df[col].isna().any():
            df[col] = df[col].fillna(df[col].median())

# Si el usuario apaga la imputación y quedan NaN, los quitamos para no romper sklearn,
# pero avisamos — esto es intencional para ilustrar por qué el EDA importa.
missing_before = len(df)
df = df.dropna(subset=selected_features + [TARGET_COL])
missing_after = len(df)

X = df[selected_features]
y = df[TARGET_COL]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=int(random_state)
)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

pred_train = modelo.predict(X_train)
pred_test = modelo.predict(X_test)

mae_train = mean_absolute_error(y_train, pred_train)
mae_test = mean_absolute_error(y_test, pred_test)
rmse_train = mean_squared_error(y_train, pred_train) ** 0.5
rmse_test = mean_squared_error(y_test, pred_test) ** 0.5
r2_train = r2_score(y_train, pred_train)
r2_test = r2_score(y_test, pred_test)

media_train = y_train.mean()
pred_baseline = np.full_like(y_test, fill_value=media_train, dtype=float)
mae_baseline = mean_absolute_error(y_test, pred_baseline)

# ------------------------------------------------------------
# TAB 2: Train / Test
# ------------------------------------------------------------

with tabs[1]:
    if not impute and missing_after < missing_before:
        st.warning(
            f"Se descartaron {missing_before - missing_after} filas con NaN porque "
            "la imputación está desactivada."
        )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Filas totales", len(df))
    c2.metric("Train", len(X_train))
    c3.metric("Test", len(X_test))
    c4.metric("Features usadas", len(selected_features))

    st.markdown("### Código equivalente")
    st.code(
        "from sklearn.model_selection import train_test_split\n\n"
        "X_train, X_test, y_train, y_test = train_test_split(\n"
        f"    X, y, test_size={test_size}, random_state={int(random_state)}\n"
        ")",
        language="python",
    )

    st.markdown("### Muestra de Train")
    st.dataframe(X_train.assign(**{TARGET_COL: y_train}).head(), use_container_width=True)

# ------------------------------------------------------------
# TAB 3: Modelo y métricas
# ------------------------------------------------------------

with tabs[2]:
    st.markdown("### Coeficientes del modelo")
    coefs = pd.DataFrame({
        "feature": selected_features,
        "coeficiente": modelo.coef_,
    }).sort_values("coeficiente", key=abs, ascending=False)
    st.dataframe(coefs, use_container_width=True)
    st.caption(f"Intercepto (β₀): {modelo.intercept_:,.2f}")

    st.markdown("### Métricas sobre Test")
    m1, m2, m3 = st.columns(3)
    m1.metric("MAE", f"{mae_test:,.0f}")
    m2.metric("RMSE", f"{rmse_test:,.0f}")
    m3.metric("R²", f"{r2_test:.3f}")

    st.markdown("### Real vs Predicción (Test)")
    fig2, ax2 = plt.subplots(figsize=(5, 5))
    ax2.scatter(y_test, pred_test, alpha=0.5, edgecolor="k", linewidth=0.3)
    lims = [min(y_test.min(), pred_test.min()), max(y_test.max(), pred_test.max())]
    ax2.plot(lims, lims, "r--", label="y = x (ideal)")
    ax2.set_xlabel("Precio real")
    ax2.set_ylabel("Precio predicho")
    ax2.set_title("Real vs Predicción")
    ax2.legend()
    st.pyplot(fig2)

    st.markdown("### Comparación contra baseline (predecir siempre la media)")
    bl_df = pd.DataFrame({
        "estrategia": ["Baseline (media)", "Modelo (Regresión Lineal)"],
        "MAE": [mae_baseline, mae_test],
    }).set_index("estrategia")
    st.bar_chart(bl_df)

    mejora_pct = (mae_baseline - mae_test) / mae_baseline * 100
    if mejora_pct > 0:
        st.success(f"El modelo mejora el baseline en {mejora_pct:.1f}% de MAE.")
    else:
        st.error(
            f"El modelo NO supera al baseline (empeora en {-mejora_pct:.1f}%). "
            "Revisen las features seleccionadas."
        )

# ------------------------------------------------------------
# TAB 4: Overfitting / Underfitting
# ------------------------------------------------------------

with tabs[3]:
    st.markdown("### Error en Train vs Test")

    comp = pd.DataFrame({
        "conjunto": ["Train", "Test"],
        "MAE": [mae_train, mae_test],
        "RMSE": [rmse_train, rmse_test],
        "R2": [r2_train, r2_test],
    })
    st.dataframe(comp.set_index("conjunto"), use_container_width=True)
    st.bar_chart(comp.set_index("conjunto")[["MAE", "RMSE"]])

    ratio = mae_test / mae_train if mae_train > 0 else float("inf")

    st.markdown("### Diagnóstico automático")
    if ratio > 1.5:
        st.error(
            f"⚠️ Posible **overfitting**: MAE_test es {ratio:.2f}× MAE_train "
            "(el modelo generaliza peor de lo que memoriza)."
        )
    elif mae_train > mae_baseline and mae_test > mae_baseline:
        st.warning(
            "⚠️ Posible **underfitting**: ni siquiera en Train el modelo supera "
            "al baseline — probablemente le faltan features o relaciones más ricas."
        )
    else:
        st.success(
            "✅ Buen indicio de generalización: MAE_train ≈ MAE_test y ambos "
            "superan al baseline."
        )

    st.caption(
        "Prueba quitar features en la barra lateral, o comparar viviendas.csv vs "
        "viviendas_reto.csv, para ver cómo cambia este diagnóstico en vivo."
    )

# ------------------------------------------------------------
# TAB 5: Predicción interactiva
# ------------------------------------------------------------

with tabs[4]:
    st.markdown("### Arma una vivienda nueva y observa la predicción en tiempo real")

    input_values = {}
    cols = st.columns(len(selected_features))
    for i, feat in enumerate(selected_features):
        col_data = df[feat]
        with cols[i]:
            input_values[feat] = st.slider(
                feat,
                float(col_data.min()),
                float(col_data.max()),
                float(col_data.median()),
            )

    nueva = pd.DataFrame([input_values])[selected_features]
    precio_estimado = modelo.predict(nueva)[0]

    st.markdown("---")
    c1, c2 = st.columns([1, 2])
    with c1:
        st.metric("Precio estimado", f"${precio_estimado:,.0f}")
        st.metric("Precio promedio (Train)", f"${media_train:,.0f}")
    with c2:
        st.dataframe(nueva, use_container_width=True)

    st.caption(
        "Esta predicción usa el mismo modelo entrenado en la pestaña 3, con las "
        "features y el split configurados en la barra lateral."
    )

st.markdown("---")
st.caption("Diplomado de Python y Análisis de Datos · Universidad Marista · Clase 9")
