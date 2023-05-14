import time
#=======GHI CHU
#==MAHOA
def MaHoa (plaintext, key):
    # cau lenh cha co dau :
    t0 = time.time()
    ciphertext=""
    # doi voi python ' hay " la nhu nhau
    
    for c in plaintext:
        if c!=' ' and c != '\n':
            so = ord(c) - 33;
            #65 -> A
            so = (so + int(key)) % 65500;
            ciphertext = ciphertext + chr(so+33)
        else:
            ciphertext=ciphertext+c
    
    print("Running time: %8.6f s" %(time.time() - t0))

    return ciphertext

#========================================GIAIMA
def GiaiMa(ciphertext, key):
    plaintext = ""
    for c in ciphertext:
        if c!= ' ' and c != '\n':
            so = ord(c) - 33
            so = (so - int(key) + 65500) % 65500
            plaintext = plaintext + chr(so+33)
        else:
            plaintext = plaintext + c
    print(type(plaintext))
    return plaintext

#==========================================RUN
def Run():
    p=input('Moi nhap chuoi can ma hoa: ')
    key =3
    c = MaHoa(p, key)
    print('Sau khi ma hoa: ', c)

    s= GiaiMa(c, key)
    print('Sau khi giai ma: ',s)

#=============================================
if __name__ =='__main__':   #entry point
    Run()

