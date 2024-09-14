
# Comparacion =>  Van a retornar un Booleano (True o False)
#  ==   !=    <    >    >= <=

numero1 =  10
numero2 = 20

#      10    == 20   False
# print(numero1 == numero2)

# # RETO => MOSTRAR EN TERMINAL
# # El resultado de usar los operadores de comparacion
# print(numero1 != numero2)  # True
# print(numero1 < numero2) # 10 < 20 => True
# print(numero1 > numero2) # 10 > 20 => False
# print(numero1 <= numero2) # 10 < 20 => True
# print(numero1 >= numero2) # 10 > 20 => False

# Logicos
# not  - and - or   =>  JS  &&  || 
print(not numero1 >= numero2)
#       10    >   20    and  10 !=   20
#            False     and   True
#                   False o True
print(numero1 > numero2  and numero1 != numero2)