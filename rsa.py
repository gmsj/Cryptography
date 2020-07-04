import math
import gmpy2

def gcdExtended(a, b):
    if a == 0 :   
        return b,0,1
    gcd, x1, y1 = gcdExtended(b%a, a)  
    x = y1 - (b//a) * x1  
    y = x1  
    return gcd,x,y

def modInverse(a, m):
    g, x, y = gcdExtended(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def totient(p,q):
	return (p-1)*(q-1)

def calcN(x,y):
	return (x * y)

def encript(msg, e, n):
	msgEnc = pow(msg, e, n)
	return msgEnc

def decript(msg, d, n):
	msgDec = pow(msg, d, n)
	return msgDec

def test(num):
	for i in range(2,num):
		if (num % i) == 0:
			print("Result: " + str(i) + " q: " + str(num//i))
			return i, num//i

def testSquare(num):
	gmpy2.get_context().precision=100000
	sqrt = int(gmpy2.sqrt(num))
	# print("Square: " + str(sqrt))
	for i in range(sqrt,1,-1):
		if (num % i) == 0:
			print("Result: " + str(i) + " q: " + str(num//i))
			return i, num//i

def factoryPQ(e, d, n):
	k = (e * d) -1
	g = 1
	while True:
		g = int(gmpy2.next_prime(g))
		t = k
		# print('g: ' + str(g) + ' | t: ' + str(t))
		while (t % 2) == 0:
			t = t // 2
			x = pow(g,t,n)
			# print('t: '+ str(t))
			if (x > 1):
				y, aux, aux1 = gcdExtended(x-1,n)
				if y > 1:
					p = y
					q = n // y
					return p, q