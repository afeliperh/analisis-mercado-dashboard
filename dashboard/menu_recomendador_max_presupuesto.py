
import streamlit as st
import pandas as pd
import itertools

# Cargar datos
df = pd.read_csv("data\Tabla_de_productos.csv")

def limpiar_valores(valor):
    if isinstance(valor, str):
        return valor.replace("$", "").replace(",", "").strip()
    return valor

def extraer_valor_numerico(valor):
    if isinstance(valor, str):
        num = ''.join(c for c in valor if c.isdigit() or c == '.')
        try:
            return float(num)
        except:
            return None
    return valor

# Preprocesamiento general
df["Precio Total"] = df["Precio Total"].apply(limpiar_valores).astype(float)
df["Precio en porcion"] = df["Precio en porcion"].apply(limpiar_valores)
df["Precio en porcion"] = pd.to_numeric(df["Precio en porcion"], errors='coerce')
df["Categoria"] = df["Categoria"].str.strip().str.title()
df["Porcion en gr/ml/unidad"] = df["Porcion en gr/ml/unidad"].fillna("")

# Porción predeterminada para bebidas
bebidas = df["Categoria"] == "Bebidas"
sin_porcion = df["Porcion en gr/ml/unidad"].isin(["", None])
df.loc[bebidas & sin_porcion, "Porcion en gr/ml/unidad"] = "250 ml"
df["Cantidad Total (ml)"] = df["Cantidad Total"].apply(extraer_valor_numerico)

filtro_bebidas_porcion = bebidas & df["Precio en porcion"].isna()
df.loc[filtro_bebidas_porcion, "Precio en porcion"] = (
    df["Precio Total"] / df["Cantidad Total (ml)"] * 250
)

# Categorías a usar
categorias_validas = [
    "Grasas Saludables", "Frutos Secos", "Proteina", "Sustitutos",
    "Carbohidratos", "Lácteos", "Bebidas", "Vegetales", "Frutas"
]

df = df[df["Categoria"].isin(categorias_validas)].dropna(subset=["Precio en porcion"])

# Streamlit UI
st.title("💡 Recomendador de Menú - Uso Óptimo del Presupuesto")

presupuesto = st.number_input("💰 Presupuesto disponible ($):", min_value=0, step=500, value=6000)
st.sidebar.header("🍽️ Porciones deseadas por categoría")
porciones_deseadas = {}
for categoria in categorias_validas:
    porciones_deseadas[categoria] = st.sidebar.number_input(
        f"{categoria}:", min_value=0, step=1, value=1
    )

# Función para seleccionar combinaciones óptimas
def encontrar_mejor_combinacion(df, porciones_deseadas, presupuesto):
    candidatos = []
    for categoria, cantidad in porciones_deseadas.items():
        if cantidad > 0:
            productos_cat = df[df["Categoria"] == categoria]
            productos_cat = productos_cat.sort_values("Precio en porcion").head(cantidad * 4)  # más variedad
            candidatos.append(list(itertools.combinations(productos_cat.index, min(len(productos_cat), cantidad))))
        else:
            candidatos.append([()])

    mejores_productos = []
    mejor_total = 0

    for combinacion in itertools.product(*candidatos):
        ids = [i for grupo in combinacion for i in grupo]
        seleccion = df.loc[ids].drop_duplicates()
        total = seleccion["Precio en porcion"].sum()
        if total <= presupuesto and total > mejor_total:
            mejor_total = total
            mejores_productos = seleccion

    return mejores_productos, mejor_total

# Ejecutar recomendación
if st.button("📋 Generar menú"):
    resultado, total = encontrar_mejor_combinacion(df, porciones_deseadas, presupuesto)
    if not resultado.empty:
        st.subheader("✅ Menú recomendado")
        st.dataframe(resultado[[
            "Producto", "Marca", "Supermercado", "Categoria", 
            "Porcion en gr/ml/unidad", "Precio en porcion"
        ]])
        st.markdown(f"**💸 Total utilizado: ${total:.2f}**")
        st.success("Menú generado aprovechando al máximo tu presupuesto.")
    else:
        st.error("❌ No se encontró un menú que cumpla los requisitos dentro del presupuesto.")
