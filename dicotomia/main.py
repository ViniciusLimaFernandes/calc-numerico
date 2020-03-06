import math

def main():
    a = 2
    b = 3

    dicotomia(a,b,(a+b)/2)

def dicotomia(a,b,xi):
    x = (a+b)/2
    err = (abs(b-a))/2
    errRelat = abs((x-xi/max(1,abs(x))))

    print("a=",a," b=",b," x=",x," err=", err," errRelat=",errRelat)
    print(abs(x-xi), " < ",err*max(1,abs(x)))    

    if(abs(x-xi)<err*max(1,abs(x))):
        return

    if(calcFunc(x)*calcFunc(a) < 0):
        return dicotomia(a,x,x)
    
    return dicotomia(x,b,x)
    
def calcFunc(x):
    f = lambda n: (n**2)-5

    return f(x)

main()