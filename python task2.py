import numpy as np

def task2():
    print ("Task 2:")
    arr1 = np.arange(16).reshape(2,8) + 1
    arr2 = np.arange(21).reshape(7,3) + 5
    shape1 = arr1.shape
    shape2 = arr2.shape
    size = lambda x1, x2 : x1 if (x1 < x2) else x2
    smallX = size(shape1[0], shape2[0])
    smallY = size(shape1[1], shape2[1])
    arrToAdd = np.zeros((smallX, smallY), dtype=int)
    finalSize = arrToAdd.shape
    for row in range(finalSize[0]):
        for columb in range(finalSize[1]):                                      
            arrToAdd[row][columb] = arr1[row][columb] + arr2[row][columb]
    print(arrToAdd)
    
if __name__ == "__main__":
     task2()
