"""
    ! Semana3
    ? Resumen de la semana 3, la introduccion a python 
"""

# Variable de tipo diccionario que almacena notas
puntos = {'A':10,'B':8.0,'C':5.0}
numero_cursos = 0
total_puntos = 0
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
        numero_cursos += 1
        total_puntos += puntos[nota]

if numero_cursos > 0:
    print('Su promedio es: {0}'.format(total_puntos/numero_cursos))        
