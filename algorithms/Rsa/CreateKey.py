import algorithms.Rsa.MyMath as MyMath
import algorithms.Rsa.GenePrime as GenePrime

def getE(phi):
	e = 65537
	while True:
		if MyMath.GCD(e,phi) == 1:
			break
		e+= 2
	return e

def getD(e, phi):
	d = MyMath.GCD_extended(e,phi)[0] #[x,y,z] #d = x
	if d < 0:
		d+= phi
	return d

def main():
	p, q = GenePrime.getPQ()

	n = p*q
	phi = (p-1)*(q-1)
	e = getE(phi)
	d = getD(e, phi)
	
	fo = open("algorithms/Rsa/Data/PublicKey.txt","w")
	fo.write(str(n)+'\n'+str(e))
	fo.close()
	fo = open("algorithms/Rsa/Data/PrivateKey.txt","w")
	fo.write(str(n)+'\n'+str(d))
	fo.close()

# main()
