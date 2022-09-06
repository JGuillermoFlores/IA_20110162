#Al siguiente código añádele un par de rangos de edad. Uno de 18 años hasta 45 y otro de más de 100 años hasta 120.
edad = int(input('¿Cuál es tu edad?\n')) #Se le pregunta al usuario su edad 
if edad <= 0:                             #Se declara el primer condicional 
	print('Nadie puede tener esa edad.')  #Se imprime ese mensaje si se cumple
elif edad <= 1 and edad < 18:             #Utilizamos elif para tener mas condiciones dentro del if       
	print('Eres menor de edad.')          #Se imprime en consola si se cumple la condicion
elif edad == 18 and edad <= 45:           #Agregamos la primer condicion de 18 a 45 años 
	print('Eres mayor de edad')           #Se imprime en consola si la condicion se cumple
elif edad <= 100:                         #Establecemos otro elif
	print('Eres mayor de edad.')          #Se imprime en consola si se cumple 
elif edad > 100 and edad  < 120:          #Agregamo la segunda condicion 
	print('Eres alguien muy grande ')
else:                                     #Si ninguna condicion se cumple 
	print('Edad no válida.')              #Se imprime en consola el siguiente mensaje 
