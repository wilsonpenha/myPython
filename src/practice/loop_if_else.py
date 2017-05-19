'''
Created on 1 de mai de 2017

in Python code, the code indentation does matter
in the below code, if you move the else: position, it will affect the output.

@author: wpjunior
'''

import math


def main():
    print (avg_distance(x=[2,4,6], y=[8,10,12]))
    
def avg_distance(x,y):
    n = len(x)
    dist = 0
    for i in range(n):
        xi = x[i]
        yi = y[i]
        for j in range(i+1,n):
            dx = x[j]-xi
            dy = y[j]-yi
            dist += math.sqrt(dx*dx+dy*dy)
    return 2.0*dist/(n*(n-1))


if __name__ == '__main__': 
    main()