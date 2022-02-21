import sys
n = int(sys.stdin.readline())
for i in range(1, n+1):
    print(" "*(i-1) + "*"*(n-i+1))
