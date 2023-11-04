import random
def nombre_dificultad():
  nick1=input("ingrese su nombre: ")
  dificultad1=input("ingrese la dificultad (f para facil, n normal, d dificl): ").lower()

  while dificultad1 != "f" and dificultad1!= "n" and  dificultad1!= "d":
    dificultad1=input("ERROR SELECCIONE UNA DIFICULTAD VALIDA (f para facil, n normal, d dificl): ").lower()

  datos_turno={"nick":nick1,"dificultad":dificultad1}
  return datos_turno

#print(nombre_dificultad()["nick"])
def paso_5(dic1,dic2):
  print(f"feliciades {dic2["nick"]}, jugando en la dificultad {dic2["dificultad"]}, has obtenido {dic1["correctas"]}pts en {dic1["tiempo"]}''")
#diccionario= [{"nick":dic2["nick"], "dificultad":dic2["dificultad"],"correctas":dic1["correctas"], "tiempo":dic1["tiempo"]},]
  return dic1|dic2

def no_repetir():
  preguntar=set()
  try:
    a1 = open(r"C:\Users\Usuario\Desktop\uade\Algoritmia\quiz-game\PREGUNTAS.txt",'rt')
    while len(preguntar)<5:
      question = a1.readline()
      preguntar.add(question)

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

    
  return preguntar


  

#preguntas=(1,2,3,3,2,2,2,4,4,5)
x=no_repetir()
print(x)