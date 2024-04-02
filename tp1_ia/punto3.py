def calcular_promedio_general_del_curso(lista_estudiantes):
    return sum(estudiante[2] for estudiante in lista_estudiantes) / len(lista_estudiantes)

def calcular_promedio_de_edad_del_curso(lista_estudiantes):
    return round(sum(estudiante[1] for estudiante in lista_estudiantes) / len(lista_estudiantes))

def obtener_estudiantes_mayores_de_edad(lista_estudiantes):
    mayores_de_edad = [
        estudiante 
        for estudiante in lista_estudiantes 
        if estudiante[1] >= 18 
    ]

    return mayores_de_edad

def obtener_mejores_tres_estudiantes(lista_estudiantes):

    # Lista ordenada por promedios
    lista_ordenada = sorted(
        lista_estudiantes, 
        key= lambda estudiante : estudiante[2],
        reverse= True
    )

    lista_ordenada = lista_ordenada[:3]
    lista_ordenada = [
        (estudiante[0], estudiante[2]) 
        for estudiante in lista_ordenada
    ]

    return lista_ordenada

nombre = ""
edad = 0
promedio_general = 0.0
estudiantes = []

while True:
    nombre = input("Ingrese el nombre del estudiante:\n")

    if nombre == "*":
        break

    try:
        edad = int(input("Ingrese la edad del estudiante:\n"))
    except:
        print("¡Edad incorrecta!")
        continue
    
    try:
        promedio_general = float(input("Ingrese el promedio general del estudiante:\n"))
    except:
        print("¡Promedio incorrecto!")
        continue
    
    estudiantes.append((nombre, edad, promedio_general))

print("Lista de estudiantes ordenada alfabéticamente:")
print(sorted(estudiantes))

print("Promedio general del curso:")
print(calcular_promedio_general_del_curso(estudiantes))

print("Estudiantes mayores de edad (ordenados desc.):")
print(
    sorted(
        obtener_estudiantes_mayores_de_edad(estudiantes),
        key= lambda estudiante : estudiante[1],
        reverse= True
    )
)

print("Promedio de edad de los estudiantes:")
print(calcular_promedio_de_edad_del_curso(estudiantes))

print("Los tres estudiantes con mejor promedio general:")
print(obtener_mejores_tres_estudiantes(estudiantes))
