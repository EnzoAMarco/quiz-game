    

uwu = [
        {'nick': 'ren3', 'dificultad': 'f', 'correctas': 1, 'tiempo': 2},
        {'nick': 'ren2', 'dificultad': 'f', 'correctas': 2, 'tiempo': 2},
        {'nick': 'ren1', 'dificultad': 'f', 'correctas': 3, 'tiempo': 2},

      ]

print('nick d p t')
print('\n'.join([' '.join(map(str, fila.values())) for fila in sorted(uwu , key=lambda x: x['correctas'], reverse=True)]))
