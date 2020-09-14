# 바닥 공사(타일 깔기)
n = int(input())
d = [0]*1001

d[1] = 1
d[2] = 3

# i번째 타일을 놓였을 때 경우의 수가 3가지 있다.
# 마지막 타일이
## | 모양 타일인 경우 (i-1)에 놓여 i까지 온다
## = 모양 타일인 경우 (i-2)에 놓여 i까지 온다
## ㅁ 모양 타일인 경우 (i-2)에 놓여 i까지 온다
for i in range(3, n+1):
  d[i] = (d[i-1] + 2*d[i-2]) % 796796

print(d[n])