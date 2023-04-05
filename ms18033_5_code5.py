import numpy as np
a = [[0,2,1] , [4,1,-1] , [-2,3,-3]] #coefficient matrix
b = [5,-3,5]

#creating the augmented matrix
for i in range(len(b)):
	a[i].append(b[i])

#function for back substitution
def back_substitution(m):
	sol = np.zeros(len(m))
	sol[0] = m[-1][-1]/m[-1][-2]
	for i in range(1,len(sol)):
		for k in range(i):
			sol[i] += - sol[k]*m[len(m)-i-1][len(m)-k-1]
		sol[i] = (sol[i] + m[len(m)-i-1][-1])/m[len(m)-i-1][len(m)-i-1]
	return(sol[::-1])

#function for forward substitution
def forward_substitution(n):
    sol = np.zeros(len(n))
    sol[0] = n[0][-1]/n[0][0]
    for i in range(1,len(sol)):
        sol[i] = n[i][-1]
        for k in range(i):
            sol[i] += n[i][k]*x[k]
        sol[i]/m[i][i]
        return(sol)




            
    
