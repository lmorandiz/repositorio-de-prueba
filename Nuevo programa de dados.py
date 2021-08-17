import random
Dado_1=random.randint(1,6)
Dado_2=random.randint(1,6)
print("Tirada dado 1:")
print(Dado_1)
print("tirada dado 2:")
print(Dado_2)
print("Total tirada:")
print(Dado_1+Dado_2)
Nuevojuego=True
while Nuevojuego==True:
   print("¿Desea tirar otra vez? Presione Sí y luego enter")
   print("En caso contrario ingrese la palabra no  y de enter:")
   Respuesta=input(str(" "))
   if Respuesta=="si":
      Nuevojuego=True
      Dado_1=random.randint(1,6)
      Dado_2=random.randint(1,6)
      print("Tirada dado 1:")
      print(Dado_1)
      print("tirada dado 2:")
      print(Dado_2)
      print("Total tirada:")
      print(Dado_1+Dado_2)
   if Respuesta=="no":
      Nuevojuego=False
      break