# -*- coding: utf8 -*-
#DocGhiFile

def DocFile(fileName):
    lines = [] #list
    f = open(fileName, 'r' ,encoding="utf-8")
    for line in f:
        #print(line)
        lines.append(line)
    return lines
##############################
def Run():
    s= DocFile('text.txt')
    print(s)
#============================
if __name__ == '__main__':
    Run()


