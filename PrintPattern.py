""" def pypat(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(i,j)
            print("* ", end="")
        print("\r")

n = 5
pypat(n) """

def pypat2(n):
    k = 2*n - 2 #8
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")

        k = k - 2

        for j in range(0, i+1):
            print("* ",end="")
        
        print("\r")
        
n = 5
pypat2(5)