import numpy as np 
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    dim1 = len(a[0])
    dim2 = len(b[0])

    if dim1 != dim2:
        return -1

    c = np.dot(a, b)
	return c