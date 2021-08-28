
def bubblesort(numbers):

    for j in range(len(numbers) - 1, 0, -1):
        for i in range(j):
            if numbers[i] > numbers[i + 1]:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp


arr = [7, 19, 1, 2, 13, 5, 23, 29, 11, 17, 6]
print("El arreglo en desorden es:")
print(arr)
bubblesort(arr)
print("El arreglo ordenado mediante el método Bubble Sort: ")
print(arr)