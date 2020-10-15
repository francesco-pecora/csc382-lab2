import random

def heapify(arr, length, current): 
    steps = 3                   # three initializations
    largest = current
    left = 2 * current + 1
    right = 2 * current + 2
  
    # determine if children exist and are grater than root
    steps += 2
    if left < length and arr[current] < arr[left]:
        steps += 1
        largest = left
    steps += 2
    if right < length and arr[largest] < arr[right]:
        steps += 1
        largest = right
  
    # change root, if needed
    steps += 1
    if largest != current:
        steps += 1
        arr[current],arr[largest] = arr[largest],arr[current]
        # heapify the root.
        steps += heapify(arr, length, largest)
    return steps

def heapSort(arr):
    '''
    Sorting algorithm.
    '''
    steps = 1
    length = len(arr)

    # building a maxheap
    steps += (length // 2 - 1) * 2          # two operations each loop (counting inside heapify each time)
    for i in range(length // 2 - 1, -1, -1):
        current = i
        steps += heapify(arr, length, current)
    
    # extract the elements
    steps += (length - 1) * 2               # two operations each loop (counting inside heapify each time)
    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        steps += heapify(arr, i, 0)
    
    return steps


if __name__ == '__main__':
    n = 100
    a = [random.randint(1, n) for _ in range(1, n + 1)]
    # a = [x for x in range(0, n - 1)]
    heapSort(a)
    print(a)