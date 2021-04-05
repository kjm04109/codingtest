n = int(input())

for i in range(n):
    test = str(input())
    cnt = 0
    sum = 0
    for t in test:
        if t =="O":
            cnt +=1
            sum += cnt
        else : 
            cnt = 0
    print(sum)