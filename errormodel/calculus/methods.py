import math

def taylor(fn,fd,fe,x,iter=2):
  s=0
  for i in range(0,iter):
    s += fn(i)/math.factorial(fd(i))*(x**fe(i))
  return s

def seno(x):
  return taylor(lambda n: (-1)**n, lambda n: 2*n+1, lambda n: 2*n+1, x)

def cosseno(x):
  return taylor(lambda n: (-1)**n, lambda n: 2*n, lambda n: 2*n, x)

def exp(x):
  return taylor(lambda n:1, lambda n:n, lambda n:n, x)

def rad(x):
  return x/180*math.pi