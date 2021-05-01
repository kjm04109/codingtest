
import time

start_time = time.time()

n = int(input())
score = list(map(int, input().split()))

score = sorted(score)
result = 0 
count = 0

for i in score :
    count += 1 
    if count >= i :
        result += 1 
        count = 0
print (result)

# 그룹 수 최소화
# while score != [] :
#     c = score[-1]
#     if c > len(score) :
#         score.remove(c)
#     elif c == len(score):
#         result +=1
#         break
#     else :
#         score = score[c-1:-1]
#         result += 1
# print(result)


end_time = time.time()
print(end_time - start_time)
