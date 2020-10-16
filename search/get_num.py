from bisect import bisect_left, bisect_right
n, x = map(int, input().split())
data = list(map(int, input().split()))
r = bisect_right(data, x)
l = bisect_left(data, x)
if r-l==0:
  print(-1)
else:
  print(r-l)