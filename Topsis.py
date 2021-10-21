import numpy as np
import pandas as pd


matriz=[[1,5],[4,2],[3,3]]
pesos=[0.5,0.5]

#TOPSIS
"Para p=+infinito,poner 3 en parámetro p"

def normas(matriz,p):
  if p==3:
    normas=np.nanmax(matriz, axis=0)
  else:
    normas=np.zeros(len(matriz[0]))
    suma=np.zeros(len(matriz[0]))
    for i in range(len(matriz)):
      for j in range(len(matriz[0])):
       suma[j]=suma[j]+matriz[i][j]**p
       normas[j]=suma[j]**(1/p)
  return normas 

def ponderar(matriz,pesos):
  pond=np.zeros((len(matriz),len(matriz[0])))
  for i in range(len(matriz)):
    
      for j in range(len(matriz[0])):
        pond[i][j]=matriz[i][j]*pesos[j]
  return pond

def distancia(matriz,ideal,p):
  distancias=np.zeros(len(matriz))
  resta=np.zeros((len(matriz),len(matriz[0])))
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        resta[i][j]=abs(ideal[j]-matriz[i][j])
  if p==3:
    distancias=np.nanmax(resta, axis=1) 
  else:
    suma=np.zeros(len(matriz))
    for i in range(len(resta)):
      for j in range(len(resta[0])):
        suma[i]=suma[i]+resta[i][j]**p
    for i in range(len(distancias)):
      distancias[i]=suma[i]**(1/p)
  return distancias

def TOPSIS(matriz,pesos,p):
  norma=normas(matriz,p)
  puntajes=np.zeros(len(matriz))
  normal=np.zeros((len(matriz),len(matriz[0])))
  completo=list(np.zeros((len(matriz),2)))
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      normal[i][j]=matriz[i][j]/norma[j]
  normalpond=ponderar(normal,pesos)
  ideal=np.nanmax(normalpond, axis=0)
  anti=np.nanmin(normalpond, axis=0)
  distanciaI=distancia(normalpond,ideal,p)
  distanciaA=distancia(normalpond,anti,p)
  for i in range(len(puntajes)):
    puntajes[i]=distanciaA[i]/(distanciaI[i]+ distanciaA[i])
  for i in range(len(puntajes)):
       completo[i]=['A'+str(i+1),puntajes[i]]
  Tabla=pd.DataFrame(completo).set_axis(['','Puntaje'],axis=1,)
  Tabla=Tabla.sort_values(by=['Puntaje'],ascending=False)
 
  return Tabla
  
TOPSIS(matriz,pesos,3)

