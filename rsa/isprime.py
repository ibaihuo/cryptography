import random

def powmod(x,a,m):
    r=1
    while a>0:
        if a%2==1: r=(r*x)%m
        a=a>>1; x=(x*x)%m
    return r

def isprime(p):
    q=p-1
    while q%2==0: q=q>>1
    for i in xrange(1,7):  ## probability adjusted here
        a=2+long(random.random()*(p-2))
        if powmod(a,p-1,p)
