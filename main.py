from time import perf_counter

# 3

preguntas = [
            'Quien "sabia que no sabia nada"?;Aristoteles;Ortega y Gasset;Socrates;Platon;1',
            # 'Quien "sabia que no sabia nada"?;Aristoteles;Ortega y Gasset;Socrates;Platon;2',
            # 'Quien "sabia que no sabia nada"?;Aristoteles;Ortega y Gasset;Socrates;Platon;3',
            # 'Quien "sabia que no sabia nada"?;Aristoteles;Ortega y Gasset;Socrates;Platon;4',
             ]

def paso3(preguntasLista):

  t1_start = perf_counter() 

  for i in preguntasLista:
    registro_spliteado = i.split(';')
    print(registro_spliteado[0], *enumerate(registro_spliteado[1:-1],1), sep='\n')
    if input('Respuesta: ') == registro_spliteado[-1]:
      print('Respuesta correcta')
    else:
      print('Respuesta incorrecta, la respuesta correcta era la nro', int(registro_spliteado[-1]), registro_spliteado[int(registro_spliteado[-1])])
      
  t1_stop = perf_counter()

  print('----------------------------------------------------------------')
  print('Tiempo tardado', round(t1_stop-t1_start), 'segundos')
  
paso3(preguntas)