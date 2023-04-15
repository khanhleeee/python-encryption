#=====================================
def MaHoa(p, key):
    ciphertext=""
    for i in range (len(p)):
        c = p[i]
        vt_key = i % len(key)
        if c!= 32:
            so = ord(c) - 65
            so_key = ord(key[vt_key])- 65 + 1
            so = so ^ so_key
            ciphertext += chr (so + 65)
        else:
            ciphertext += key[vt_key]
    return ciphertext
#==============================================
def Run():
    #p = input('Moi nhap chuoi can ma hoa: ')
    p = input('Moi nhap chuoi can ma hoa: ')
    p = p.upper()
    key = input('Moi nhap key: ')
    key = key.upper()
    c = MaHoa(p, key)
    print('Sau khi ma hoa: ', c)

    s = MaHoa(c, key)
    print('Sau khi giai ma: ', s)
#==============================================
if __name__ == '__main__':
    Run()
#==============================================
