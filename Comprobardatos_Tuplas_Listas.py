colores = input('Introduce un color:\n')     #Perimitimos que el usuario introduca los datos 
tupla_colores = ('beige', 'tinto', 'verde', 'rojo')  #Creamos la tupla con sus elementos 

if colores in tupla_colores[0]:              #Ponemos la funcion in con su respectiva posicion y las condicionaes 
	print('El color beige está admitido')    #imprimimos si se cumple la condicion
elif colores in tupla_colores[1]:             #Ponemos la funcion in con su respectiva posicion
	print('El color tinto está admitido')     #imprimimos si se cumple la condicion
elif colores in tupla_colores[2]:             #Ponemos la funcion in con su respectiva posicion 
	print('El color verde está admitido')      #imprimimos si se cumple la condicion
elif colores in tupla_colores[3]:             #Ponemos la funcion in con su respectiva posicion
	print('El color rojo está admitido')      #imprimimos si se cumple la condicion
else:                                         #Si no se cumple ninguna condicion 
	print('Color no admitido')                #Se imprime en consola 
