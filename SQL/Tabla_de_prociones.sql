select Producto_Descripcion as 'Producto', 
	Case
		When (Categ_Id in(5, 7, 12) ) and (Producto_Requerimiento >= 2) then concat(Producto_Requerimiento, ' ml')
		When (Categ_Id not in(5, 7, 12) ) and (Producto_Requerimiento >= 2) then concat(Producto_Requerimiento, ' gr')
        When Producto_Requerimiento < 2 then concat(Producto_Requerimiento, ' Unidad')
	end as 'Porción en gr/ml/unidades'
from analisis_mercado.productos 
Join analisis_mercado.categorias on Producto_CategoriaId=Categ_Id
where Producto_Requerimiento is not null;

    