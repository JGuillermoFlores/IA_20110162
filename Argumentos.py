#¿Cuántos argumentos se utilizan en cada una de estas llamadas?

#def colores(*args):
#	pass

#colores('rojo', 'azul', 'verde', 'amarillo')      #Hay 4 argumentos
#colores('lila', 'negro', 'rojo')                  #3 argumentos
#colores('rosa')                                   #1 argumento
#colores('marrón', 'naranja')                      #2 argumentos

#Completa el siguiente fragmento de código:
def colores(*args):      #Se crea la funcion
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.') #Se imprime la funcion mandando llamar cada uno de los argumentos en su posicion 

colores('naranja', 'rojo')

#Crea una función que realice la suma de cinco números utilizando solo *args. Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().
def suma(*args):      #Se crea una nueva funcion 
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]   #Se crea la suma con la posicion de los argumentos 
	print('El resultado de sumar estos cinco números es:', resultado) #Se imprime el resultado 

suma(67, 7, 8, 7873, 19, 12)  #Se hace la tipla con los numeros 
