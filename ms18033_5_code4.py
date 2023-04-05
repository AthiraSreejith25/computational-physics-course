import numpy as np

a = [[2,1,4], [8,-3,2], [4,11,-1]] #coefficient matrix

#function for back substitution
def back_substitution(m):
	sol = np.zeros(len(m))
	sol[0] = m[-1][-1]/m[-1][-2]
	for i in range(1,len(sol)):
		for k in range(i):
			sol[i] += - sol[k]*m[len(m)-i-1][len(m)-k-1]
		sol[i] = (sol[i] + m[len(m)-i-1][-1])/m[len(m)-i-1][len(m)-i-1]
	return(sol[::-1])

"""
def forward_substitution(m):
	sol = np.zeros(len(m))
	sol [0] = m[0][0]/m[0][-2]
	for i in range(1,len(sol)):
		for k in range(i):
			sol[i] = -sol[k]*m[i][k]
		sol[i] += m[i][-1]/m[i][i]

"""

l = np.zeros((len(a),len(a)))
u = np.zeros((len(a),len(a)))

#creating L matrix
for i in range(len(a)):
	l[i][0] = a[i][0]/u[0][0]
	for j in range(1,len(a)):
		l[i][j] = a[i][j] - 
