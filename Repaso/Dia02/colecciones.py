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



# SET 
# Es desordenada => no tiene indices o posiciones 
# Si es editable

# alumnos = {
#    'Cristhian',
#    'Jhonny',
#    'Jhossimar',
#    'Kevin',
#    'Miguel',
#    'Yhulisa',
#    'Yrvin',
#    'Yrvin'
# }

# Agregar un elemento a un set => add
# alumnos.add('Arnold')
# # Para eliminar usamos => remove
# alumnos.remove('Kevin')
# print(alumnos)
# alumnos.add('Kevin')

categorias = {
   'electrodomesticos',
   'maquillaje',
   'ropa'
}

# El  =>   in      me indica si esta o no esta un valor
# ropa == ropA
print('ropA' in  categorias)

# Tuplas
# Son ordenas
# NO SE PUEDEN EDITAR (ineditable)
meses = ('Enero', 'Febrero','Diciembre')
envio = ('Preparando', 'Enviado', 'Entregado')

# Diccionarios | JS => Object
# Son ordenados PEROOO no utilizan indices 
# Usamos las LLAVES (KEYS)

persona = {
   'nombre': 'Arnold',
   'apellido': 'Gallegos',
   'genero': 'Masculino',
   'hobbies': ['Comer', 'Programar', 'Fotografia'],
   'direccion': {
      'calle': 'Calle las paltas',
      'numero': 123
   },
   'estado_civil': 'Soltero'
}

#Si quisieramos acceder al hobbie
# print(f"El hobbie es {persona['hobbies'][1]}")

# # Para acceder a un diccionario dentro de otro
# print(f"La calle es {persona['direccion']['calle']}")

# Cuantos hobbies tienes
# print(f"La cantidad de hobbies es {len(persona['hobbies'])}")

# RETO 04
superheroes = {
   'nombre': 'Batman',
   'nombre_real': 'Bruce Wayne',
   'enemigos': ['Joker', 'Red Hat', 'Pinguin'],
   'habilidades':{
      'combate': ['karate', 'taekondo'],
      'investigacion':{
         'principal': 'Super detective'
      }
   }
}
# Quiero que me muestren el nombre de "Batman"
print(superheroes.get('nombre'))
print(superheroes['nombre'])
# Quiero que me retornen ->  Su nombre real es Bruce Wayne
print(f"Su nombre real es {superheroes['nombre_real']}")
# Quiero que me muestren el nombre de "Joker"
print(superheroes['enemigos'][0])
# Quiero que me retoren -> Tiene 3 enemigos
print(f"Tiene {len(superheroes['enemigos'])} enemigos")
# Quiero que me retornen -> Su habilidad es el karate
print(f"Su habilidad es el {superheroes['habilidades']['combate'][0]}")
# Quiero que me retornen -> El es un Super detective
print(f"El es un {superheroes['habilidades']['investigacion']['principal']}")