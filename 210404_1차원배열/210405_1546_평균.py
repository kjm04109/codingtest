n = int(input())

score_list = list(map(int,input().split()))

high = max(score_list)
for i in range(n):
    score_list[i] = score_list[i]/high*100

print(sum(score_list)/n)