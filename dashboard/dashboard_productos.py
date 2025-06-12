import streamlit as st
import pandas as pd

# Cargar datos
df = pd.read_csv("data\Tabla_de_productos.csv")

# Limpieza
def limpiar_valores(valor):
    if isinstance(valor, str):
        return valor.replace("$", "").replace(",", "").strip()
    return valor

df["Precio Total"] = df["Precio Total"].apply(limpiar_valores).astype(float)
df["Precio en gr/ml/unidad"] = df["Precio en gr/ml/unidad"].apply(limpiar_valores).astype(float)

def convertir_precio_porcion(valor):
    if "Ilimitada" in str(valor):
        return None
    return float(limpiar_valores(valor))

df["Precio en porcion"] = df["Precio en porcion"].apply(convertir_precio_porcion)

# Título
st.title("🛒 Dashboard de Productos por Porción")

# Filtros
st.sidebar.header("🔎 Filtros")

# ✅ Múltiples supermercados
supermercados = st.sidebar.multiselect(
    "Selecciona uno o más supermercados:",
    options=sorted(df["Supermercado"].unique()),
    default=sorted(df["Supermercado"].unique())
)

# ✅ Múltiples categorías
categorias = st.sidebar.multiselect(
    "Selecciona una o más categorías:",
    options=sorted(df["Categoria"].unique()),
    default=sorted(df["Categoria"].unique())
)

# 🔍 Búsqueda por nombre de producto
buscar = st.sidebar.text_input("Buscar producto (nombre parcial):")

# 💰 Rango de precio por porción
min_precio = df["Precio en porcion"].dropna().min()
max_precio = df["Precio en porcion"].dropna().max()
rango_precio = st.sidebar.slider(
    "Rango de precio por porción ($):",
    float(min_precio), float(max_precio),
    (float(min_precio), float(max_precio))
)

# Aplicar filtros
df_filtrado = df[
    (df["Supermercado"].isin(supermercados)) &
    (df["Categoria"].isin(categorias)) &
    (df["Producto"].str.contains(buscar, case=False, na=False)) &
    (df["Precio en porcion"].fillna(0).between(rango_precio[0], rango_precio[1]))
]

# Mostrar tabla
st.subheader("📋 Productos filtrados")
st.dataframe(df_filtrado[["Producto", "Marca", "Supermercado", "Precio Total", "Cantidad Total", "Porcion en gr/ml/unidad", "Precio en porcion"]])

# Gráfico
st.subheader("💸 Precio por porción")
df_bar = df_filtrado.dropna(subset=["Precio en porcion"])
if not df_bar.empty:
    st.bar_chart(df_bar.set_index("Producto")["Precio en porcion"])
else:
    st.warning("⚠️ No hay productos que coincidan con los filtros actuales.")
