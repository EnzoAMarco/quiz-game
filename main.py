from time import perf_counter
import random


def obtener_datos():
  nick1 = input("Ingrese su nick (3 a 12 caracteres): ")

  while len(nick1) < 3 or len(nick1) > 12:
    nick1 = input("ERROR, Ingrese un nick en el rango de caracteres (3 a 12 caracteres): ")

  dificultad1 = input("Ingrese la dificultad (f = facil, m = medio, d = dificil): ").lower()

  while dificultad1 != "f" and dificultad1!= "m" and  dificultad1!= "d":
    dificultad1 = input("ERROR, seleccione una dificultad valida (f = facil, m = medio, d = dificl): ").lower()

  return {"nick":nick1, "dificultad":dificultad1}

def obtener_preguntas(dificultad):

  try:
    preg = open(r'preguntas.txt','rt', encoding='UTF-8')

    if dificultad == 'f':
      n_dificultas = 1

    elif dificultad == 'm':
      n_dificultas = 2

    elif dificultad == 'd':
      n_dificultas = 3

    conjunto_preg = set()


    while len(conjunto_preg) < n_dificultas:
      preg.seek(0)
      num_preg = random.randint(1, 540)

      for num_txt, linea in enumerate(preg):

        if int(num_txt) == num_preg:
          linea = linea.rstrip('\n')
          conjunto_preg.add(linea)

    return conjunto_preg

  except FileNotFoundError as md:
    print(md)

  except OSError as mensaje:
      print('No se pudo grabar el archivo:', mensaje)

  finally:
      try:
          preg.close()

      except NameError:
          pass
      
def actividad_juego(preguntasLista):

  data_puntuacion = {'correctas': 0, 'tiempo': 0}
  contador_inicio = perf_counter() 

  for i in preguntasLista:
    registro_spliteado = i.split(';')
    print(registro_spliteado[0], *enumerate(registro_spliteado[1:-1],1), sep='\n')

    respuesta = input("Respuesta: ")

    if respuesta.isdigit() == True:
      aux = int(respuesta) 
    else: aux = 0

    while aux < 1 or aux > len(registro_spliteado)-2 or respuesta.isdigit()==False:
      respuesta = input("La respuesta ingresada no es válida, por favor elija una de las opciones disponibles.\nRespuesta: ")
      if respuesta.isdigit() == True:
        aux= int(respuesta) 
      else: aux = 0

    if respuesta == registro_spliteado[-1]:
      print('✔️  Respuesta correcta ✔️')
      data_puntuacion['correctas'] += 1
    else:
      print('❌ Respuesta incorrecta❌ La respuesta correcta era la número', registro_spliteado[-1], '-',registro_spliteado[int(registro_spliteado[-1])])
      
    print('----------------------------------------------------------------')
      
    
  contador_fin = perf_counter()
  data_puntuacion['tiempo'] = round(contador_fin-contador_inicio)

  print('Tiempo tardado', round(contador_fin-contador_inicio), 'segundos')
  
  return data_puntuacion

def resultado_turno(dic1, dic2):
  
  print(f"Feliciades {dic1['nick']}, jugando en la dificultad {dic1['dificultad']}, has obtenido {dic2['correctas']}pts en {dic2['tiempo']} segundos")
  return dic1|dic2

def resultado_sesion(datos):

  print('nick'.ljust(13), 'dificultad'.ljust(13), 'correctas'.ljust(13), 'tiempo')
  print('\n'.join([' '.join(z.ljust(13) for z in map(str, fila.values())) for fila in sorted(datos , key=lambda x: x['correctas'], reverse=True)]))

def guardar_resultados(lista, direA1):

  try:
    a1 = open(direA1,'at')

    for i in [[z for z in map(str, fila.values())] for fila in lista]:
      a1.write(';'.join(i) + '\n')
    
  except FileNotFoundError as md:
    print(md)

  except OSError as md:
    print('error so', md)
      
  finally:   
    try:
      a1.close()

    except NameError as md:
      print(md)
      pass

def jugar():

  participante_actual = obtener_datos()
  participantes_sesion.append(resultado_turno(participante_actual, actividad_juego(obtener_preguntas(participante_actual['dificultad']))))

  print('----------------------------------------------------------------')
  seguir_jugando=input('Quieres seguir jugando?(s = Si / n = No): ').lower()
  print('----------------------------------------------------------------')

  while seguir_jugando != "s" and seguir_jugando != "n" :
    seguir_jugando=input('Por favor elija una opcion válida, quieres seguir jugando?(s = Si / n = No): ').lower()
    print('----------------------------------------------------------------')

  if seguir_jugando == "s":
    jugar()
  else:
    print('Resultados de la sesión:', sep='\n')

# ------------------------PROGRAMA PRINCIPAL----------------------------------

print('----------------------------------------------------------------')
print('Bienvenido a The quiz game'.center(64))
print('----------------------------------------------------------------')

participantes_sesion = []

jugar()

print(participantes_sesion)
resultado_sesion(participantes_sesion)
guardar_resultados(participantes_sesion, 'historico.txt')
