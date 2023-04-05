import math
import numpy as np

x = [1,2,3,4,5]
f = [30,15,32,18,25]
m = len(f)-1
h = x[1] - x[0]
a = np.zeros((m-1,m-1))

for i in range(len(a)):
    a[i][i] = 4
    if i-1 >=  0:
        a[i][i-1] = 1
    if i+1 < len(a):
        a[i][i+1] = 1

#print(a)

b = [((f[i+1] - 2*f[i] + f[i-1])*6/h) for i in range(1,m)]
#print(b)


m = np.linalg.solve(a,b)
#mi.append(0)
mi = m.tolist()
mi = [0] + mi
#print(mi)


x0 = 2.5
i = 1
for j in range(len(x)):
    if x0 <= x[j]:
        i = j - 1
        break
#print(i)

print((mi[i+1] - mi[i])*(x0 - x[i])**(3)/(6*h) + mi[i]*(x0 - x[i])**(2)/2 + ((f[i+1] - f[i])/h - h*(2*mi[i] +  mi[i+1])/6)*(x0 - x[i]) + f[i])

"""
di = f[i]
bi = mi[i]/2
ai = (mi[i+1] - mi[i])/(6*h)
ci = (f[i+1] - f[i])/h - (2*mi[i] + mi[i+1])*h/6
p = x0 - x[i]
print(ai, bi, ci, di)
print(ai*(p)**(3) + bi*(p)**(2) + ci*p + di)
"""
