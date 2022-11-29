#crea una clase llamada Producto
#nombre, unidades y precio
#creas un producto camisa, 10, 9.95 de precio
#muestra el nombre de producto por consola
class Producto:
    def __init__(self,nombre,unidades,precio):
        self.nombre=nombre
        self.unidades=unidades
        self.precio=precio

    def creacion(self):
        print(f'el nombre del producto es:{self.nombre}')

    def infoProducto(self):
        print(f'el inventario valorado es: {self.nombre}-{self.unidades}-{self.precio}-{self.unidades*self.precio} ')


producto1=Producto('camisa',10,9.95)
producto1.creacion()

producto1.infoProducto()





#crea un método de infoProducto. Muestra el nombre, unidades, precio y inventario valorado (uxp)

#práctica de sobreescritura.
#crea una clase llamada Servicio
#tiene un método llamado consultarDetalle que muestra. el servicio es básico.
#la empresa tiene dos servicios. estándar y premium. Son dos clases que derivan de Servicio
#la clase Estandar y Premium tienen un método llamado consultarDetalle y explican que son
#servicio estándar y premium respectivamente.
#pide por consola un servicio. Elegimos premium y te muestra el resultado de consultarDetalle



class Servicio:


    def consultarDetalle(self):
        print('el servicio es básico')





class Estandar(Servicio):
    def consultarDetalle(self):
        print('el servicio es estandar')





class Premium(Servicio):

    def consultarDetalle(self):
        print('el servicio es premium')

producto2 = Premium()
producto2.consultarDetalle()
producto2=Estandar()
producto2.consultarDetalle()