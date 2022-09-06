# Valor inicial de x
x = 0


while x <= 30:  #Establecemos los parametros del bucke
	x += 1  # incrementamos la x de 1 en 1 

	
	if x == 4 or x == 6 or x == 10:                  #Usamos if== para generar los saltos en 4,6,10
		print('Se saltó el valor ', x, ' de x')
		continue                              #Generamos el salto

	
	if x == 15:                                   #Usamos if==15 para romper el bucle
		print('Se rompió la ejecución del bucle cuando x valía: ', x)
		break                                            #Rompemos el bucle

	
	print(x)  #Se imprime el resultado final 

