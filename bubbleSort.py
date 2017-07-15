#Simple Bubble Sort
#15.07.17
#g7tro4w
import random

class BubbleSort:
    arraySize = 0
    array = []
    
    def __init__(self, sizeOfArray, intervalFrom, intervalTo):
        self.arraySize = sizeOfArray
        i = 0
        random.seed()
        while i < self.arraySize:
            self.array.insert(i, random.randint(intervalFrom, intervalTo))
            i= i + 1
            
    def __del__(self):
        self.array.clear()
        
    def printArray(self):
        print(self.array)

    def sort(self):
        isSorted = 0
        while not(isSorted):
            isSorted = 1
            i = 0
            while(i < self.arraySize-1):
                if(self.array[i+1]<self.array[i]):
                    self.array[i+1] = self.array[i] + self.array[i+1]
                    self.array[i] = self.array[i+1] - self.array[i]
                    self.array[i+1] = self.array[i+1] - self.array[i]
                    isSorted = 0
                i = i + 1

def main():
    while 1:
        n = int(input('Enter size of array:\n'))
        a = int(input('Enter primary position for random:\n'))
        b = int(input('Enter final position for random:\n'))
        sort = BubbleSort(n, a, b)
        sort.printArray()
        sort.sort()
        sort.printArray()
        del sort
main()
