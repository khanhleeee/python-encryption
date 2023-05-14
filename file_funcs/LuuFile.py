#SaveFile
##############################
def GhiFile(lines, filename, key = ''):
    f = open(f"./texts/{filename}.txt", 'w', encoding="utf-8")
    f.writelines(lines)

    if(key != ''):
        print(key)
        f = open(f"./texts/{filename}_PrivateKey.txt", 'w', encoding="utf-8")
        f.writelines(key)

##############################
#GhiFile(lines)
def Run():
    s= GhiFile('text.txt')
    print(s)
#============================
if __name__ == '__main__':
    Run()
