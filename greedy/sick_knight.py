# n은 1, 2와 그 이상일때만 고려해주면 된다.
# 무조건 오른쪽으로 움직여야 하므로
# m을 고려하는 것이 중요하다

n, m = map(int, input().split())

cnt = 1

if n == 1:
  pass
elif n == 2:
  cnt = min(4, (m+1)//2)
else:
  if m <= 6:
    cnt = min(4, m)
  else:
    cnt = m-2

print(cnt)