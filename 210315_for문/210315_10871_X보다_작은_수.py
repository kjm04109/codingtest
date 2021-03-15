import sys

n, x =map(int,input().split())
data= list(map(int,sys.stdin.readline().split()))


for i in data:
    if i < x:
        print(i,end = " ")  #자동 줄바꿈 안되도록 end 지정!!
    

