import numpy as np 
a = np.matrix([[1,2,-1], [3,4,1], [5,1,-3]])
b = np.matrix([[1],[4],[8]])

 

def gauss(a,b):
    n = len(b)
    for k in range(1,n):
        for i in range(k+1,n):
            if  a[i,k] != 0.0:
                a[i,k+1:n] = a[i,k+1:n] - a [i,k]/a[k,k] *a[k,k+1:n]
                b[i] = b[i] -a [i,k]/a[k,k] *b[k]
    for k in range (n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]

    print("Check:", np.linalg.solve(a,b))
    print("MetGauss:", np.linalg.inv(a) * b)
    return b

 

print("Reverse met:", gauss(np.matrix(a), np.matrix(b)))