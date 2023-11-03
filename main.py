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

di1 = {'correctas': 3, 'tiempo': 10}
di2= {"nick":"Artenam","dificultad":"medio"}

