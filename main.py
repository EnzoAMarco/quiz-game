from time import perf_counter

def nombre_dificultad():
  nick1=input("ingrese su nombre: ")
  dificultad1=input("ingrese la dificultad (f para facil, n normal, d dificl): ").lower()

  while dificultad1 != "f" and dificultad1!= "n" and  dificultad1!= "d":
    dificultad1=input("ERROR SELECCIONE UNA DIFICULTAD VALIDA (f para facil, n normal, d dificl): ").lower()

  datos_turno={"nick":nick1,"dificultad":dificultad1}
  return datos_turno

#print(nombre_dificultad()["nick"])
def paso_5(dic1,dic2):
  print(f"feliciades {dic2['nick']}, jugando en la dificultad {dic2['dificultad']}, has obtenido {dic1['correctas']}pts en {dic1['tiempo']}")
  return dic1|dic2

di1 = {'correctas': 3, 'tiempo': 10}
di2= {"nick":"Artenam","dificultad":"medio"}

preguntas = [
            'Quien "sabia que no sabia nada"?;Aristoteles;Ortega y Gasset;Socrates;Platon;1',
            'Quien "sabia que no sabia nada"?;Aristoteles;Ortega y Gasset;Socrates;Platon;2',
            # 'Quien "sabia que no sabia nada"?;Aristoteles;Ortega y Gasset;Socrates;Platon;3',
            # 'Quien "sabia que no sabia nada"?;Aristoteles;Ortega y Gasset;Socrates;Platon;4',
             ]
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

def paso7(datos):

  print('\n'.join([' '.join(map(str, fila)) for fila in sorted(datos , key=lambda x: x[2], reverse=True)]))

# paso7([['owo','m',3],['uwu','h',5],['awa','f',1]])

def paso8(lista, direA1):
    
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
