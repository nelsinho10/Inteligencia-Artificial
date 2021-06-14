"""
    ! Semana3
    ? Resumen de la semana 3, la introduccion a python 
"""

# Variable de tipo diccionario que almacena notas
puntos = {'A':10,'B':8.0,'C':5.0}
# Variable de tipo entero
numeroCursos = 0
# Variable de tipo puntos
totalPuntos = 0
# Variable de tipo boolean
fin = False

# Mientras no sea Verdadero
while not fin:
    nota = input('Ingrese una nota: ')
    
    if nota == '':
        fin = True

    # Si la nota no esta en el diccionario puntos 
    elif nota not in puntos:
        print('Nota desconocida')

    else:
        numeroCursos += 1
        totalPuntos += puntos[nota]

if numeroCursos > 0:
    print('Su promedio es: %s' %(totalPuntos/numeroCursos))        


"""
    ! NOTAS
    ? Alias: Es la forma de asignar varios identificadores a un mismo objeto 
    * Cuando se asigna otro valor al objeto se rompe el alias

    ? Clases Predefinidas
    * Son clases que no necesitan la importacion de modulos externos para funcionar

    ? Clases Mutables e Inmutables
    * Mutables: Una vez creada la clase puede cambiar de valor 
    * Inmutables Una vez creada la clase no puede cambiar su valor
"""