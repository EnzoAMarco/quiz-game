from time import perf_counter
import random

def paso1():
  nick1=input("ingrese su nombre: ")
  dificultad1=input("ingrese la dificultad (f para facil, n normal, d dificl): ").lower()

  while dificultad1 != "f" and dificultad1!= "n" and  dificultad1!= "d":
    dificultad1=input("ERROR SELECCIONE UNA DIFICULTAD VALIDA (f para facil, n normal, d dificl): ").lower()

  datos_turno={"nick":nick1,"dificultad":dificultad1}
  return datos_turno

def paso2(dificultad):

  try:
    preg=open('preguntas.txt','rt')

    linea=preg.readline()

    cont_preg=0

    if dificultad=='f':
      n_dificultas=3

    lista_preg=[]

    while cont_preg<n_dificultas:
      preg.seek(0)
      cont_preg+=1

      num_preg=random.randint(1,500)

      lista_repetidos.append(num_preg)
      for num_txt,linea in enumerate(preg):

        if int(num_txt)==num_preg:
          linea=linea.rstrip('\n')
          lista_preg.append(linea)

    return lista_preg

  except OSError as mensaje:
      print('No se pudo grabar el archivo:', mensaje)

  finally:
      try:
          preg.close()
          
      except NameError:
          pass

preguntas = paso2()

# toma una lista de preguntas como parametro y devuelve un dic con correctas = nro de preguntas correactas y tiempo = segundos totales que tomo responder todo
def paso3(preguntasLista):

  data_puntuacion = {'correctas': 0, 'tiempo': 0}
  contador_inicio = perf_counter() 

  for i in preguntasLista:
    registro_spliteado = i.split(';')
    print(registro_spliteado[0], *enumerate(registro_spliteado[1:-1],1), sep='\n')

    if input('Respuesta: ') == registro_spliteado[-1]:
      print('Respuesta correcta')
      data_puntuacion['correctas'] += 1
    else:
      print('Respuesta incorrecta, la respuesta correcta era la nro', int(registro_spliteado[-1]), registro_spliteado[int(registro_spliteado[-1])])
      
  contador_fin = perf_counter()
  data_puntuacion['tiempo'] = round(contador_fin-contador_inicio)

  print('----------------------------------------------------------------')
  print('Tiempo tardado', round(contador_fin-contador_inicio), 'segundos')
  
  return data_puntuacion

# print(paso3(preguntas))

def paso_4(dic1,dic2):
  print(f"feliciades {dic2['nick']}, jugando en la dificultad {dic2['dificultad']}, has obtenido {dic1['correctas']}pts en {dic1['tiempo']}")
  return dic1|dic2

di1 = {'correctas': 3, 'tiempo': 10}
di2= {"nick":"Artenam","dificultad":"medio"}

def paso5(datos):

  print('\n'.join([' '.join(map(str, fila)) for fila in sorted(datos , key=lambda x: x[2], reverse=True)]))

# paso7([['owo','m',3],['uwu','h',5],['awa','f',1]])

def paso6(lista, direA1):
    
  try:
    a1 = open(direA1,'at')
    a1.writelines(lista)
    
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
