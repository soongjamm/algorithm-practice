# 백준 10815 - 숫자 카드
# python search/number_card.py
## 입력
# 5
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10
## 출력
# 1 0 0 1 1 0 0 1

n = int(input())
na = list(map(int, input().split()))
m = int(input())
ma = list(map(int, input().split()))

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

na.sort()
for i in range(m):
  print(binary_search(na, ma[i], 0, n-1), end = ' ')
