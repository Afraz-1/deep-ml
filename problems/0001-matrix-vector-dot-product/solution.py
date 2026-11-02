import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	dim1 = len(a[0])
	dim2 = len(b)
	if dim1 != dim2:
		return -1

	result = np.dot(a,b)
	return result
