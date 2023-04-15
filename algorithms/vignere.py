def MaHoa(plaintext, key):
    ciphertext = ""
    for i in range (len(plaintext)):
        c = plaintext[i]
        vt_key = i % len(key)
        if c!= ' 'and c!='\n':
            so = ord(c) - 33
            so_key = ord(key[vt_key])- 33 + 1
            so = (so + so_key)%65500
            ciphertext += chr (so + 33)
        else:
            ciphertext += key[vt_key]
    return ciphertext
#==============================================
def GiaiMa(ciphertext, key):
    plaintext = ""
    for i in range (0, len(ciphertext), 1):
        c = ciphertext[i]
        vt_key = i % len(key)
        if c!= key[vt_key]:
            so = ord(c) - 33
            so_key = ord(key[vt_key]) - 33 + 1
            so = (so - so_key + 65500)%65500
            plaintext += chr(so + 33)
        else:
            plaintext += ' '
    return plaintext
#==============================================
def Run():
    p = input('Moi nhap chuoi can ma hoa: ')
    p = p.upper()
    key = input('Moi nhap key: ')
    key = key.upper()
    c = MaHoa(p, key)
    print('Sau khi ma hoa: ', c)

    s = GiaiMa(c, key)
    print('Sau khi giai ma: ', s)
#==============================================
if __name__ == '__main__':
    Run()
#==============================================


