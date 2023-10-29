import random

#contadores de cuantas preguntas tiene cada dificultad

'''El contadora de medio y general los saque porque no hacen falta
para sacar el medio se le suma dos al contador de facil y se le resta dos al de dificil
los demas ya estan definidos con sus propios contadores
'''

'''
      if linea=='medio' or flagm==1:
        flagf=0
        contm+=1
        flagm=1
'''
#  contm=-2
#  contgeneral=-3
#  flagm=0
#  contgeneral+=1


try:
  preg=open('preguntas.txt','rt')

  nick='robert'
  dificultad='m'

  linea=preg.readline()



  contf=-2
  contd=-1

  flagf=0
  flagd=0


  while linea:
      linea=linea.rstrip('\n')


      if linea=='facil' or flagf==1:
        contf+=1
        flagf=1

      if linea=='medio':
        flagf=0

      elif linea=='dificil' or flagd==1:
        flagm=0
        contd+=1
        flagd=1

      linea=preg.readline()

  print(contf,contd)

except OSError as mensaje:
    print('No se pudo grabar el archivo:', mensaje)

finally:
    try:
        preg.close()
        
    except NameError:
        pass