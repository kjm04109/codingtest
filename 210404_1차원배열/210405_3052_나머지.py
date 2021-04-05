num_list = []
for i in range(0,10):
    a = int(input())
    n = a % 42
    num_list.append(n)

uniq_num = set(num_list)   #set : 리스트에서 중복값 없애는 함수
print(len(uniq_num))


