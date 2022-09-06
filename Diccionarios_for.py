#Itera el diccionario teclado1 con un solo bucle for que muestre esto en la consola:
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',    #Declaramos el diccionario y sus elementos 
	'Precio': '89,99'
}

for x in teclado1:                #Usamos el bucle for para iterar cada elemento del diccionario 
	print(x, '=', teclado1[x] + '.')  #Imprimimos  con el punto 
