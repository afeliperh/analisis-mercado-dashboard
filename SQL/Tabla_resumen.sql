select  Producto_Descripcion as 'Producto',
		Producto_Marca as 'Marca',
        Compra_Lugar as 'Supermercado',
        concat(Compra_Precio,' $') as 'Precio Total',
        case
			when Compra_Cantidad < 10 then concat(Compra_Cantidad, ' Unidades')
			when Categ_Id in (5, 7, 12) and Compra_Cantidad >= 10  then concat(Compra_Cantidad, ' ml')
            when Categ_Id not in (5, 7, 12) and Compra_Cantidad >= 10  then concat(Compra_Cantidad, ' gr')
        end as 'Cantidad Total', 
        concat (Compra_Precio_Cantidad, ' $') as 'Precio en gr/ml/unidad',
        case
			when Producto_Requerimiento < 4 then concat(Producto_Requerimiento, ' Unidades')
			when Categ_Id in (5, 7, 12) and Producto_Requerimiento >= 4  then concat(Producto_Requerimiento, ' ml')
            when Categ_Id not in (5, 7, 12) and Producto_Requerimiento >= 4 then concat(Producto_Requerimiento, ' gr')
            else ifnull((Producto_Requerimiento),"Porcion Ilimitada")
        end as'Porcion en gr/ml/unidad',
        case
			when (Producto_Requerimiento*Compra_Precio_Cantidad) is not null then concat(Producto_Requerimiento*Compra_Precio_Cantidad, ' $')
			else ifnull((Producto_Requerimiento*Compra_Precio_Cantidad),"Porcion Ilimitada")
        end as 'Precio en porcion', 
        case
			when Categ_Descripcion in('Carnes','Pollo','Pescado') then 'Proteina'
            when Categ_Descripcion in('Granos','Harinas','Pastas') then 'Carbohidratos'
            when Producto_Descripcion = 'Aguacate' then 'Grasas Saludables'
			when Categ_Descripcion = 'Vegetales' and Producto_Descripcion != 'Aguacate' then 'Vegetales'
            when Categ_Descripcion = 'Lácteos' then 'Lácteos'
            when Categ_Descripcion = 'Bebidas' then 'Bebidas'
            when Categ_Descripcion = 'Frutas' then 'Frutas'
            when Categ_Descripcion = 'Sustitutos' then 'Sustitutos'
            when Categ_Descripcion = 'Nueces' then 'Frutos Secos'
            when Categ_Descripcion = 'Condimentos y Salsas' then 'Condimentos y Salsas'
            when Categ_Descripcion = 'Aceites' then 'Grasas Saludables'
            when Categ_Descripcion = 'Aseo' then 'Aseo'
        end as 'Categoria' 
        from analisis_mercado.productos
	Join analisis_mercado.compras on producto_Id = Compra_ProductoId
    Join analisis_mercado.categorias on Categ_Id = Producto_CategoriaId;