insert into analisis_mercado.compras (Compra_ProductoId,Compra_Fecha,Compra_Lugar,Compra_Precio,Compra_Cantidad)
values ((select producto_Id from analisis_mercado.productos where Producto_Descripcion ='Vino Blanco'),CURRENT_DATE(),'D1','16950','750'),
		((select producto_Id from analisis_mercado.productos where Producto_Descripcion ='Vino Tinto'),CURRENT_DATE(),'D1','22950','500');
        ((select producto_Id from analisis_mercado.productos where Producto_Descripcion ='Salsa Napolitana'),CURRENT_DATE(),'Alkosto','10430','500'),
        ((select producto_Id from analisis_mercado.productos where Producto_Descripcion ='Mayonesa'),CURRENT_DATE(),'Alkosto','22900','440');