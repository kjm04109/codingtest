t = int(input())

check = t  #break 하기 위해 비교하려고 저장
cnt = 0

while True:
    i = t//10 + t%10   
    num = (t%10)*10+i%10  
    cnt += 1
    t = num  #반복 돌기 위해 t 수정 
    if num == check:  #확인
        break
    else :
        continue
print(cnt)


