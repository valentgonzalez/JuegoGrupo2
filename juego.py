
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

inicio()
numero = int(input("Ingresa un número del 1 al 10: "))
rango = int(input("Ingresa un 0 si crees que tu número es menor que el aleatorio o un 1 si crees que es mayor: "))
num_random = random.randint(1, 10)
funcion_random(numero, num_random)
resultado(numero, num_random, rango)
