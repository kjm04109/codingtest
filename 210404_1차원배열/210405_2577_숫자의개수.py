number = 1
for i in range(0,3):
    a  = int(input())
    number = number*a


num_list =[]
for i in str(number):   #정수를 문자로 전환하고 리스트 추가 
    i = int(i)      #다시 정수로 
    num_list.append(i)

for i in range(0,10):
    print(num_list.count(i))   #리스트 요소가 숫자면 바로 list.count(i)로 요소 갯수 셀 수 있음 
