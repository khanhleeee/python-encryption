import algorithms.RSA.MyMath as MyMath
import algorithms.RSA.MyBase as MyBase


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

# def decode(C): # file PlanintextDecode
# 	n, d= getPrivateKey("algorithms/RSA/Data/PrivateKey.txt")
# 	base = 4
# 	P = ""
# 	for i in C:
# 		if(i != ' ' and i != ''):
# 			m = MyMath.powMod(MyBase.toInt(i,64),d,n)
# 			c = str(m)
# 			while len(c) % base != 0:
# 				c = '0' + c
# 			x = 0
# 			while x != len(c):
# 				a = c[x:x+base]
# 				x+= base
# 				P+= chr(int(a))
# 	return P

def decode(C): # file PlanintextDecode
	n, d= getPrivateKey("algorithms/RSA/Data/PrivateKey.txt")
	print("c", C)
	P = ""
	for i in C:
		m = MyMath.powMod(MyBase.toInt(i,64),d,n)
		c = str(m)
		while len(c) % 4 != 0:
			c = '0' + c
		x = 0
		while x != len(c):
			a = c[x:x+4]
			x+= 4
			P+= chr(int(a))
	
	return P

