import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np

class Visualizer:

    def __init__(self, inputs):
        self.inputs = inputs

    def printSingleRunValues(self, heapTimes, heapSteps):
        '''
        function that prints information about each run of the two algorithms
        heapTimes -> list of CPU times for insertion sort
        heapSteps -> list of operations during insertion sort
        mergeTimes -> list of CPU times for merge sort
        '''
        for i in range(len(self.inputs)):
            print('Input Size: ', self.inputs[i])
            print('Insertion CPU Time: ', heapTimes[i], 'x 10^(-2) seconds')
            print('Insertion Steps: ', heapSteps[i])
            print('C constant: ', float(heapSteps[i]) / (self.inputs[i] ** 2.0))
            print()

    
    def plotCurves(self, x, y, title):

        x = [x*100 for x in range(1, len(x) + 1)]

        _, ax = plt.subplots(1)

        ax.plot(x, y, 'r', label='Heap Curve')

        plt.xlabel('Number of Operations')
        plt.ylabel('CPU Time')

        ax.set_title('Heap Sort')

        ax.legend()

        plt.legend()
        plt.tight_layout()
        plt.show()
