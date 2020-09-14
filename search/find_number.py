# 백준 1920 수찾기
# python search/find_number.py
## 입력
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
## 출력
# 1
# 1
# 0
# 0
# 1

n = int(input())
na = list(map(int, input().split()))
m = int(input())
ma = list(map(int, input().split()))

na.sort()

def binary_search(arr, target, start, end):
  while start <= end:
    mid = (start+end) // 2
    if arr[mid] == target:
      return 1
    elif arr[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return 0

for i in range(m):
  print(binary_search(na, ma[i], 0, n-1))