
# 1) 끝나는 시간 오름차순, 시작하는 시간의 오름차순!!! 정렬
# 2) 앞 미팅의 끝나는 시간이 다음 미팅 시작 시간보다 같거나 크면 선택 + 1
# 3) 반복 

n = int(input())

sch = []

# 한줄 코딩
sch = sorted( [tuple( map(int,input().split())) for _ in range(n) ], key=lambda x : (x[1], x[0]) )

# for i in range(0,n):
#     st, et = map(int, input().split())
#     sch.append([st,et])

# sch.sort(key=lambda x : (x[1],x[0]))  # 끝나는 시간[1] 우선으로 정렬 후, 시작 시간으로 정렬

# sch = sorted(sch, key= lambda x : x[1])

et = sch[0][1]
cnt = 1

for i,j in sch[1:] :
    if i >= et:
        et = j
        cnt += 1
    
        
print(cnt)    

    
    
