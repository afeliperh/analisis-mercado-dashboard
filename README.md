# Recomendador de Menús Saludables por Presupuesto

SQL + Streamlit · Dashboard interactivo con lógica de optimización

Este proyecto permite visualizar, filtrar y recomendar combinaciones de alimentos según su precio por porción, categoría y presupuesto disponible.
Está construido sobre una base de datos relacional en SQL, con lógica de selección optimizada para ayudar al usuario a maximizar su compra dentro de un presupuesto determinado.

---

## Funcionalidades

- Visualización de los productos saludables por categoría y supermercado.
- Cálculo automático del precio por porción de cada alimento.
- Recomendador inteligente de menú por tipo de alimento (carbohidrato, proteína, bebida, etc.).
- Optimización para cumplir con el número deseado de alimentos dentro del presupuesto.
- Categorización automática de bebidas con porción estándar (250 ml).

---

## Cómo usar

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

## Estructura del repositorio

- `sql/`: Scripts SQL para construir la base de datos relacional
- `data/`: Exportación CSV desde MySQL con productos y precios
- `dashboard/`: Aplicaciones de visualización y recomendación en Streamlit
- `README.md`: Documentación del proyecto

---

### Casos de uso potencial
- Educación nutricional con presupuesto limitado.
- Aplicaciones en EPS, bienestar corporativo o mercados comunitarios.
- Prototipo funcional para apps de salud o nutrición consciente.

---

## 👤 Autor

**Andrés Felipe Ruiz Hernández**  
Ingeniero Biomédico | Ciencia de Datos aplicada a salud, nutrición y consumo consciente  
📍 Bogotá, Colombia  
🔗 [LinkedIn](https://www.linkedin.com/in/andresfeliperuiz)
🔗 [APP en vivo](https://analisis-mercado-dashboard.onrender.com)
