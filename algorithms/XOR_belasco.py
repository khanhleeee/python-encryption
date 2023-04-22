    #==========XOR BELASCO==============
def MaHoa(plaintext,key):
    ciphertext=""
    for i in range(len(plaintext)):
        c = plaintext[i]
        if c!=' ':
            row = ord(key[i%len(key)]) - 33;
            col = ord(c) - 33;
            so = row ^ col
            ciphertext = ciphertext+ chr(so+ 33)
        else:
            ciphertext=ciphertext+' '
    return ciphertext
#====================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    p=p.upper()
    k =  input("Moi nhap chuoi key: ")
    k=k.upper()
    c = MaHoa(p,k)
    print("Sau khi ma hoa= ", c)
    s= MaHoa(c,k)
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main() 
