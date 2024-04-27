'''
Punto a):
Para determinar la menor cantidad de colores necesarios para resolver el problema se podría:
- Empezar con un dominio de colores que sea igual en cantidad a las cantidades de regiones a colorear,
  intentar resolver el problema, si se pudo resolver restar un color al dominio e intentar nuevamente
  hasta que el problema no pueda resolverse. Cuando no se pueda resolver el problema volver al dominio
  de la iteración anterior para obtener la mínima cantidad de colores.
- Empezar con un dominio de colores que solo tenga un color, intentar resolver el problema, si no se pudo
  resolver el problema añadir un color al dominio e intentar nuevamente hasta resolver el problema. La 
  primera vez que se logre resolver el problema se tendrá la cantidad mínima de colores.
'''

from simpleai.search import CspProblem, backtrack

variables = (
    'Argentina',
    'Chile',
    'Uruguay',
    'Paraguay',
    'Bolivia',
    'Brasil',
    'Perú',
    'Ecuador',
    'Colombia',
    'Venezuela',
    'Guayana',
    'Suriname',
    'Guyana Francesa'
)

domains = {
    'Argentina' : ['red', 'green', 'blue', 'yellow'],
    'Chile' : ['red', 'green', 'blue', 'yellow'],
    'Uruguay' : ['red', 'green', 'blue', 'yellow'],
    'Paraguay' : ['red', 'green', 'blue', 'yellow'],
    'Bolivia' : ['red', 'green', 'blue', 'yellow'],
    'Brasil' : ['red', 'green', 'blue', 'yellow'],
    'Perú' : ['red', 'green', 'blue', 'yellow'],
    'Ecuador' : ['red', 'green', 'blue', 'yellow'],
    'Colombia' : ['red', 'green', 'blue', 'yellow'],
    'Venezuela' : ['red', 'green', 'blue', 'yellow'],
    'Guayana' : ['red', 'green', 'blue', 'yellow'],
    'Suriname' : ['red', 'green', 'blue', 'yellow'],
    'Guyana Francesa' : ['red', 'green', 'blue', 'yellow']
}

def const_different(variables, values):
    return values[0] != values[1]

constraints = [
    (('Argentina', 'Chile'), const_different),
    (('Argentina', 'Uruguay'), const_different),
    (('Argentina', 'Paraguay'), const_different),
    (('Argentina', 'Bolivia'), const_different),
    (('Argentina', 'Brasil'), const_different),
    (('Uruguay', 'Brasil'), const_different),
    (('Chile', 'Bolivia'), const_different),
    (('Chile', 'Perú'), const_different),
    (('Bolivia', 'Paraguay'), const_different),
    (('Bolivia', 'Brasil'), const_different),
    (('Bolivia', 'Perú'), const_different),
    (('Perú', 'Brasil'), const_different),
    (('Perú', 'Ecuador'), const_different),
    (('Perú', 'Colombia'), const_different),
    (('Ecuador', 'Colombia'), const_different),
    (('Colombia', 'Brasil'), const_different),
    (('Colombia', 'Venezuela'), const_different),
    (('Venezuela', 'Brasil'), const_different),
    (('Venezuela', 'Guayana'), const_different),
    (('Guayana', 'Brasil'), const_different),
    (('Guayana', 'Suriname'), const_different),
    (('Suriname', 'Brasil'), const_different),
    (('Suriname', 'Guyana Francesa'), const_different),
    (('Guyana Francesa', 'Brasil'), const_different),
]

my_problem = CspProblem(variables, domains, constraints)

output = backtrack(my_problem)
print('\nColor mapping:\n')
for k, v in output.items():
    print(k, '==>', v)