# 볼링공 고르기
# python greedy/bowling_ball.py

n, m = map(int, input().split())
arr = list(map(int, input().split()))

from itertools import combinations
import math
li = list(combinations(arr, 2))
dup = 0
for i in li:
  if i[0] == i[1]:
    dup += 1

ans = math.factorial(n)//(math.factorial(n-2)*2) - dup
print(ans)