import random
import time

def CrearSubArreglo(A, indIzq, inDer):
    return A[indIzq:inDer+1]
def Merge(A,p,q,r):
    Izq = CrearSubArreglo(A,p,q)
    Der = CrearSubArreglo(A,q+1,r)
    i = 0
    j = 0
    for k in range(p,r+1):
        if (j >= len(Der)) or (i < len(Izq) and Izq[i] < Der[j]):
            A[k] = Izq[i]
            i = i + 1
        else :
            A[k] = Der[j]
            j = j + 1
def MergeSort(A,p,r):
    if r-p > 0:
        q = int ((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge(A,p,q,r)
comenzar = time.time()

A = [random.randint(0,2000)for i in range(2000)]
MergeSort(A, 0, 2000 - 1)
print("Mi arreglo")
print(A)
fin = time.time()
print(time.time())
MergeSort(A, 0, 2000 - 1)
print("Arreglo Ordenado")
for i in range(2000):
    print("%d" % A[i])
fin = time.time()
print(time.time())