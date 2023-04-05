import numpy as np
a = [[0,2,1] , [4,1,-1] , [-2,3,-3]] #coefficient matrix
b = [5,-3,5]

#creating the augmented matrix
for i in range(len(b)):
	a[i].append(b[i])

#function for back substitution
def solutions(m):
	sol = np.zeros(len(m))
	sol[0] = m[-1][-1]/m[-1][-2]
	for i in range(1,len(sol)):
		for k in range(i):
			sol[i] += - sol[k]*m[len(m)-i-1][len(m)-k-1]
		sol[i] = (sol[i] + m[len(m)-i-1][-1])/m[len(m)-i-1][len(m)-i-1]
	return(sol[::-1])



for k in range(len(a[0])-2): #iterating through columns of a

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
	for s in range(k+1,len(a)): #iterating through rows below k
		a1 = a[s][k]
		a2 = a[k][k]

		for t in range(len(a[0])): #iterating through colmuns of row s
			a[s][t] = a[s][t] - a[k][t]*a1/a2
			print(a)
print("The solution of [x1,x2,x3] is ", solutions(a))
