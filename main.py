#Añadir colores
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
RESET = '\033[39m'

#Ciclo de Juego
iniciar_trivia_gol= True  
intentos = 0

#Mensaje de bienvenida
print ("¡Hola! Te doy la bienvenida a resolver una trivia sobre ...")

print()
print(GREEN+"¡Fútbol!"+RESET)
print()

print ("Veremos si conoces algunos datos curiosos sobre futbol.")
print()

#Suerte aleatoria
import random

#Temporalidad
import time
time.sleep(2)

nombre = input(YELLOW+"¿Como te llaman?: "+RESET)

print("\n Hola", nombre,". A continuación, nos gustaria que respondieras las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta.\n")
time.sleep(2)

print(BLUE+"¡Y arranca el juego!"+RESET)


for cuenta_regresiva in range(3, 0, -1):
  print(cuenta_regresiva)
  time.sleep(1)

while iniciar_trivia_gol == True:
  intentos += 1
  puntaje = 0
  
  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")
  
  time.sleep(2)

  print()
  print (YELLOW+"N°1) ¿Qué futbolista peruano logro jugar en el Barcelona FC de España?"+RESET)
  print()
  print ("a) Teofilo Cubillaz")
  print ("b) Hugo Sotil")
  print ("c) Héctor Chumpitaz")
  print ("d) Claudio Pizarro")
  
  respuesta_1 = input("\nTu respuesta: ")
  print()

  #Ciclos y respuesta secreta
  while respuesta_1 not in ("a", "b", "c", "d", "e"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_1 == "e": #Respuesta secreta
    print (YELLOW+"¡Tarjeta Amarilla! No quieras hacer enfadar al arbitro, debemos concentrarnos en el juego."+RESET)
    
  elif respuesta_1 == "a":
    print (RED+"No ha sido gol porque se ha ido   fuera!"+RESET, "Hugo Sotil, ha sido el único futbolista peruano que de la segunda división local dio un salto gigantesco hasta el Barcelona de España. ")

  elif respuesta_1 == "c":
    print (RED+"No ha sido gol porque se ha ido fuera!"+RESET, "Hugo Sotil, ha sido el único futbolista peruano que de la segunda división local dio un salto gigantesco hasta el Barcelona de España. ")

  elif respuesta_1 == "d":
    print (RED+"No ha sido gol porque se ha ido fuera!"+RESET, "Hugo Sotil, ha sido el único futbolista peruano que de la segunda división local dio un salto gigantesco hasta el Barcelona de España. ")

  else:
    puntaje += 1
    print (GREEN+"Gooool! "+RESET, nombre, GREEN+"acaba de tirar un gol de media cancha!"+RESET)
    print("Hugo Sotil, ha sido el único futbolista peruano que de la segunda división local dio un salto gigantesco hasta el Barcelona de España.")
  time.sleep(3)

  print()
  print(BLUE+"Ya que hablamos de logros."+RESET)
  print()
  time.sleep(2)

  print (YELLOW+"N°2) ¿Cual es la selección con mas títulos de la copa del mundo?"+RESET)
  print ("a) Alemania")
  print ("b) Francia")
  print ("c) Argentina")
  print ("d) Brazil")
  print()

  respuesta_2 = input("\nTu respuesta: ")

  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  if respuesta_2 == "a":
    print (RED+"No está fino hoy. Está decidiendo mal."+RESET, "Brazil es la seleccion con cinco trofeos en la copa del mundo 1958, 1962, 1970, 1994 y 2002.")

  elif respuesta_2 == "b":
    print (RED+"No está fino hoy. Está decidiendo mal."+RESET, "Brazil es la seleccion con cinco trofeos en la copa del mundo 1958, 1962, 1970, 1994 y 2002.")

  elif respuesta_2 == "c":
    print (RED+"No está fino hoy. Está decidiendo mal."+RESET, "Brazil es la seleccion con cinco trofeos en la copa del mundo 1958, 1962, 1970, 1994 y 2002. ")

  else:
    puntaje += 1
    print (GREEN+"Le pega al arco y es ... Goool! "+RESET, nombre, GREEN+"para emocionar a la hinchada"+RESET)
    print("Brazil es la seleccion con cinco trofeos en la copa del mundo 1958, 1962, 1970, 1994 y 2002.")
  time.sleep(5)

  print()
  print(BLUE+"Si hablamos sobre el mundial, todos quieren participar en uno ¿no? "+RESET)
  print()
  time.sleep(2)

  print (YELLOW+"N°3) ¿Sabes cuál es la selección de sudamérica que nunca participó en un mundial?"+RESET)
  print ("a) Guatemala")
  print ("b) Venezuela")
  print ("c) Bolivia")
  print ("d) Perú")
  print()

  respuesta_3 = input("\nTu respuesta: ")
  print()
  
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_3 == "a":
    print (RED+"Gol fallado es gol en contra"+RESET, "Venezuela no fue capaz de lograr aun un pase al mundial.")
  
  elif respuesta_3 == "c":
    print (RED+"Gol fallado es gol en contra"+RESET, "Venezuela no fue capaz de lograr aun un pase al mundial.")
  
  elif respuesta_3 == "d":
    print (RED+"Gol fallado es gol en contra"+RESET, "Venezuela no fue capaz de lograr aun un pase al mundial.")
  
  else:
    puntaje += 1
    print (GREEN+"Y lo define"+RESET, nombre, GREEN+"lo gana, para romper la ventana del mundo, Gol Coca Cola!"+RESET)
    print("Venezuela no fue capaz de lograr aun un pase al mundial.")
  time.sleep(5)
  
  print()
  print(BLUE+"Hay muchos equipos buenos, sin embargo ..."+RESET)
  print()
  
  print (YELLOW+"N°4) ¿A cual de estos equipos lo consideran el mejor del siglo XXI ?"+RESET)
  print ("a) Barcelona")
  print ("b) Arsenal")
  print ("c) Real Madrid")
  print ("d) PSG")
  
  respuesta_4 = input("\nTu respuesta: ")
  while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_4 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_4 == "a":
    print (RED+"¡Final, final, no va más!"+RESET, "Real Madrid acaba de llevarse el premio como el mejor club en lo que va del siglo XXI (2001-2020) en los Globe Soccer Awards.")
  
  elif respuesta_4 == "b":
    print (RED+"¡Final, final, no va más!"+RESET, "Real Madrid acaba de llevarse el premio como el mejor club en lo que va del siglo XXI (2001-2020) en los Globe Soccer Awards.")
  
  elif respuesta_4 == "d":
    print (RED+"¡Final, final, no va más!"+RESET, "Real Madrid acaba de llevarse el premio como el mejor club en lo que va del siglo XXI (2001-2020) en los Globe Soccer Awards.")
  
  else:
    puntaje += 1
    print (GREEN+"Gooool! "+RESET, nombre, GREEN+"Si"+RESET,nombre,GREEN+"consigue mantener esta ventaja de"+RESET, puntaje ,GREEN+"goles hasta el final, podría ganar la Liga"+RESET)
    print("Real Madrid acaba de llevarse el premio como el mejor club en lo que va del siglo XXI (2001-2020) en los Globe Soccer Awards.")
  time.sleep(5)
  print()



  if puntaje == 0:
    print (RED+"está dejando en ridículo al mundo del fútbol."+RESET, puntaje, "goles no es algo para celebrar")
  
  elif puntaje == 1:
    print (RED+"Está dejando en ridículo al mundo del fútbol."+RESET, puntaje, "goles no es algo para celebrar.")
  
  elif puntaje == 2:
    print (RED+"A"+RESET,nombre, RED+"le va muy mal el calor, le afecta mucho."+RESET)
  
  elif puntaje == 3:
    print (MAGENTA+"Es mejor irse al descanso ganando que perdiendo."+RESET)
  
  elif puntaje == 4:
    print (MAGENTA+"Eres uno de los mejores jugadores que hemos visto en esta temporada."+RESET)
  
  print()
  
  time.sleep(3)
  print ("Pero que veo, el clima no ayuda, el partido se cancelo por la lluvia", nombre, "por jugar la trivia, en este primer tiempo lograste", puntaje, "goles")

  print("\n¿Deseas ir por un segundo tiempo e intentar la trivia nuevamente?")
  repetir_trivia_gol = input("Ingresa 'si' para repetir, o cualquier tecla si crees que mereces un descanso: ").lower()
  
  if repetir_trivia_gol != "si":  
   print("\nDiste lo mejor", nombre, " es hora de ir a descansar y alistarse para el proximo partido. Que te vaya bien y ¡Buena suerte!")
   iniciar_trivia_gol = False