colores = ['rojo', 'azul', 'verde', 'amarillo']
print(colores)



colores.append('morado')
print(colores)



colores.insert(4,'gris')
print(colores)

colores.sort()
print(colores)

colores.sort(reverse=1)
print(colores)


print(sorted(colores))
print(colores)

print("La lista contiene",len(colores),"colores")