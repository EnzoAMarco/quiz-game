import random

#contadores de cuantas preguntas tiene cada dificultad

'''El contadora de dificil lo saque porque no hacen falta
para sacar el dificil se le suma dos al contador de medio hasta el contador general
los demas ya estan definidos con sus propios contadores
contf+3,contf+contm
'''
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

  lista_preg=[]

  for i in range(5):
  
    preg.seek(0)

    if dificultad=='f':
      num_preg=random.randint(1,contf)

    elif dificultad=='m':
      num_preg=random.randint(1,7)

    elif dificultad=='d':
      num_preg=random.randint(contf+contm+1,contgeneral)


    for num_txt,linea in enumerate(preg):
    
      if int(num_txt)==num_preg:

        linea=linea.rstrip('\n')
        lista_preg.append(linea)

  print(lista_preg)

except OSError as mensaje:
    print('No se pudo grabar el archivo:', mensaje)

finally:
    try:
        preg.close()
        
    except NameError:
        pass