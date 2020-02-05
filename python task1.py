import numpy as np

def task1():
    print ("Task 1:")
    a=np.array([[2,2],[1,1],[3,2]])
    b=np.array([[1,2,2],[2,1,2]])
    c=np.zeros((a.shape[0],b.shape[1]), dtype=int)
    size=c.shape
    for row in range(size[0]):
        for column in range(size[1]):
            for mul in range(a.shape[1]):
                c[row][column] += a[row][mul]*b[mul][column]
    print (c)


if __name__ == "__main__":
    task1()