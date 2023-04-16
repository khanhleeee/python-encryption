#SaveFile
##############################
def GhiFile(lines, filename):
    f = open(f"./texts/{filename}", 'w', encoding="utf-8")
    f.writelines(lines)

##############################
#GhiFile(lines)
def Run():
    s= GhiFile('text.txt')
    print(s)
#============================
if __name__ == '__main__':
    Run()
