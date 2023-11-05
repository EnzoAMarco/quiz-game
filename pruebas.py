lnick=[]
lpts=[]
ltime=[]

matriz=[]


  lnick.append(nick_dif['nick'])
  lpts.append(pt)
  ltime.append(puntos['tiempo'])

for f in range(len(lnick)+1):
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
        matriz[f][c]=lnick[0]
        lnick.remove(lnick[0])
      if c == 1:
        matriz[f][c]=str(lpts[0])+'pts'
        lpts.remove(lpts[0])
      if c == 2:
        matriz[f][c]=str(ltime[0])+'s'
        ltime.remove(ltime[0])
    

for f in range(len(matriz)):
  for c in range(len(matriz[0])):

    print('%8s' %matriz[f][c], end=' | ')
  print()