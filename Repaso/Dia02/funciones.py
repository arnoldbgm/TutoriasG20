# function NOMBRE_FUNCION (PARAMETROS) { CODIGO }

# Para crear una funcion, debemos de usar la palabra def
# def elNombreDeLaFuncion():
def mostrarUno():
   print(1)

# Se llma a una funcion 
mostrarUno()

# Para llamar a una funcion se tiene que poner los parentesis, en caso de que no se coloque no se ejecutar
mostrarUno

# PARAMETROS
def calcular_promedio(parametro1:int, parametro2:int):
   resultado = ( parametro1 + parametro2 ) / 2
   # print(resultado)
   return resultado

mondonguito = calcular_promedio(15,18)  # 16.5

print(f"Este es el valor de mondonguito {mondonguito}")