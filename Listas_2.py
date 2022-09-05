colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa','blanco', 'naranja']
print(colores)
print("El ultimo color es ",colores[-1],"\n\n")

colores = ["\n\n",'rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa','blanco', 'naranja']
print(colores)
del colores[2]
print(colores,"\n\n")

colores = ["\n\n",'rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa','blanco', 'naranja']
print(colores)
colores.remove('lila')
print(colores,"\n\n")

colores = ["\n\n",'rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa','blanco', 'naranja']
print(colores)
almacena_valor = colores.pop(4)
print('El color eliminado y almacenado es:',  almacena_valor)