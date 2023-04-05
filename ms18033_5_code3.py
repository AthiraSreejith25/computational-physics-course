import numpy as np
a = [[2,4,1] , [3,2,-2] , [3,-3,3]] #coefficient matrix
b = [3,-2,18]

#creating the augmented matrix
for i in range(len(b)):
	a[i].append(b[i])

#function for substitution
def solutions(m):
	sol = np.zeros(len(m))

	for i in range(len(sol)):
		sol[i] = m[i][-1]/m[i][i]
	
	return(sol)


for k in range(len(a[0])-1): #iterating through columns of a

	#finding the row with maximum value for kth column
	maxi = a[k][k]
	row = k
	for r in range(k+1,len(a)):
		if maxi - a[r][k] < 0:
			maxi = a[r][k]
			row = r

	#swapping rows
	z = a[row]
	a[row] = a[k]
	a[k] = z


	#elimination
	for s in range(len(a)): #iterating through rows except k

		if s != k:

			a1 = a[s][k]
			a2 = a[k][k]

			for t in range(len(a[0])): #iterating through colmuns of row s
				a[s][t] = a[s][t] - a[k][t]*a1/a2


print("The solution of [x1,x2,x3] is ", solutions(a))


