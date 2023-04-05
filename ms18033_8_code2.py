import math
from prettytable import PrettyTable
from copy import deepcopy

x = []
sinx = []


for i in range(10,51,5):
    x.append(i/100)
    #sinx.append(round(math.sin(i/100),14))
    sinx.append(math.sin(i/100))

def table(f,a = []):
    if len(f) > 1:
        c = []
        for i in range(1,len(f)):
            #c.append(round((f[i] - f[i-1]),14))
            c.append(f[i] - f[i-1])
        a.append(c)
        #print(len(c))
        table(c,a)
    return(a)

tmp = table(sinx)

def forward_interpol(y,xi,del_f):
    #print(len(xi), len(del_f))
    h = xi[1] - xi[0]
    value = math.sin(xi[0])
    for i in range(1,len(xi)):
        a = del_f[i-1][0]/(math.factorial(i)*(h)**i)
        for j in range(i):
            a *= y - xi[j]
        value += a
    return(value)

print(forward_interpol(0.13,x,tmp))

def backward_interpol(y,xi,del_f):
    #print(len(xi), len(del_f))
    h = xi[1] - xi[0]
    value = math.sin(xi[0])
    for i in range(1,len(xi)):
        a = del_f[i-1][-1]/(math.factorial(i)*(h)**i)
        for j in range(i):
            a *= y - xi[len(xi) - j]
        value += a
    return(value)
print(forward_interpol(0.47,x,tmp))



def divided_diff_table(f,a = [], count = 0):
    if len(f) > 1:
        c = []
        for i in range(1,len(f)):
            c.append(round((f[i] - f[i-1])/(x[i+count] - x[i - 1]),5))
            #print(count)
        count += 1
            
        a.append(c)
        #print(len(c))
        divided_diff_table(c,a,count)
    return(a)

tmp =  divided_diff_table(sinx)


def divided_interpol(y,xi,del_f):
    #print(len(xi), len(del_f))
    h = xi[1] - xi[0]
    value = math.sin(xi[0])
    for i in range(1,len(xi)):
        a = del_f[i-1][0]
        
        for j in range(i):
            a *= y - xi[j]
        value += a
    return(value)
print(divided_interpol(0.47,x,tmp))






