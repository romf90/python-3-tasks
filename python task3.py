import numpy as np

def task3():
    arr1 = np.arange(16).reshape(2,8) + 1
    arr2 = np.arange(21).reshape(7,3) + 5    
    shape1 = arr1.shape
    shape2 = arr2.shape    
    size = lambda x1, x2 : x1 if (x1 > x2) else x2    
    bigX = size(shape1[0], shape2[0])
    bigY = size(shape1[1], shape2[1])    
    arrToAdd = np.zeros((bigX, bigY), dtype=int)   
    for row in range(shape1[0]):
        for column in range(shape1[1]):
            arrToAdd[row][column] += arr1[row][column]
    for row in range(shape2[0]):
        for column in range(shape2[1]):
            arrToAdd[row][column] += arr2[row][column]
    print(arrToAdd)

if __name__ == "__main__":
     task3()