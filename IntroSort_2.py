import math

def introsort(arr):
    max_depth = 2 * math.ceil(math.log2(len(arr)))
    introsort_helper(arr, 0, len(arr) - 1, max_depth)

def introsort_helper(arr, low, high, max_depth):
    if low < high:
        if max_depth == 0:
            heapsort(arr, low, high)
        else:
            if len(arr) > 16:
                pivot = partition(arr, low, high)
                print(arr)  # Imprime o estado atual da lista após a partição
                introsort_helper(arr, low, pivot - 1, max_depth - 1)
                introsort_helper(arr, pivot + 1, high, max_depth - 1)
            else:
                insertionsort(arr, low, high)
    else:
        print(arr)  # Imprime o estado atual da lista

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def heapsort(arr, low, high):
    build_heap(arr, low, high)

    for i in range(high, low, -1):
        arr[i], arr[low] = arr[low], arr[i]
        heapify(arr, low, i - 1)
        print("heapsort",arr)  # Imprime o estado atual da lista durante a etapa do Heapsort

def build_heap(arr, low, high):
    n = high - low + 1

    for i in range(low + n // 2, low - 1, -1):
        heapify(arr, low, high, i)

def heapify(arr, low, high, root):
    largest = root
    left_child = 2 * root - low + 1
    right_child = 2 * root - low + 2

    if left_child <= high and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child <= high and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, low, high, largest)

def insertionsort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1

        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print("\t",arr[i] ,">",arr[j+1],"\nInsertionSort",arr )  # Imprime o estado atual da lista durante o Insertion Sort
        print("-------------------------------------------")  # Imprime o estado atual da lista durante o Insertion Sort

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("\nPasso inicial:", arr)
introsort(arr)
print("Lista ordenada:", arr)