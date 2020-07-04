# Recursive function to return gcd of a and b 
def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
# Function to return LCM of two numbers 
def lcm(a,b): 
    return int((a*b) // gcd(a,b))

def getN(p,q):
	return pow(p,2) * q

def getD(n, p, q):
	return pow(n,-1,lcm(p - 1, q - 1))

def encrypt(msg, n):
	return pow(msg,n,n)

def decrypt(msg,d,p,q):
	return pow(msg,d, p*q)
