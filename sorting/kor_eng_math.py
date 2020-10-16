# https://www.acmicpc.net/problem/10825
# pypy3 
n = int(input())
data = []
for i in range(n):
  d = list(input().split())
  d[1], d[2], d[3] = int(d[1]), int(d[2]), int(d[3])
  data.append(d)

data = sorted(data, key = lambda x : (-x[1], x[2], -x[3], x[0]))


for i in data:
  print(i[0])