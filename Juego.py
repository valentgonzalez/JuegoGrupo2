

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
        


# In[ ]:





# In[ ]:



