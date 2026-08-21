import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# CONFIGURACIÓN

st.set_page_config(
    page_title="Dashboard de Ventas",
    layout="wide"
)

st.title("Dashboard Ejecutivo de Ventas")
st.caption("Análisis del desempeño comercial del negocio")


# CARGAR DATOS

@st.cache_data
def cargar_datos():
    df = pd.read_csv("data/ventas.csv")

    # Convertir fecha
    df["Fecha"] = pd.to_datetime(df["Fecha"])

    # Convertir columnas numéricas
    df["Cantidad"] = pd.to_numeric(df["Cantidad"], errors="coerce")
    df["Precio"] = pd.to_numeric(df["Precio"], errors="coerce")
    df["Ventas"] = pd.to_numeric(df["Ventas"], errors="coerce")

    return df


try:
    df = cargar_datos()

except FileNotFoundError:
    st.error("No se encontró el archivo ventas.csv")
    st.stop()


# SIDEBAR - FILTROS

st.sidebar.header("Filtros")

fecha_min = df["Fecha"].min()
fecha_max = df["Fecha"].max()

rango_fechas = st.sidebar.date_input(
    "Selecciona un periodo:",
    value=(fecha_min, fecha_max),
    min_value=fecha_min,
    max_value=fecha_max
)

productos = st.sidebar.multiselect(
    "Producto:",
    options=sorted(df["Producto"].unique()),
    default=sorted(df["Producto"].unique())
)

regiones = st.sidebar.multiselect(
    "Región:",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

vendedores = st.sidebar.multiselect(
    "Vendedor:",
    options=sorted(df["Vendedor"].unique()),
    default=sorted(df["Vendedor"].unique())
)


# APLICAR FILTROS

df_filtrado = df.copy()

if len(rango_fechas) == 2:
    fecha_inicio = pd.to_datetime(rango_fechas[0])
    fecha_fin = pd.to_datetime(rango_fechas[1])

    df_filtrado = df_filtrado[
        (df_filtrado["Fecha"] >= fecha_inicio)
        & (df_filtrado["Fecha"] <= fecha_fin)
    ]


df_filtrado = df_filtrado[
    df_filtrado["Producto"].isin(productos)
    & df_filtrado["Region"].isin(regiones)
    & df_filtrado["Vendedor"].isin(vendedores)
]


if df_filtrado.empty:
    st.warning("No existen datos para los filtros seleccionados.")
    st.stop()


# KPIs

st.subheader("Indicadores principales")

ventas_totales = df_filtrado["Ventas"].sum()
unidades_totales = df_filtrado["Cantidad"].sum()
ticket_promedio = df_filtrado["Ventas"].mean()

producto_mas_vendido = (
    df_filtrado.groupby("Producto")["Cantidad"]
    .sum()
    .idxmax()
)

region_mejor = (
    df_filtrado.groupby("Region")["Ventas"]
    .sum()
    .idxmax()
)


col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Ventas totales",
    f"${ventas_totales:,.2f}"
)

col2.metric(
    "Unidades vendidas",
    f"{unidades_totales:,.0f}"
)

col3.metric(
    "Venta promedio",
    f"${ticket_promedio:,.2f}"
)

col4.metric(
    "Producto líder",
    producto_mas_vendido
)

col5.metric(
    "Mejor región",
    region_mejor
)


st.divider()


# VENTAS POR PRODUCTO

st.subheader("¿Qué producto vende más?")

ventas_producto = (
    df_filtrado.groupby("Producto", as_index=False)
    .agg(
        Ventas=("Ventas", "sum"),
        Cantidad=("Cantidad", "sum")
    )
    .sort_values("Ventas", ascending=False)
)


fig_producto = px.bar(
    ventas_producto,
    x="Producto",
    y="Ventas",
    color="Ventas",
    text_auto=".2s",
    title="Ventas totales por producto"
)

fig_producto.update_layout(
    xaxis_title="Producto",
    yaxis_title="Ventas ($)",
    coloraxis_showscale=False
)

st.plotly_chart(
    fig_producto,
    use_container_width=True
)


# VENTAS POR REGIÓN

st.subheader("¿Qué región tiene mejor desempeño?")

ventas_region = (
    df_filtrado.groupby("Region", as_index=False)
    .agg(
        Ventas=("Ventas", "sum"),
        Cantidad=("Cantidad", "sum")
    )
    .sort_values("Ventas", ascending=False)
)


col1, col2 = st.columns([2, 1])

with col1:

    fig_region = px.bar(
        ventas_region,
        x="Region",
        y="Ventas",
        color="Region",
        text_auto=".2s",
        title="Ventas por región"
    )

    fig_region.update_layout(
        showlegend=False,
        xaxis_title="Región",
        yaxis_title="Ventas ($)"
    )

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )


with col2:

    fig_region_pie = px.pie(
        ventas_region,
        names="Region",
        values="Ventas",
        hole=0.5,
        title="Participación de ventas"
    )

    st.plotly_chart(
        fig_region_pie,
        use_container_width=True
    )


# TENDENCIA TEMPORAL

st.subheader("¿Cómo está funcionando el negocio?")

ventas_fecha = (
    df_filtrado.groupby("Fecha", as_index=False)["Ventas"]
    .sum()
    .sort_values("Fecha")
)


fig_tendencia = px.line(
    ventas_fecha,
    x="Fecha",
    y="Ventas",
    markers=True,
    title="Evolución de ventas en el tiempo"
)

fig_tendencia.update_layout(
    xaxis_title="Fecha",
    yaxis_title="Ventas ($)"
)

st.plotly_chart(
    fig_tendencia,
    use_container_width=True
)


# MEDIA MÓVIL

if len(ventas_fecha) >= 3:

    ventas_fecha["Media móvil"] = (
        ventas_fecha["Ventas"]
        .rolling(window=3)
        .mean()
    )


    fig_media = go.Figure()


    fig_media.add_trace(
        go.Scatter(
            x=ventas_fecha["Fecha"],
            y=ventas_fecha["Ventas"],
            mode="lines+markers",
            name="Ventas"
        )
    )


    fig_media.add_trace(
        go.Scatter(
            x=ventas_fecha["Fecha"],
            y=ventas_fecha["Media móvil"],
            mode="lines",
            name="Media móvil 3 días"
        )
    )


    fig_media.update_layout(
        title="Ventas vs tendencia de corto plazo",
        xaxis_title="Fecha",
        yaxis_title="Ventas ($)"
    )


    st.plotly_chart(
        fig_media,
        use_container_width=True
    )


# DESEMPEÑO DE VENDEDORES

st.subheader("Desempeño de vendedores")

ventas_vendedor = (
    df_filtrado.groupby("Vendedor", as_index=False)
    .agg(
        Ventas=("Ventas", "sum"),
        Cantidad=("Cantidad", "sum")
    )
    .sort_values("Ventas", ascending=False)
)


fig_vendedores = px.bar(
    ventas_vendedor,
    x="Ventas",
    y="Vendedor",
    orientation="h",
    color="Ventas",
    text_auto=".2s",
    title="Ranking de vendedores"
)

fig_vendedores.update_layout(
    yaxis={"categoryorder": "total ascending"},
    coloraxis_showscale=False
)

st.plotly_chart(
    fig_vendedores,
    use_container_width=True
)


# MATRIZ PRODUCTO VS REGIÓN

st.subheader("¿Dónde se vende cada producto?")

tabla_heatmap = pd.pivot_table(
    df_filtrado,
    values="Ventas",
    index="Producto",
    columns="Region",
    aggfunc="sum",
    fill_value=0
)


fig_heatmap = px.imshow(
    tabla_heatmap,
    text_auto=".2s",
    aspect="auto",
    title="Ventas por producto y región"
)

fig_heatmap.update_layout(
    xaxis_title="Región",
    yaxis_title="Producto"
)

st.plotly_chart(
    fig_heatmap,
    use_container_width=True
)


# DETECTAR TENDENCIA PREOCUPANTE

st.subheader("¿Existe alguna tendencia preocupante?")

if len(ventas_fecha) >= 2:

    venta_primera = ventas_fecha.iloc[0]["Ventas"]
    venta_ultima = ventas_fecha.iloc[-1]["Ventas"]

    if venta_primera != 0:

        cambio = (
            (venta_ultima - venta_primera)
            / venta_primera
        ) * 100

    else:
        cambio = 0


    if cambio < -10:

        st.error(
            f"""
            Alerta: Las ventas del último periodo son
            **{abs(cambio):.1f}% menores** respecto al inicio
            del periodo analizado.
            """
        )


    elif cambio > 10:

        st.success(
            f"""
            Tendencia positiva: Las ventas aumentaron
            aproximadamente **{cambio:.1f}%** entre el inicio
            y el final del periodo.
            """
        )


    else:

        st.info(
            f"""
            Las ventas se mantienen relativamente estables.
            El cambio observado es de **{cambio:.1f}%**.
            """
        )


# INSIGHTS AUTOMÁTICOS

st.subheader("Insights del análisis")

producto_lider = ventas_producto.iloc[0]
region_lider = ventas_region.iloc[0]
vendedor_lider = ventas_vendedor.iloc[0]


participacion_producto = (
    producto_lider["Ventas"]
    / ventas_totales
) * 100


participacion_region = (
    region_lider["Ventas"]
    / ventas_totales
) * 100


st.markdown(
    f"""
### Principales hallazgos

**Producto líder:** `{producto_lider["Producto"]}` genera
**${producto_lider["Ventas"]:,.2f}**, equivalente al
**{participacion_producto:.1f}% de las ventas totales**.

**Región con mejor desempeño:** `{region_lider["Region"]}`,
con ventas por **${region_lider["Ventas"]:,.2f}**
y una participación del **{participacion_region:.1f}%**.

**Mejor vendedor:** `{vendedor_lider["Vendedor"]}`,
con **${vendedor_lider["Ventas"]:,.2f}** en ventas.

En total se vendieron **{unidades_totales:,.0f} unidades**
durante el periodo seleccionado.
"""
)


# RECOMENDACIÓN

st.subheader("Recomendación para la dirección")

region_peor = ventas_region.iloc[-1]
producto_peor = ventas_producto.iloc[-1]


st.success(
    f"""
    **Recomendación ejecutiva**

    El negocio debería fortalecer la disponibilidad y promoción de
    **{producto_lider["Producto"]}**, ya que actualmente es el producto
    que más ingresos genera.

    Al mismo tiempo, conviene analizar la región
    **{region_peor["Region"]}**, ya que presenta el menor nivel
    de ventas del periodo.

    Una estrategia posible consiste en replicar las prácticas comerciales
    de **{region_lider["Region"]}** en las regiones de menor desempeño
    y revisar si existen problemas de inventario, demanda, precio
    o desempeño del equipo comercial.

    También debe vigilarse el producto
    **{producto_peor["Producto"]}**, pues es el que actualmente
    aporta menos ingresos.
    """
)


# TABLA DETALLADA

with st.expander("Ver datos utilizados"):

    st.dataframe(
        df_filtrado.sort_values(
            "Fecha",
            ascending=False
        ),
        use_container_width=True
    )


# DESCARGAR DATOS FILTRADOS

csv = df_filtrado.to_csv(
    index=False
).encode("utf-8")


st.download_button(
    label="Descargar datos filtrados",
    data=csv,
    file_name="ventas_filtradas.csv",
    mime="text/csv"
)