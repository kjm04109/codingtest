import time

start_time = time.time()

s = str(input())

result = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])
    if num <= 1 or result <= 1:
        result += num 
    else :
        result *= num 

print(result)

# lst = []
# for i in range(0, len(s)) :
#     num = int(s[i])
#     lst.append(num)

# result = max(lst)
# lst.remove(result)

# for n in range(0,len(lst)) :
#     if lst[n] <= 1 :
#         result += lst[n] 
#     else :
#         result *= lst[n]





end_time = time.time()
print(end_time - start_time)

