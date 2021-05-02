# 28776KB, 64ms

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

print(cnt)

