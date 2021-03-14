# a,b =map(int,input().split())
# c = a*(b%10)
# d = a*(b%100//10)
# e = a*(b//100)

# print(c)
# print(d)
# print(e)
# print(e*100+d*10+c)


num1 = int(input())
num2 = input()  #각 자리 숫자 받기 위해 str 로 입력 받기

for i in range(0,len(num2)) :
    multi = num1 * int(num2[2-i])
    print(multi)

print(num1*int(num2))

