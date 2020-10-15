from generators.generators import Generator
from algorithms.heapSort import heapSort
from visualization.visualize import Visualizer
import time


def runHeapSort(arr):
    '''
    function that runs and times heap sort
    arr -> list of integers
    return -> time in seconds^(-5), num of operations
    '''
    startTime = time.perf_counter_ns()
    steps = heapSort(arr)
    endTime = time.perf_counter_ns()
    return (endTime - startTime) / 10000000.0, steps

def runSortedArrays(inputs):
    '''
    function that performs a run on Heap
    sort using sorted arrays as input
    inputs -> array of input sizes
    return -> info about the two algorithm runs (time and steps for each one)
    '''
    heapTimes = []         # cpu time for heap sort
    heapSteps = []         # num of operations for heap sort

    for inputSize in inputs:
        generator = Generator(inputSize)
        newArray = generator.generateSortedArray()
        heapTime, heapStep = runHeapSort(newArray)
        
        heapTimes.append(heapTime)
        heapSteps.append(heapStep)

    return heapTimes, heapSteps


def runReversedSortedArrays(inputs):
    '''
    function that performs a run on Heap sort
    using reversed sorted arrays as input
    inputs -> array of input sizes
    return -> info about the two algorithm runs (time and steps for each one)
    '''
    heapTimes = []         # cpu time for heap sort
    heapSteps = []         # num of operations for heap sort

    for inputSize in inputs:
        generator = Generator(inputSize)
        newArray = generator.generateReversedSortedArray()
        heapTime, heapStep = runHeapSort(newArray)
        
        heapTimes.append(heapTime)
        heapSteps.append(heapStep)

    return heapTimes, heapSteps


def runRandomPermutationArrays(inputs):
    '''
    function that performs a run on heap sort
    using random permutations as input
    inputs -> array of input sizes
    return -> info about the two algorithm runs (time and steps for each one)
    '''
    heapTimes = []         # cpu time for heap sort
    heapSteps = []         # num of operations for heap sort

    for inputSize in inputs:
        generator = Generator(inputSize)
        newArray = generator.generateRandomPermutation()
        heapTime, heapStep = runHeapSort(newArray)
        
        heapTimes.append(heapTime)
        heapSteps.append(heapStep)

    return heapTimes, heapSteps


def run50RandomInRangeArrays(inputs):
    '''
    function that generates n arrays of n random numbers (n is each entry in inputs)
    and returns info about the run in the form of average of the n runs
    inputs -> list of array sizes
    return -> average info about the algorithm runs (time and steps for each one)
    '''
    finalHeapTimes = []     # cpu time for Heap sort
    finalHeapSteps = []     # num of operations for Heap sort
    for inputSize in inputs:
        heapTimes = []
        heapSteps = []
        generator = Generator(inputSize)
        arrays = generator.generate50RandomInRange()
        for array in arrays:
            heapTime, heapStep = runHeapSort(array)
            heapTimes.append(heapTime)
            heapSteps.append(heapStep)
        
        # appending the average of the n runs in the final result array
        finalHeapTimes.append(sum(heapTimes)/len(heapTimes))
        finalHeapSteps.append(sum(heapSteps)/len(heapSteps))
    
    return finalHeapTimes, finalHeapSteps


if __name__ == '__main__':

    # input sizes given in the instructions
    inputs = [100, 200, 300, 400, 500, 1000, 4000, 10000]
    print()

    visualizer = Visualizer(inputs)

    # running algorithms for the sorted array inputs
    heapTimes, heapSteps = runSortedArrays(inputs)
    print('- SORTED ARRAYS -')
    print()
    visualizer.printSingleRunValues(heapTimes, heapSteps)
    visualizer.plotCurves(inputs, heapTimes, 'SORTED ARRAYS')

    print('[STILL RUNNING] wait for the new output...')
    print()

    # running algorithms for the reversed sorted array inputs
    heapTimes, heapSteps = runReversedSortedArrays(inputs)
    print('- REVERSED SORTED ARRAYS -')
    print()
    visualizer.printSingleRunValues(heapTimes, heapSteps)
    visualizer.plotCurves(inputs, heapTimes, 'REVERSED SORTED ARRAYS')

    print('[STILL RUNNING] wait for the new output...')
    print()

    # running algorithms for the random permutation array inputs
    heapTimes, heapSteps = runReversedSortedArrays(inputs)
    print('- RANDOM PERMUTATION ARRAYS -')
    print()
    visualizer.printSingleRunValues(heapTimes, heapSteps)
    visualizer.plotCurves(inputs, heapTimes, 'RANDOM PERMUTATION ARRAYS')

    print('[STILL RUNNING] wait for the new output...')
    print()

    # running algorithms for the random permutation array inputs
    heapTimes, heapSteps = run50RandomInRangeArrays(inputs)
    print('- 50 RANDOM ARRAYS EACH RUN -')
    print()
    visualizer.printSingleRunValues(heapTimes, heapSteps)
    visualizer.plotCurves(inputs, heapTimes, '50 RANDOM ARRAYS EACH RUN')