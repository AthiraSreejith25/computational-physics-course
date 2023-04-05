import numpy as np

a = [[-2,0,-1],[1,-1,1],[2,2,0]]

b = [1,1,1]

a = [[2,-12],[1,5]]
b = [1,1]
def eigenv(x,y,tolerance, max_itr):
    
    condition = True
    lambda_old = max(y)
    for i in range(max_itr):
       
        #lambda_old = lambda_new
        print(condition)
        if condition:
        
            y = np.matmul(x,y)
            lambda_new = np.min(y)
            p = y/min(abs(k) for k in y)
            #y = p
            
            condition = abs(lambda_new - lambda_old) > tolerance
            lambda_old = lambda_new
            print(p)
            print(min(y))
        else:
            break
    return(lambda_new, p)

print(eigenv(a,b,0.001,200))


