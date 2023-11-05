from time import perf_counter
import random

def paso1():
  nick1=input("ingrese su nombre: ")
  dificultad1=input("ingrese la dificultad (f para facil, m medio, d dificl): ").lower()

  while dificultad1 != "f" and dificultad1!= "m" and  dificultad1!= "d":
    dificultad1=input("ERROR SELECCIONE UNA DIFICULTAD VALIDA (f para facil, m medio, d dificl): ").lower()

  datos_turno={"nick":nick1,"dificultad":dificultad1}
  return datos_turno

def paso2(dificultad):

  try:
    preg=open(r'quiz-game\preguntas.txt','rt')

    linea=preg.readline()

    if dificultad=='f':
      n_dificultas=1

    if dificultad=='m':
      n_dificultas=2
      
    if dificultad=='d':
      n_dificultas=3
      
    conjunto_preg=set()

    while len(conjunto_preg)<n_dificultas:
      preg.seek(0)
      num_preg=random.randint(1,40)

      for num_txt,linea in enumerate(preg):

        if int(num_txt)==num_preg:
          linea=linea.rstrip('\n')
          conjunto_preg.add(linea)

    return conjunto_preg
  
  except OSError as mensaje:
      print('No se pudo grabar el archivo:', mensaje)

  finally:
      try:
          preg.close()
          
      except NameError:
          pass


# toma una lista de preguntas como parametro y devuelve un dic con correctas = nro de preguntas correactas y tiempo = segundos totales que tomo responder todo
def paso3(preguntasConjutos):

  data_puntuacion = {'correctas': 0, 'tiempo': 0}
  contador_inicio = perf_counter() 

  for i in preguntasConjutos:
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


  print('Tiempo tardado', round(contador_fin-contador_inicio), 'segundos')
  
  return data_puntuacion

# print(paso3(preguntas))

#def paso_4(dic1,dic2):
#  print(f"feliciades {dic2['nick']}, jugando en la dificultad {dic2['dificultad']}, has obtenido {dic1['correctas']}pts en {dic1['tiempo']}")
#  return dic1|dic2


def paso5(datos):

  print('\n'.join([' '.join(map(str, fila)) for fila in sorted(datos , key=lambda x: x[2], reverse=True)]))

# paso7([['owo','m',3],['uwu','h',5],['awa','f',1]])

def paso6(time,player,point):
    
  try:
    hist = open(r'quiz-game\historico.txt','at')
    hist.write(str(point)+';'+player+';'+str(time)+'\n')
    
  except FileNotFoundError as md:
    print(md)

  except OSError as md:
    print('error so', md)
      
  finally:   
    try:
      hist.close()

    except NameError as md:
      print(md)
      pass

def ordenar_por_burbujeo(l_nick,l_pts,l_time):

  #Ordena las 3 listas en paralelo

  for i in range(0,len(l_pts)-1):
    for j in range(i+1,len(l_pts)):
      
      if l_pts[j]>l_pts[i]:

        aux=l_pts[j]
        l_pts[j]=l_pts[i]
        l_pts[i]=aux

        aux1=l_time[j]
        l_time[j]=l_time[i]
        l_time[i]=aux1

        aux2=l_nick[j]
        l_nick[j]=l_nick[i]
        l_nick[i]=aux2

  return l_nick,l_pts,l_time


def printear_matriz(lista_nick,lista_pts,lista_time):

  #printea las listas del punto anterior ordenadas por mayor puntaje en una amtriz

  matriz=[]

  for f in range(len(lista_nick)+1):
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
          matriz[f][c]=lista_nick[0]
          lista_nick.remove(lista_nick[0])
        if c == 1:
          matriz[f][c]=str(lista_pts[0])+'pts'
          lista_pts.remove(lista_pts[0])
        if c == 2:
          matriz[f][c]=str(lista_time[0])+'s'
          lista_time.remove(lista_time[0])
      

  for f in range(len(matriz)):
    for c in range(len(matriz[0])):

      print('%8s' %matriz[f][c], end=' | ')
    print()



#PROGRAMA PRINCIPAL-------------------------

lnick=[]
lpts=[]
ltime=[]

#Este mamarracho es para volver a repetir el programa y se appeneand las cosas en sus listas

while True:

  p1=paso1()

  p2=paso2(p1['dificultad'])

  p3=paso3(p2)

  #p4=paso_4(paso1(),p3)

  p6=paso6(p3['tiempo'],p1['nick'],p3['correctas'])

  lnick.append(p1['nick'])
  lpts.append(p3['correctas'])
  ltime.append(p3['tiempo'])

  again=input('Quiere volver a jugar? (S/N)').upper()
  print()

  if again=='N':
    break

ln,lp,lt=ordenar_por_burbujeo(lnick,lpts,ltime)

p_ma=printear_matriz(ln,lp,lt)