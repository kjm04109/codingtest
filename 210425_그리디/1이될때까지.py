import time

start_time = time.time()

n, k  = map(int, input().split())
cnt = 0

# while n != 1:
#     if n % k == 0 :
#         n /= k
#         cnt += 1

#     else :
#         n -= 1
#         cnt += 1
### 8.5137300491333 초

while True :
    target = (n//k)*k
    cnt += (n-target)
    n = target
    if n <k :
        break
    n //= k 
    cnt += 1

cnt += (n-1)
# 3.8258423805236816 
        
print(cnt)

end_time = time.time()
print(end_time - start_time)
