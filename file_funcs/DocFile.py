import time
# -*- coding: utf8 -*-
#DocGhiFile

def DocFile(fileName):
    t0 = time.time()
    lines = [] #list
    f = open(fileName, 'r' ,encoding="utf-8")
    for line in f:
        #print(line)
        lines.append(line)
    print("Time: %8.6f" %(time.time() - t0))
    return lines
##############################
def Run():
    s= DocFile('text.txt')
    print(s)
#============================
if __name__ == '__main__':
    Run()


