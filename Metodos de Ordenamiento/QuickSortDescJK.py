def intercambia( A, x, y):
    tmp= A[x]
    A[x]= A[y]
    A[y] = tmp
    
def Particionar( A,p,r):
    print (A)
    x=A[p]
    print (x)
    i = p
    for j in range(p+1, r+1):
        if(A[j]>=x): #Para poder hacerlo en forma descendente es modificar el signo mayor que y menor que < >
            i=i+1
            intercambia( A,i,j)
    intercambia( A,i,p)
    return i

def Quicksort(A,p,r):
    if( p < r):
        q=Particionar(A,p,r)
        Quicksort(A,p,q-1)
        Quicksort(A,q+1,r)

A=[10,80,30,90,40,50,70]
Quicksort(A,0,6)
print(A)