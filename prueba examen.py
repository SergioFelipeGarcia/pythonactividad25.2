#crea una función que nos permita:
#pide la ciudad a donde viajar.
#indica la fecha de salida
#selecciona la estancia
#muestra un detalle al cliente sobre su reserva.
#ciudad destino - checkin/checkout -
#si la estancia es superior a 5 días, descuento es true

#definicion de función
def reservar():
#formulario de registro/entrada
    ciudad=input('dime tu ciudad de destino:') #almacena un string
    fecha=input('indica la fecha de entrada (dd-mm-yyyy):')
    dias=input('indica los dias de estancia:')
#cuidado porque todas las variables son string por el retorno de input

