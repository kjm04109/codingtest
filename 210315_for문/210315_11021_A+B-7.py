import sys

n = int(sys.stdin.readline())

for i in range(1,n+1):
    a,b = map(int,sys.stdin.readline().split())
    print("Case #{0}: {1}".format(i, a+b))


