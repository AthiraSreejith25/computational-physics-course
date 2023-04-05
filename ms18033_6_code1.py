import numpy as np
import matplotlib.pyplot as plt


x = [[4,1,1],[0,2,1],[-2,0,9]]
y = [[1,0,-1,],[1,2,1],[2,2,3]]

c = 0

def bounds(h):
    boundlist = []
    fig, ax = plt.subplots()

    
    for i in range(len(h)):
        centre = h[i][i]
        radius = sum(h[i]) - centre
        ##circle_list.append(centre)
        #circle1 = plt.Circle((0, 0), 0.2, color='r')
        
        ax.set_xlim((-10,20))
        ax.set_ylim((-15, 20))
        circle1 = plt.Circle((centre, 0),  radius, color = 'r', fill = False)
        ax.add_artist(circle1)
    
        boundlist.append(sum(h[i]))
        boundlist.append(2*h[i][i] - sum(h[i]))
        #boundlist.append(centre - radius)
        #boundlist.append(centre + radius)
    plt.savefig('ms18033_6_output1-{}.png'.format(c))
    plt.show()
    
    
    return([max(boundlist) , min(boundlist)])

c += 1
print("The bounds of the eigenvalues of the first matrix is: " ,bounds(x))

c += 1
print("The bounds of the eigenvalues of the second matrix is: " ,bounds(y))


 
