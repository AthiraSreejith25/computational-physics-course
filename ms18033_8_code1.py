import math
from prettytable import PrettyTable
from copy import deepcopy

x = []
sinx = []


for i in range(10,51,5):
    x.append(i/100)
    sinx.append(math.sin(i/100))

myTable = PrettyTable()
columns = ["x", "sin(x)"]
myTable.add_column(columns[0],x)
myTable.add_column(columns[1],[round(j,8) for j in sinx])
print("Table of x and sin(x): ")
print(myTable)
print('\n\n')

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
for i in tmp:
    for j in i:
        j = round(j,14)
#forward Difference
forward = deepcopy(tmp)

for i in range(len(forward)):
    for j in range(i+1):
        forward[i].append("")


myTable = PrettyTable()
columns = ["x", "sin(x)"]
myTable.add_column(columns[0],x)
myTable.add_column(columns[1],sinx)

for i in range(len(forward)):
    columns.append(i)
    myTable.add_column(columns[i+2],forward[i])

print("Forward Difference")
print(myTable)
print('\n\n')

    
#Backward difference    
backward = deepcopy(tmp)

for i in range(len(backward)):
    for j in range(i+1):
        
        backward[i] = [""] + backward[i]


myTable = PrettyTable()
columns = ["x", "sin(x)", "1", "2", "3", "4", "5", "6"]
myTable.add_column(columns[0],x)
myTable.add_column(columns[1],sinx)

for i in range(len(backward)):
    columns.append("")
    myTable.add_column(columns[i+2],backward[i])

print("Backward Difference")
print(myTable)
print('\n\n')




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

print(divided_diff_table(sinx))


        
#
fofo = [-14, -10.032, -5.296, -0.256, 6.672,14]
#print("Forward Table: ", forward(fofo))


        
        
