import algorithms.Rsa.MyMath as MyMath
import algorithms.Rsa.MyBase as MyBase


def getPrivateKey (file) : # file Privatekey
	fi = open(file,"r", encoding="utf-8")
	n = int(fi.readline())
	d = int(fi.readline())
	fi.close()
	return n, d

def getCiphertext(file): # file Ciphertext
	fi = open(file,"r", encoding="utf-8")
	C = fi.readline()
	C = C.split(" ")
	C = C[:-1]
	fi.close()
	return C

def decode(Cipher, key): # file PlanintextDecode
	key = tuple(key.split("\n"))
	Cipher = Cipher.strip()

	n, d = key
	n = int(n)
	d = int(d)

	C = [Cipher]

	fo = open("algorithms/Rsa/Data/PlaintextDecode.txt","w", encoding="utf-8")

	base = 4
	P = ""

	for i in C:
		m = MyMath.powMod(MyBase.toInt(i,64),d,n)
		c = str(m)
		while len(c) % base != 0:
			c = '0' + c
		x = 0
		while x != len(c):
			a = c[x:x+base]
			x+= base
			P+= chr(int(a))
			fo.write(chr(int(a)))
	fo.close()
	
	return P
