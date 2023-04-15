#SaveFile
##############################
def GhiFile(lines, filename):
    f = open(filename, 'w', encoding="utf-8")
    f.writelines(lines)

##############################
#GhiFile(lines)
#============================
if __name__ == '__main__':
    Run()
