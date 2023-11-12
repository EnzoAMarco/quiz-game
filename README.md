# quiz-game
--------------------------------------------------------------------------------------------------------------
# -obtener_datos(), Se ingresa el nick y la dificultad validandolos

# -obtener_preguntas(diccionario), Se selecciona un conjunto de preguntas en base a la dificultad y devuelve un conjunto, haciendo que no haya preguntas repetidas.

# -actividad_juego(lista/conjunto), Con el retorno de la funcion anterior se divide pregunta por pregunta del conjunto con un split, printeando en pantalla las preguntas y en cada una el usuario responde, imprime  
# correcto si acerto y suma un al contador de respuestas correctas, o incorrecta si no acertó y pone la respuesta correcta, al mismo tiempo se va a estar contando la cantidad de 
# tiempo que se tardó en responder las preguntas.

# -resultado_turno(diccionario, diccionario), Se imprimi en pantalla la puntuacion final al usuario, la dificultad jugada y el tiempo tardado.

# -resultado_sesion(lista de diccionarios), Al terminarse de ejecutar el programa y se informan todos los participantes de la sesion ordenados segun el puntaje obtenido

# -guardar_resultados(lista de diccionarios, path) Los participantes de la sesión se archivaran en un txt llamdo "historico.txt"

# -jugar(), Se pregunta si se quiere volver a jugar, validando que los input sean correctos.

# El formato del archivo historico.txt es nick;dificultad;puntuacion;tiempo(en segundos)