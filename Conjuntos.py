grupo_A = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14])                #CONJUNTO UNIVERSO
grupo_B = set(["         "])                                     #CONJUNTO VACIO
grupo_C = set([1,2,3,5,7,11,13])                                 #CONJUNTO A
grupo_D = set([2,4,6,8,10,12])                                   #CONJUNTO B 

print("Los elementos del universo son",grupo_A)
print("Los elementos del conjunto vacio son",grupo_B)
print("Los elementos del conjunto A son",grupo_C)
print("Los elementos del conjunto B son",grupo_D)

gAB = grupo_C.union(grupo_D)
print("\n\nLos elementos del conjunto A union B son",gAB)

gAB = grupo_C.intersection(grupo_D)
print("\n\nLos elementos del conjunto A interseccion B son",gAB)

gAB = grupo_C.difference(grupo_D)
print("\n\nLos elementos del conjunto A diferencia B son",gAB)

gA = grupo_C.issubset(grupo_A)       
print ("\n\nEl conjunto A, es subconjunto del universo? ",gA)
gA = grupo_D.issubset(grupo_A)       
print ("El conjunto B, es subconjunto del universo? ",gA)
gB = grupo_B.issubset(grupo_A)       
print ("El conjunto vacio, es subconjunto del universo? ",gB)

gA = grupo_A.issuperset(grupo_C)       
print ("\n\nEl universo es un superconjunto del conjunto A? ",gA)
gA = grupo_A.issuperset(grupo_D)       
print ("El universo es un superconjunto del conjunto B? ",gA)
gA = grupo_A.issuperset(grupo_B)       
print ("El universo es un superconjunto del conjunto vacio? ",gA)

gI = grupo_C==grupo_D
print("\n\nEl conjunto A y B son iguales? ", gI)


gI = grupo_A.symmetric_difference(grupo_C)       
print("\n\nLa difererencia simetrica del universo y el conjunto A es:", gI)
gI = grupo_A.symmetric_difference(grupo_D)       
print("La difererencia simetrica del universo y el conjunto B es:", gI)

def get_cart_prd(pools):
  result = [[]]
  for pool in pools:
    result = [x+[y] for x in result for y in pool]
  return result

print("\n\nProducto cartesiano")

mylists = [["A", "B", "C"],
    [1,2,3]]
print (mylists)
print(get_cart_prd(mylists))