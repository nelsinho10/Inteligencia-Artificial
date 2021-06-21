Semana 4
===

### Operadores logicos

    - AND
    - OR
    - NOT


#### Los operadores logicos hacen cortocircuito
    
- **AND**: Si el primer elemento evaluado es `False` el segundo no se evalua

- **OR**: Si el primero elemento evaluado es `True` el segundo no se evalua

### Operadores de igualdad

- **Equivalencia**: Es ver si dos valores son equivalentes. 
    -   Operador `==` -> return Boolean
    -   Negacion `!=` 
- **Identidad**: Dos nombres estan hacindo referencia al mismo objeto, o si los identificadores son aliases uno del otro.
    -   Operador `is` -> return Boolean
    -   Negacion `is not` 


### Operadores de Comparacion
    `< <= >= >`
    - Se pueden utilizar en cadenas
    - Las minusculas estan antes de las mayusculas

### Operadores de Aritmeticos
    + - * /
    - Con una pleca / la division retorna un flotante
    - La division entera se hace con dos //
    - La elevacion a la poencia `2 ** 4`
    - El modulo es el resto de la division `%`

### Operadores de Secuencia
    - Acceder a los elementos `a[0]`
    - Acceder a los elementos de el final para adelante `a[-1]`
    - Obtener trozos de la secuencia `a[0:2]` el segundo elemento se le resta uno
    - Obtener secuencias las secuencias con saltos `a[0:5:3]`
    - Concatenar dos listas `a + b`, produce una nueva lista
    - Concatenar dos tuplas `a + b`
    - Con el `*` concatenamos elementos de una lista `a = [0] * 100`
    - Se pueden utilizar los operadores de pertenencia `2 in a`
    - Ver si un elemento no esta en la lista `3 not in a`
    - Con el operador `del a[1]`
    - Los str son secuencias por lo tanto aplican estos operadores

### Operadores de los set y los frozenset
    - Para ver si un elemento esta en el conjunto `'a' in b`

### Operadores de los diccionarios
    - Con las llaves se crea un diccinario vacio `a = {}`
    - Accediendo a la clave me retorna el valos `a['a']`
    - Se pueden agregar claves nuevas `a[''] = 'hola'`
    - con `del` podemos borrar claves

   
### Bloques de decision
    - Se realiza a travez del bloque if , seguido de otro bloque elif y por ultimo else si no se cumple niguna condicion
    - No existe el switch, pero se puede emular con un diccionario cuyos valores sean funciones y las condiciones serian las claves del diccionario
    - Todo lo que se mande como condicion se convierte en booleano mediante el uso del constructor de bool

### Bloques de repeticion
    - podemos recorrer los iterables de varias formas las listas, tuplas y los str
    - `for`
        `for e in lista`   
        `for i in range(len(lista))` -> el range genera un iterable que inicia en 0 hasta el numero que se le pase menos 1, tiene dos argumentos mas, el inicio  y el salto
    - `while`
        primero se declare una variable y despues se compara la condicion que se le pasa
    - `break` sirve para interrumpir el ciclo y no seguirlo ejecutando
    - `continue` sirve para saltarse a la siguiente iteracion

### Funciones en Python
    - En python existen funciones y metodos
    - Se utiliza la palaba reservada def
    - Si una funcion no tiene un `return` retorna None donde None es una referencia hacia ningun lado
**Parametros formales:** Son los identificadores que estan en el prototipo de la funcion.

**Parametros Actuales:** Son los parametros que se le envian a la funcion cuando se llama dicha funcion.

    - Implicitamente ocurre que los parametros formales se igualen a los actuales
    - Los parametros en python son mutables
    - 
**Parametros por defecto:** Son valores que se definen en el prototipo de la funcion, primero tienen que ir los parametros formales y luego los parametros por defecto.

**Parametro por palabra clave:** Sirve para el envio de palabra haciendo referencia al nombre que se le coloco en el prototipo de la funcion.

### Manejo de Excepciones
- Las excepciones son objetos
- Son objetos lanzados cuando se detecta una circunstancia exepcional, como por ejemplo el agotamiento de memoria
- Las excepciones pueden ser "capturadas" por un contexto que pueda manejarla de la forma adecuada.
- Si una excepcion no es capturada, entonces esta causara que el interprete termine la ejecucion del programa.

**Ejemplos de excepciones:**
![exepciones](/assets/excepciones.PNG)

- Las excepciones se lanzan con `raise nombreExcepcion('Mensaje')`

- Capturar las excepciones se realizan con
    - `try`
    - `except TipoExcepcion as e`

### Modulos de python
- Los modulos permiten agrupar definiciones y enunciados relacionados entre si
- los modulos se utilizan con las palabras reservadas `from` *nombre modulo* `import` *nombre de la definicion que se necesita*
- Para importar todo se utiliza `*`
- Solo se puede importar el modulo con `import nombre modulo`
- Para crear un modulo se guardan las definiciones en un archivo de extension .py
- Para ejecutar el codigo indicado solamente cuando el modulo se llame se utiliza el condicional:
    `if __name__ == '__main__':`