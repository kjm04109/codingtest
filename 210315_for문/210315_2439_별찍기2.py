n = int(input())

for i in range(1,n+1):
    print(" "*(n-i),"*"*i,sep="") #공백채우고 별,

#콤마,로 이어주면서 생기는 공백을 지워주기 위해 => sep="" 
