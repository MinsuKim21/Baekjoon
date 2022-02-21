import sys
L=[]
for i in range(9):
    L.append(int(sys.stdin.readline()))
print(max(L))
print(L.index(max(L))+1)