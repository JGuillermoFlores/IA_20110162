#Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categoría' y 'Precio'. Muestra la última clave ('Modelo') que queda en la consola.
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',    #Creamos el diccionario1 y sus elementos 
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',     #Creamos el diccionario2 y sus elementos 
	'Precio': '59,99'
}

del teclado1                          #Se utiliza 'del' para eliminar el diccionario1
del teclado2['Categoría']             #Utilizamos 'del' para eliminar elementos del diccionario2
del teclado2['Precio']
print(teclado2['Modelo'])             #Se imprime le modelo del diccionario2 
