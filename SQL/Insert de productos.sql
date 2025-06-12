insert into analisis_mercado.productos (Producto_Descripcion,Producto_Marca,Producto_CategoriaId)
values ('Papa', 'N/A',(select c.Categ_Id from analisis_mercado.categorias c where c.Categ_Descripcion ='Vegetales')),
	   ('Pimentón', 'N/A',(select c.Categ_Id from analisis_mercado.categorias c where c.Categ_Descripcion ='Vegetales')),
       ('Repollo', "N/A",(select c.Categ_Id from analisis_mercado.categorias c where c.Categ_Descripcion ='Vegetales')),
       ('Zanahoria', "N/A",(select c.Categ_Id from analisis_mercado.categorias c where c.Categ_Descripcion ='Vegetales')),
       ('Vino Blanco', 'Quinta las Cabras',(select c.Categ_Id from analisis_mercado.categorias c where c.Categ_Descripcion ='Bebidas')),
       ('Soda', 'Bretaña',(select c.Categ_Id from analisis_mercado.categorias c where c.Categ_Descripcion ='Bebidas')),
       ('Jugo de naranja', 'Túnez',(select c.Categ_Id from analisis_mercado.categorias c where c.Categ_Descripcion ='Bebidas')),
       ('Maicitos Congelados', 'McCain',(select c.Categ_Id from analisis_mercado.categorias c where c.Categ_Descripcion ='Harinas')),
       ('Papas Congeladas', 'McCain',(select c.Categ_Id from analisis_mercado.categorias c where c.Categ_Descripcion ='Harinas')),
       ('Verduras Congeladas', 'Zenú',(select c.Categ_Id from analisis_mercado.categorias c where c.Categ_Descripcion ='Vegetales')),
       ('Crema de Pistacho', 'Why Not',(select c.Categ_Id from analisis_mercado.categorias c where c.Categ_Descripcion ='Nueces')),
       ('Crema de Avellana', 'Why Not',(select c.Categ_Id from analisis_mercado.categorias c where c.Categ_Descripcion ='Nueces'));
