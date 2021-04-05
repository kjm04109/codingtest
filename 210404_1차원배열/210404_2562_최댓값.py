data = []
for i in range(0,9):
    a = int(input())
    data.append(a)

# n = 0

# for i in range(0,len(data)):
#     if int(data[i])> n  :
#         n = data[i]
#         num = i
#     else :
#        continue
# print(n, num+1)

#더 쉬운 방법
max_data = max(data)
print(max_data,data.index(max_data)+1)
