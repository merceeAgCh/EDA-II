import time
import random

#Ejemplo del metodo de ordenamiento Radix Sort

def RadixSort(arr, d):           #tfuncion inicial nombrada como radix
    place = 1                    #primer digito
    for i in range(0, d):   
        CountingSort(arr, place)        #LLmamos el algoritmo de countingS
        place *= 10 

def CountingSort(arr, place):     
   output = [0] * len(arr)    
   count = [0] * 10     
   for i in range(0, len(arr)):  
       index = int((arr[i] / place)%10) 
       count[index] += 1    
   for i in range(1, 10):
        count[i] += count[i - 1]
   i = len(arr)-1 
   while i >= 0:
        index = int((arr[i] / place)%10) 
        output[count[index] - 1] = arr[i]   
        count[index] -= 1  
        i -= 1  
   for i in range(0, len(arr)):
        arr[i] = output[i]   

        #main
n = [10, 100]                             #tamanio del arreglo
d = int(input("Numero de digios:"))       #numnero
    
for i in n:
        #arr = [55, 75, 12, 23, 45, 23, 78, 34, 35, 11]
        arr = [random.randint(10**(d-1),10**d-1 ) for x in range(i)]   #our array that are filled by the random numbers
        start = time.perf_counter()  
        RadixSort(arr, d)
        end =  time.perf_counter()
        ResultTime = end - start 
        print ("Arreglo: ", arr)
        print("Tamanio:", i)
        print ("Tiempo:", end,"-", start,"=",ResultTime)   #Elapsed time during the whole program in seconds
        print ("RadixSort tiempo:", ResultTime, "\n")