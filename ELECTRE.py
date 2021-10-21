
import numpy as np
import pandas as pd

matriz=[[1,5],[4,2],[3,3]]
pesos=[0.5,0.5]
#Electre

def  normalizar(matriz):
  normal=np.zeros((len(matriz),len(matriz[0])))
  max=np.nanmax(matriz, axis=0)
  min=np.nanmin(matriz, axis=0)
  rango=max-min
  for i in range(len(matriz)):
      for j in range(len(matriz[0])):
        normal[i][j]=(matriz[i][j]-min[j])/rango[j]
  return normal

def ponderar(matriz,pesos):
  pond=np.zeros((len(matriz),len(matriz[0])))
  for i in range(len(matriz)):
    
      for j in range(len(matriz[0])):
        pond[i][j]=matriz[i][j]*pesos[j]
  return pond

def concordancia(matriz,pesos):
   matrizC = np.zeros((len(matriz), len(matriz)))
   for i in range(len(matriz)):
    for j in range(len(matriz)):
      for k in range(len(matriz[i])):
        if i==j:
          matrizC[i][j]=np.nan
        else:
          if matriz[i][k]==matriz[j][k]:
            matrizC[i][j] = matrizC[i][j]+pesos[k]*0.5
          if matriz[i][k]>matriz[j][k]:
            matrizC[i][j] = matrizC[i][j]+pesos[k]
          else:
            continue
   return matrizC
    
def discordancia(matriz, pesos):
  matrizD = np.zeros((len(matriz), len(matriz)))
  for i in range(len(matriz)):
    for j in range(len(matriz)):
       diff = []
       diff2 = []
       for k in range(len(matriz[i])):
         if matriz[j][k]>matriz[i][k]:
           diff2.append(matriz[j][k]-matriz[i][k])
         diff.append(abs(matriz[j][k]-matriz[i][k]))
       if i==j:
          matrizD[i][j]=np.nan
       else:
        if len(diff2) == 0:
          matrizDiscor[i][j] = 0
        else:
          matrizD[i][j]=(max(diff2))/(max(diff))
  return matrizD 