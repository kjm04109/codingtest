# 28776KB, 64ms
import time
start_time = time.time()

n , k = map(int, input().split())
# kind = list(map(int, input().split()))
kind = []
for i in range (0,n):
    kind.append(int(input()))

kind = sorted(kind, reverse=True)
cnt = 0 
ch = k

for i in kind :
    if ch // i > 0 :
        cnt += ch//i
        ch = ch%i
        if ch == 0 :
            break
    else :
        continue

print(cnt)

end_time = time.time()
print(end_time - start_time)
