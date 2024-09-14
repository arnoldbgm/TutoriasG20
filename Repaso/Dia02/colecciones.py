# Las colecciones de datos son variables que pueden guardar varios valores.

# Listas (List) (arreglos)
frutas = ['manzana','platano', "papaya", "granadilla", 'platano']
# Es de tipo MUTABLE => (Modificarla)
# Las listas poseen un indice

# A continuacion devolveremos platano
# print(frutas[1])

# Para agregar valores debemos usar =>  append
# frutas.append("uva")
# print(frutas)

# Para eliminar un valor de la lista segun su indice usamos lo que es  => pop
# IMPORTANTE => EL pop retorna el indice del valor que eliminaste
# frutas.pop(2) #Se elimina el ultimo elemento de la lista
# print(frutas)
# ['manzana','platano', "papaya", "granadilla"]

# Una eliminacion directa  => remove
# frutas.remove('MaNZaNa')
# print(frutas)
# ORIGINAL ['manzana','platano', "papaya", "granadilla", 'platano']

# # Modificar un valor 
# frutas[0] = 'granadilla'

# frutas[2] = 'granadilla'

# Mostrar la cantidad de elementos que posee una lista
# Usamos  =>   len()
# print(len(frutas))
# Me dice tambien la longitud de un texto, lista, tupla y set

# RETO 03
# De la siguiente Lista
marcas = ["LG", "SAMSUNG", "APPLE", "NOKIA", "SONY"]
# Que inserten un elemento a la lista "TOSHIBA"
# Eliminen el elemento de posicion 2
# Elimien "APPLE"
# Que modifiquen NOKIA  =>   "XIAOMI"
# Que me retornen la longitud de la lista
