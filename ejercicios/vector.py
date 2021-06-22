### Ejercicio:
# Implemente los métodos de la clase Vector para que funciones de acuerdo a
# lo que indican sus cadena de documentación y se obtenga los resultados que
# se indican en el código de uso.
#
# Antes de subir su ejercicio al campus virtual compruebe su correctiud
# en el siguiente enlace:
#   https://rp-autograder.herokuapp.com/
# (El autograder empezará a funcionar a más tardar hoy 21 de junio a las 
#  9:00pm)
#
# PD: El texto después del caracter '#' en Python es un comentario.
# La palabra 'pass' puede borrarla cuando haya puesto código al método.

class Vector:

  def __init__(self, elementos):
    """Inicializa el vector con el iterable elementos.
    Lanza una excepción en caso de que elementos no sea iterable."""
    pass
  
  def sumar(self, vector):
    """Retorna la suma del vector actual con el parámetro <vector>
    Lanza una excepción de tipo TypeError en caso de que <vector> no sea de 
    tipo Vector.
    Lanza una excepción de tipo ValueError en caso de que <vector> no tenga
    las mismas dimensiones del vector actual.
    """
    pass

  def prod_punto(self, vector):
    """Retorna el producto punto del vector actual con el parámetro <vector>
    Lanza una excepción de tipo TypeError en caso de que <vector> no sea de 
    tipo Vector.
    Lanza una excepción de tipo ValueError en caso de que <vector> no tenga
    las mismas dimensiones del vector actual.
    """
    pass

  def size(self):
    """Retorna el número de elementos en el vector"""
    pass


## Ejemplo de uso ##

v1 = Vector([4,5,6])
v2 = Vector([1,2,3])

# v3 = v1.sumar(v2)
# print(v3.elementos)  # Debería de imprimir [5,7,9]
# v3 = v2.sumar(v1)
# print(v3.elementos)  # Debería de imprimir [5,7,9]
# r4 = v1.prod_punto(v2)
# print(r4)            # Debería imprimir 32

