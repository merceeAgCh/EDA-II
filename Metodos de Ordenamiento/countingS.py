import sys

# argv: a list of integers that are >= 0 and less than a certain limit k.
def main(list_string, k):

    j = 0
    # list_string = list_string.rstrip('\r\n\t\b')
    input_array=[]
    # Parse String input 'list' to turn it into a list of integers.
    for i in list_string:
        if (i == ','):
            input_array.append(j)
            j = 0
            continue
        if (i == '['):
            continue
        if (i == ']'):
            input_array.append(j)
            continue
        j = j*10 + int(i)

    counting_array = []
    sorted_array = []
    i = 0
    # Create a list of size (k+1) with all 0's.
    while (i <= k):
        counting_array.append(0)
        i += 1
    # For each element from input list, update our counting_array.
    for element in input_array:
        counting_array[int(element)] += 1
    j = 0
    while (j <= k):
        l = 0
        num = counting_array[j]
        while (l < num):
            sorted_array.append(j)
            l+=1
        j+=1
    print(sorted_array)

if __name__ == "__main__":
    # argv: countingSort.py - a list of integers - an upper limit k
    if (len(sys.argv) != 3):
        print("Numero de argumentos no validos: Ingresa la entrada de la lista y un limite superior.")
        exit(1)
    main(sys.argv[1], int(sys.argv[2]))