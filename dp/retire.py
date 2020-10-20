# 퇴사
# https://www.acmicpc.net/problem/14501

n = int(input())
t = []
p = []
dp = [0]*(n+1) # 아래 for문에서 i+t[i]부분 때문에 n+1로 만들어줌
for _ in range(n):
  tt, tp = map(int, input().split())
  t.append(tt)
  p.append(tp)

max_value = 0
for i in range(n-1, -1, -1):
  # 마지막 날 소요시간이 1이라면 상담 가능.
  # 그 경우를 위해 <= n 까지 허용
  if t[i]+i <= n: 
    dp[i] = max(p[i]+dp[i+t[i]], max_value)
    max_value = dp[i]
  else:
    dp[i] = max_value

print(max_value)