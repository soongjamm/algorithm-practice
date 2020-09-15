# 백준 1654
# python search/cutting_LANwire.py 
## 입력
# 4 11
# 802
# 743
# 457
# 539
##출력
# 200

k, n = map(int, input().split())
lan = list()
for _ in range(k):
  lan.append(int(input()))

def binary_search(arr, target, start, end):
  res = 0
  while (start <= end):
    sum = 0
    mid = (start+end) // 2
    for i in arr:
      sum += (i // mid)
    if sum < target:
      end = mid - 1
    else:
      res = mid
      start = mid + 1
  return res

print(binary_search(lan, n, 1, max(lan)))