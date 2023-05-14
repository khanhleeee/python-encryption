import random
import algorithms.Rsa.PrimeTest as PrimeTest

def Random (b):
	a = random.getrandbits(b)
	a = a | (1 << (b-1))
	a = a | 1
	return a;

def getPrime(b):
	p = Random(b)
	d1 = d2 = d3 = 0
	while True:
		d1+= 1
		if PrimeTest.Preprocessor(p) == False:
			p+= 2
			continue
		d2+=1
		if PrimeTest.Fermat(p,20) == False:
			p+= 2
			continue
		d3+=1
		if PrimeTest.Miller_Rabin(p,20) == False:
			p+= 2
			continue
		break
	return p

def getPQ():
	p = getPrime(1024)
	q = getPrime(1024)

	return p,q

