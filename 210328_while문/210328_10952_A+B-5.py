import sys
number= []
while (True):
    num = list(map(int,sys.stdin.readline().split()))
    if num[0]==0 & num[1]==0:
        break
    number.append(num)

for i in number:
    print(i[0]+i[1])
     

