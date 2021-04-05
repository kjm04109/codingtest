c = int(input())


for i in range(c):
    
    cnt =0
    score_list = list(map(int,input().split()))
    n = score_list[0]
    avg = sum(score_list)/n-1
    for a in score_list:
        if a == score_list[0]:
            continue
        elif a > avg:
            cnt += 1 
    avg_ratio = cnt/n*100
    print("{:.3f}%" .format(avg_ratio))