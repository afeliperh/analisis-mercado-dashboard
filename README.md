# 🛒 Análisis de Precios por Porción - SQL + Dashboard Interactivo

Este proyecto permite visualizar, filtrar y recomendar productos de supermercado según su precio por porción, categoría y presupuesto, utilizando una base de datos relacional en SQL y dashboards interactivos en Python con Streamlit.

---

## 💡 Funcionalidades

- Visualización de productos filtrados por categoría y supermercado
- Cálculo automático del precio por porción
- Recomendador de menú personalizado por porciones y presupuesto
- Optimización para usar el presupuesto al máximo
- Categorización automática de bebidas con porción estándar (250 ml)

---

## 🚀 Cómo usar

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/analisis-mercado-dashboard.git
```

2. Instala las dependencias:

```bash
pip install -r dashboard/requirements.txt
```

3. Ejecuta la aplicación recomendadora:

```bash
streamlit run dashboard/menu_recomendador_max_presupuesto.py
streamlit run dashboard/dashboard_productos.py
```

---

## 📦 Estructura del repositorio

- `sql/`: Scripts SQL para construir la base de datos relacional
- `data/`: Exportación CSV desde MySQL con productos y precios
- `dashboard/`: Aplicaciones de visualización y recomendación en Streamlit
- `README.md`: Documentación del proyecto

---

## 👤 Autor

**Andrés Felipe Ruiz Hernández**  
Ingeniero Biomédico | Ciencia de Datos aplicada a salud, nutrición y consumo consciente  
📍 Bogotá, Colombia  
🔗 [LinkedIn](https://www.linkedin.com/in/andresfeliperuiz)
