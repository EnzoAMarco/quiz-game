import random

#contadores de cuantas preguntas tiene cada dificultad

'''El contadora de dificil lo saque porque no hacen falta
para sacar el dificil se le suma dos al contador de medio hasta el contador general
los demas ya estan definidos con sus propios contadores

'''

def cargar_preguntas():

  try:
    preg=open('preguntas.txt','rt')

    nick='robert'
    dificultad='m'

    linea=preg.readline()

    contf=-1
    contm=-1
    contgeneral=-3
    flagf=0
    flagm=-1

    while linea:
        linea=linea.rstrip('\n')
        contgeneral+=1

        if linea=='dificil':
          flagm=0

        elif linea=='medio' or flagm==1:
          flagf=0
          contm+=1
          flagm=1

        elif linea=='facil' or flagf==1:
          contf+=1
          flagf=1

        linea=preg.readline()

    cont_preg=0

    lista_repetidos=[]
    lista_preg=[]

    while cont_preg<5:
      preg.seek(0)
      cont_preg+=1

      if dificultad=='f':
        num_preg=random.randint(1,contf)

      elif dificultad=='m':
        num_preg=random.randint(contf+3,contf+contm)

      elif dificultad=='d':
        num_preg=random.randint(contf+contm+1,contgeneral)

      while num_preg in lista_repetidos:

        if dificultad=='f':
          num_preg=random.randint(1,contf)

        elif dificultad=='m':
          num_preg=random.randint(contf+3,contf+contm)

        elif dificultad=='d':
          num_preg=random.randint(contf+contm+1,contgeneral)

      lista_repetidos.append(num_preg)
      for num_txt,linea in enumerate(preg):

        if int(num_txt)==num_preg:
          linea=linea.rstrip('\n')
          lista_preg.append(linea)

  except OSError as mensaje:
      print('No se pudo grabar el archivo:', mensaje)

  finally:
      try:
          preg.close()
          
      except NameError:
          pass
      

def jugar(preg_por_difcultad,puntaje_actual):
  
  if preg_por_difcultad==0:

    return puntaje_actual
  
  pregunta_actual=cargar_preguntas()

  #es una lista, que devuelve una pregunta para hacer, hacer_pregunta(pregunta_actual)

  respuesta=int(input('Ingrese su respuesta: '))

  if verificar_respuesta():
    print('CORRECTO!')
    puntaje_actual+=1

  else:
    print(f'INCORRECTO, respuesta correcta ({})')

  juego(preg_por_difcultad-1,puntaje_actual)



