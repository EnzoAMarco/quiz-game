def nombre_dificultad():
  nick1=input("ingrese su nombre: ")
  dificultad1=input("ingrese la dificultad (f para facil, n normal, d dificl): ").lower()

  while dificultad1 != "f" and dificultad1!= "n" and  dificultad1!= "d":
    dificultad1=input("ERROR SELECCIONE UNA DIFICULTAD VALIDA (f para facil, n normal, d dificl): ").lower()

  datos_turno={"nick":nick1,"dificultad":dificultad1}
  return datos_turno

#print(nombre_dificultad()["nick"])