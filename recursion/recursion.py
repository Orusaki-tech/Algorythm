#create a function that prints numbers from 1 to n without using a for loop

def printnum(n:int, x:int=1):
    if x==n:
        print(n,x)
        return n

    print(x)
    return printnum(n,x+1)


printnum(5)


#write a functio that prints numbers from n to 1

def printnum2(n:int):
    if n==1:
        print(n)
        return 1
    print(n)
    return printnum2(n-1)

printnum2(9)