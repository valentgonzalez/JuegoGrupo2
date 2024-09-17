
import random

def inicio():
  print("El juego consiste en escoger un número entre 1 y 10, y luego adivinar si otro valor al azar será mayor o menor que el seleccionado")
  veri = True
  while veri == True:
      x = int(input("Ingresa un 1 si estas listo para jugar: "))
      if x != 1: 
        print("te volvemos a preguntar. Ingresa un 1 si estas listo para jugar: ")
      else:
        veri == False
        break
         

def resultado(n1, n2, n3):
  if (n3 == 0):
    if (n1 < n2):
      print("Ganaste")
    if (n1 > n2):
      print("Perdiste")
  if (n3 == 1):
    if (n1 > n2):
      print("Ganaste")
    if (n1 < n2):
      print ("Perdiste")

verificador = 0 
num_random = random.randint(1, 10)
inicio()

while verificador ==0:
    numero = int(input("Ingresa un número del 1 al 10: "))
    if numero < 11 and numero > 1 :
         rango = int(input("Ingresa un 0 si crees que tu número es menor que el aleatorio o un 1 si crees que es mayor: "))
         funcion_random(numero, num_random)
         resultado(numero, num_random, rango)
         verificador = 1 

