# 병사 배치하기
# https://www.acmicpc.net/problem/18353

# hint : LIS (Longest Increasing Subsequence)
# 가장 긴 증가하는 수열. dp[i] : array[i]가 마지막에 왔을 때 부분수열의 최대 길이

n = int(input())
data = list(map(int, input().split()))
data.reverse()
d = [1]*(n)

for i in range(1, n):
  for j in range(0, i):
    if data[i] > data[j]:
      d[i] = max(d[i], d[j]+1)

print(n-max(d))
