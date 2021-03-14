h, m = map(int,input().split())

if  m>44 :
    print( h, m-45)
elif h==0 & m<45 :
    print(23, m+15)
else :
    print( h-1, 15+m)

# 45분 이상 0시   h, m-45
# 45분 이상, 0시 이상이면 h, m-45

# 45분 미만, h-1, 15+m
# 45분 미만, 0시  23, 15+m

