#Ejercicio 2
import numpy as np

#Ejercicio 3
#version = np.__version__
#configuracion = np.show_config()
#print(np.__version__)

#Ejercicio 4. Vector nulo de longitud 10
#print(np.zeros(10))

#Ejercicio 5
#zeros = np.zeros(10)
#memoria = zeros.size*zeros.itemsize
#print(memoria)

#Ejercicio 6
#numpy.info(numpy.add)

#Ejercicio 7
#vector = np.zeros(10)
#vector[4] = 1
#print(vector)

#Ejercicio 8
#print(np.arange(10,50))

#Ejercicio 9
#vector = np.arange(0,10)
#print(vector[::-1])

#Ejercicio 10
'''matriz = ([0,1,2],[3,4,5],[6,7,8])
matriz2 = np.reshape(matriz, (3,3))
print(matriz2)'''

#Ejercicio 11 Encontrar indices diferentes a cero
'''array = [1,2,0,0,4,0]
array2 = np.nonzero(array)
print(array2)'''

#Ejercicio 12 Matriz identidad
'''matriz = np.eye(3)
print(matriz)'''

#Ejercicio 13 
'''arr = np.random.random(3)
print(arr)'''

#Ejercicio 14 Mínimo y máximo
'''arr = np.random.random(10)
max = max(arr)
min = min(arr)
print(max)
print(min)'''

#Ejercicio 15 Media
'''arr = np.random.random(10)
media = np.mean(arr)
print(media)'''

#Ejercicio 16 
'''array = np.ones(25)
matriz = np.reshape(array, (5,5))
matriz[1:-1,1:-1]=0
print(matriz)'''

#Ejercicio 17
'''array = np.ones(25)
matriz = np.reshape(array, (5,5))
#print(matriz)
matriz2 = np.pad(matriz, (1,1),'constant',constant_values=(0,0))
print(matriz2)'''

#Ejercicio 18
'''print(0*np.nan)
print(np.nan==np.nan)
print(np.inf>np.nan)
print(np.nan-np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3*0.1)'''

#Ejercicio 19
'''array = [0,1,2,3,4,5,6,7,8]
matriz = np.reshape(array, (3,3))
print(np.diag(matriz))'''

#Ejercicio 20
vector = np.zeros(64)
matriz = np.reshape (vector, (8,8))

matriz[0::2,1::2]=1
matriz[1::2,::2]=1
print(matriz)