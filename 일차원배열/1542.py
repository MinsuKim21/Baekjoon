import sys

input = sys.stdin.readline
numberator = int(input())
a,b,c = map(float, input().split())
print((a+b+c) / numberator)