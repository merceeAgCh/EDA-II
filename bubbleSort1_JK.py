def bubbleSort(A): '''se define la funcion que lleva un arreglo (A) '''
#el ciclo for es una repeticion de n veces, en este caso de 1-7
    #para i en el rango "range", con una longitud "len"de 1 hasta 7
    for i in range(1, len(A)+1): 
    #para j en el rango de la lingitud de mi arreglo "A" se le resta 1 (n-1)
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j]= A[j+1]
                A[j+1] = temp 


def bubbleSort2(A):
    bandera = True
    pasada = 0
    while pasada < len(A) - 1 and bandera:
        bandera = False
        for j in range(len(A) - 1 - pasada):
            if (A[j] > A[j + 1]):
                bandera = True
                temp = A[j]
                A[j] = A[j + 1]
    
A = [6, 12, 10, 9, 8, 15, 24, 1]
bubbleSort(A)
for i in range(len(A)):
    print(A[i])
pasada = A[1]
for j in range(len(A)-1-pasada):
    print("Las pasadas son: ",pasada)
