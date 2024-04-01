import random

def generar_lista_random(tamanio, lim_inf, lim_sup):
    lista = []

    for i in range(0, tamanio):
        lista.append(random.randrange(lim_inf, lim_sup))

    return lista

def remover_duplicados(lista):
    return list(dict.fromkeys(lista))

def generar_lista_con_cuadrados_y_cubos(lista):
    return [(elem, elem**2, elem**3) for elem in lista]

lista1 = generar_lista_random(15, 1, 11)
lista2 = generar_lista_random(15, 11, 21)

print("Lista 1 original:")
print(lista1)
print("Lista 2 original:")
print(lista2)


lista2 = remover_duplicados(lista2)

print("Lista 2 sin duplicados:")
print(lista2)

lista1.sort()
lista2.sort(reverse=True)

print("Lista 1 ordenada asc.:")
print(lista1)
print("Lista 2 sin duplicados ordenada desc.:")
print(lista2)

print("Lista 2 con cuadrados y cubos:")
print(generar_lista_con_cuadrados_y_cubos(lista2))

lista3 = lista1 + lista2
print("Lista 3:")
print(lista3)