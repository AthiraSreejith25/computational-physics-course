import numpy as np
a = [[1,2,3],[2,1,4],[1,4,3]]
b = [[2,1],[1,2],[2,1]]

def matrix_product(x,y):
	if len(x[0]) != len(y):
		return("The matrices cannot be multiplied")
	else:
		c = np.zeros([len(x), len(y[0])])
		for i in range(len(x)):
			for j in range(len(y[0])):
				value = 0
				for k in range(len(y)):
					value += x[i][k] * y[k][j] 
				c[i][j] = value 
		return(c)
print("The product of matrices, AB = \n", matrix_product(a,b))

