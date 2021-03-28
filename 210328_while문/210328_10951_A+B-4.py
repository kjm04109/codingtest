import sys

while (True):
    try : 
        a,b = map(int,sys.stdin.readline().split())
        print(a+b)
    except:
        break

## break 조건 없을 땐, 예외처리 꼭!!
