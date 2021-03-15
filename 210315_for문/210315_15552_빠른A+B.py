#input()은 반복문으로 여러줄을 입력받을 때는 시간초과 발생할 수 있다. 
#맨 끝의 개행문자까지 입력받기 떄문에 문자열 저장시 .rstrip() 추가


##한 개의 정수 입력 받기
import sys
n = int(sys.stdin.readline()) #입력값은 문자열 저장으로 개행문자 포함됨, int로 형변환하면 개행 삭제

## 정해진 개수의 정수를 한 줄에 입력 받을 때

a,b,c = map(int, sys.stdin.readline().split)

##임의의 개수의 정수를 한 줄에 입력받아 리스트 저장
import sys
data = list(map(int,sys.stdin.readline().split()))


##임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때
import sys
data = []  #빈 리스트
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split()))) #입력받은 값 list로 형변환 후 저장


##문자열 n줄을 입력받아 리스트에 저장할 때 
import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]  #strip은 문자열 앞,뒤 공백 제거 (.rstrip)



#빠른 A+B
import sys 

n = int(sys.stdin.readline())  #int 변환했으니 , rstrip 생략
for i in range(n): 
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)

