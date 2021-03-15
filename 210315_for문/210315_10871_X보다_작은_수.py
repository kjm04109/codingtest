import sys

n, x =map(int,input().split())
data= list(map(int,sys.stdin.readline().split()))


for i in data:  #리스트 요소 i로 받아올 때는 그냥 data 
    if i < x:
        print(i,end = " ")  #자동 줄바꿈 안되도록 end 지정!!
    

