
def RSAEncrypt(e,n,c):
    if c > n:
        print "Break message into smaller blocks before encrypting"
        sys.exit
    E=decToBin.modExp(c,e,n)
    return E

#This is a little non-standard for factoring, but I'm assuming the RSA modulus has only 2 factors, that is, that p and q are not pseudo primes
#and as such, n would in fact have only 2 factors (p and q)
def RSAFactor(n):
    i = 2
    k = n
    factor = [0,0]
    while i < math.sqrt(n):
        if (k % i == 0):
            k = k / i
            factor = [i,k]
            return factor #Once I find the factors, stop ... or the loop will continue, potentially for a very long time
        else:
            i += 1
    return [0,0]

#Call this function to generate the decryption key for a particular n; e is assumed to be 3
#The first output is d, the decryption exponent, the second is the passed value n
def breakCode3(n):
    factors = RSAFactor(n)
    p = factors[0]
    q = factors[1]
    z = (p - 1)*(q - 1)
    d = (2*z + 1)/3
    return [d,n]

#Performs the fast algorithm for modular exponentiation where b is the base, e the exponent, and m the modulus
def modExp(b,e,m):
    x,i = 1,0
    power = b % m
    k = decToBin(e)
    length = math.floor(math.log10(k))
    while(i <= length):
        if(k%10 == 1):
            x = (x*power)%m
        power = (power*power)%m
        k=math.floor(k/10)
        i += 1
    return x

#Returns a string of ones and zeros that, read as binary, represent the input n
def decToBin(n):
    i,k = 0,0
    while n > 0:
        x = n % 2
        n = n - x
        n = n / 2
        k = k + x*pow(10,i)
        i = i + 1
    return k
