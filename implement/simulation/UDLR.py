
### dictionary 사용
n = int(input())
plans = list(input().split())


x, y = 1, 1 # 출발 위치
# index : 0-상, 1-하, 2-좌, 3-우
d = { 'U': 0, 'D': 1, 'R':2, 'L':3}
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for plan in plans:
    nx = x+dx[d[plan]]
    ny = y+dy[d[plan]]
    if nx < 1 or n < nx or ny < 1 or n < ny :
      continue
    x,y = nx, ny
  
print(x, y)


# ### list 사용
# n = int(input())
# plans = list(input().split())

# x, y = 1, 1
# d = ['U', 'D', 'R', 'L']
# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]

# for plan in plans :
#   for i in range(len(d)):
#     if plan == d[i]:
#       nx = x+dx[i]
#       ny = y+dy[i]
#     if nx < 1 or n < nx or ny < 1 or n < ny :
#       continue
#     x,y = nx, ny