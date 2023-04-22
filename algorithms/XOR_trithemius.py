#============XOR TRITHEMIUS==============
def MaHoa(plaintext):
    ciphertext=""
    for i in range(len(plaintext)):
        c = plaintext[i]
        if c!=' ':
            so = ord(c) - 33;
            so = so ^ (i%65500)
            ciphertext = ciphertext+ chr(so+ 33)
        else:
            ciphertext=ciphertext+' '
    return ciphertext
#========================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    p=p.upper()
    c = MaHoa(p)
    print("Sau khi ma hoa= ", c)
    s= MaHoa(c)
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main()