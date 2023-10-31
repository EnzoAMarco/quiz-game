import random

from time import perf_counter

#contadores de cuantas preguntas tiene cada dificultad

'''El contadora de dificil lo saque porque no hacen falta
para sacar el dificil se le suma dos al contador de medio hasta el contador general
los demas ya estan definidos con sus propios contadores


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


'''

def ingresar_nombre_dificultad():
  nick1=input("ingrese su nombre: ")
  dificultad1=input("ingrese la dificultad (f facil, m medio, d dificl): ").lower()

  while dificultad1 != "f" and dificultad1!= "m" and  dificultad1!= "d":
    dificultad1=input("ERROR SELECCIONE UNA DIFICULTAD VALIDA (f facil, m medio, d dificl): ").lower()

  datos_turno={"nick":nick1,"dificultad":dificultad1}
  return datos_turno



def cargar_preguntas(dificultad):

  try:
    preg=open('preguntas.txt','rt')


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

    return lista_preg

  except OSError as mensaje:
      print('No se pudo grabar el archivo:', mensaje)

  finally:
      try:
          preg.close()
          
      except NameError:
          pass
      

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
    print('----------------------------------------------------------------')
  contador_fin = perf_counter()
  data_puntuacion['tiempo'] = round(contador_fin-contador_inicio)

  #print('Tiempo tardado', round(contador_fin-contador_inicio), 'segundos')
  
  return data_puntuacion


#-----------------------------PROGRAMA PRINCIPAL-----------------------------------


lnick=[]
lpts=[]
ltime=[]
ldif=[]

matriz=[]

while True:

  nick_dif=ingresar_nombre_dificultad()

  lpreg=cargar_preguntas(nick_dif['dificultad'])

  puntos=paso3(lpreg)

  if nick_dif['dificultad']=='m':
    pt=2*puntos['correctas']

  if nick_dif['dificultad']=='d':
    pt=3*puntos['correctas']

  if nick_dif['dificultad']=='f':
    pt=puntos['correctas']

  print(f'Obtuviste {pt} puntos en',puntos['tiempo'],'segundos')

  lnick.append(nick_dif['nick'])
  lpts.append(pt)
  ltime.append(puntos['tiempo'])
  ldif.append(nick_dif['dificultad'])

  print()
  a=input('Desea volver a jugar? (S/N): ')
  print()

  if a.upper()=='N':
    break

print(lnick)
print(lpts)
print(ltime)
print(ldif)

for f in range(len(lnick)+1):
  matriz.append([0]*3)

flag=0

for f in range(len(matriz)):

  for c in range(len(matriz[0])):

    if f==0 and flag==0:
      matriz[f][c]='Nick'
      matriz[f][c+1]='Puntos'
      matriz[f][c+2]='Tiempo'
      flag=1

    if f!=0:
      if c == 0:
        matriz[f][c]=lnick[0]
        lnick.remove(lnick[0])
      if c == 1:
        matriz[f][c]=str(lpts[0])+'pts'
        lpts.remove(lpts[0])
      if c == 2:
        matriz[f][c]=str(ltime[0])+'s'
        ltime.remove(ltime[0])
    

for f in range(len(matriz)):
  for c in range(len(matriz[0])):

    print('%8s' %matriz[f][c], end=' | ')
  print()





