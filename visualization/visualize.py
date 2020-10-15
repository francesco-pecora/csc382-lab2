import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np
import math

class Visualizer:

    def __init__(self, inputs):
        self.inputs = inputs

    def printSingleRunValues(self, heapTimes, heapSteps):
        '''
        function that prints information about each run of the algorithm
        heapTimes -> list of CPU times for heap sort
        heapSteps -> list of operations during heap sort
        '''
        for i in range(len(self.inputs)):
            print('Input Size: ', self.inputs[i])
            print('Heap CPU Time: ', heapTimes[i], 'x 10^(-2) seconds')
            print('Heap Steps: ', heapSteps[i])
            print('C constant: ', float(heapSteps[i]) / (self.inputs[i] * math.log2(self.inputs[i])))
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
