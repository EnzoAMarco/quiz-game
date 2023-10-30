from time import perf_counter

# 3

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

print(paso3(preguntas))