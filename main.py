from time import perf_counter
import random

# def paso1():
#   nick1=input("ingrese su nick: ")
#   dificultad1=input("ingrese la dificultad (f=facil, m=medio, d=dificl): ").lower()

#   while dificultad1 != "f" and dificultad1!= "m" and  dificultad1!= "d":
#     dificultad1 = input("ERROR SELECCIONE UNA DIFICULTAD VALIDA (f para facil, n normal, d dificl): ").lower()

#   return {"nick":nick1, "dificultad":dificultad1}
def paso1():
  nick1 = input("Ingrese su nick (3 a 12 caracteres): ")

  while len(nick1) < 3 or len(nick1) > 12:
    nick1 = input("ERROR, Ingrese un nick en el rango de caracteres (3 a 12 caracteres): ")

  dificultad1 = input("Ingrese la dificultad (f = facil, m = medio, d = dificl): ").lower()

  while dificultad1 != "f" and dificultad1!= "m" and  dificultad1!= "d":
    dificultad1 = input("ERROR, seleccione una dificultad valida (F= facil, M= medio, D= dificl): ").lower()

  return {"nick":nick1, "dificultad":dificultad1}

# def paso2(dificultad):

#   try:
#     preg=open(r'preguntas.txt','rt')

#     if dificultad=='f':
#       n_dificultas=1

#     if dificultad=='m':
#       n_dificultas=2

#     if dificultad=='d':
#       n_dificultas=3

#     conjunto_preg=set()

#     while len(conjunto_preg) < n_dificultas:
#       preg.seek(0)
#       num_preg=random.randint(1,40)

#       for num_txt, linea in enumerate(preg):

#         if int(num_txt)==num_preg:
#           linea = linea.rstrip('\n')
#           conjunto_preg.add(linea)

#     return conjunto_preg
  
#   except FileNotFoundError as md:
#     print(md)

#   except OSError as mensaje:
#       print('No se pudo grabar el archivo:', mensaje)

#   finally:
#       try:
#           preg.close()

#       except NameError:
#           pass
def paso2(dificultad):

  try:
    preg=open(r'preguntas.txt','rt', encoding='UTF-8')

    if dificultad == 'f':
      n_dificultas = 1

    elif dificultad == 'm':
      n_dificultas = 2

    elif dificultad == 'd':
      n_dificultas = 3

    conjunto_preg = set()

    while len(conjunto_preg) < n_dificultas:
      preg.seek(0)
      num_preg = random.randint(1,500)

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
      
# toma una lista de preguntas como parametro y devuelve un dic con correctas = nro de preguntas correactas y tiempo = segundos totales que tomo responder todo
def paso3(preguntasLista):

  data_puntuacion = {'correctas': 0, 'tiempo': 0}
  contador_inicio = perf_counter() 

  for i in preguntasLista:
    registro_spliteado = i.split(';')
    print(registro_spliteado[0], *enumerate(registro_spliteado[1:-1],1), sep='\n')

    respuesta = input("Respuesta: ")

    if respuesta.isdigit() == True:
      aux = int(respuesta) 
    else: aux=0

    while aux < 1 or aux > len(registro_spliteado)-2 or respuesta.isdigit()==False:
      respuesta = input("La respuesta ingresada no es válida , por favor elija una de las opciones disponibles.")
      if respuesta.isdigit() == True:
        aux= int(respuesta) 
      else: aux = 0

    if respuesta == registro_spliteado[-1]:
      print('Respuesta correcta')
      data_puntuacion['correctas'] += 1
    else:
      print('Respuesta incorrecta, la respuesta correcta era la nro', int(registro_spliteado[-1]), registro_spliteado[int(registro_spliteado[-1])])
      
    
  contador_fin = perf_counter()
  data_puntuacion['tiempo'] = round(contador_fin-contador_inicio)

  print('----------------------------------------------------------------')
  print('Tiempo tardado', round(contador_fin-contador_inicio), 'segundos')
  
  return data_puntuacion

def paso4(dic1,dic2):
  
  print(f"feliciades {dic1['nick']}, jugando en la dificultad {dic1['dificultad']}, has obtenido {dic2['correctas']}pts en {dic2['tiempo']} segundos")
  return dic1|dic2

def paso5(datos):

  print('nick'.ljust(13), 'dificultad'.ljust(13), 'correctas'.ljust(13), 'tiempo')
  print('\n'.join([' '.join(z.ljust(13) for z in map(str, fila.values())) for fila in sorted(datos , key=lambda x: x['correctas'], reverse=True)]))

def paso6(lista, direA1):

  # print([[z for z in map(str, fila.values())] for fila in lista])
  # for i in [[z for z in map(str, fila.values())] for fila in lista]:
  #   print(';'.join(i))
  
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

  participante_actual = paso1()
  participantes_sesion.append(paso4(participante_actual, paso3(paso2(participante_actual['dificultad']))))

  if input('quieres seguir jugando?(s/n): ') == "s":
    jugar()

  print('----------------------------------------------------------------', 'Resultados de la sesión:', sep='\n')
# ------------------------PROGRAMA PRINCIPAL----------------------------------

print('Bienvenido a te quiz game')
participantes_sesion = []

jugar()

# while True:

#   participante_actual = paso1()
#   participantes_sesion.append(paso4(participante_actual, paso3(paso2(participante_actual['dificultad']))))

#   if input('quieres seguir jugando?(s/n): ').lower() != 's':
#     print('----------------------------------------------------------------', 'Resultados de la sesión:', sep='\n')
#     break

# print([str(i)[1:-1] for i in participantes_sesion])
paso5(participantes_sesion)
paso6(participantes_sesion, 'historico.txt')

# paso5([
#   {'nick': 'uwu', 'dificultad': 'm','correctas': 0, 'tiempo': 10},
#   {'nick': 'owo', 'dificultad': 'f','correctas': 1, 'tiempo': 21},
#   {'nick': 'awa', 'dificultad': 'd','correctas': 3, 'tiempo': 13},
#   {'nick': 'iwi', 'dificultad': 'f','correctas': 1, 'tiempo': 5},
#   {'nick': 'ewe', 'dificultad': 'm','correctas': 2, 'tiempo': 30},
#        ])

# paso6([
#   {'nick': 'uwu', 'dificultad': 'm','correctas': 0, 'tiempo': 10},
#   {'nick': 'owo', 'dificultad': 'f','correctas': 1, 'tiempo': 21},
#   {'nick': 'awa', 'dificultad': 'd','correctas': 3, 'tiempo': 13},
#   {'nick': 'iwi', 'dificultad': 'f','correctas': 1, 'tiempo': 5},
#   {'nick': 'ewe', 'dificultad': 'm','correctas': 2, 'tiempo': 30},
#        ], 'historico.txt')