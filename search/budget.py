# 백준 2512 - 예산
# python search/budget.py
## 입력
# 4
# 120 110 140 150
# 485
## 출력
# 127

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

def binary_search(arr, maximum, start, end):
  res = 0
  
  while start <= end:
    total = 0
    up_limit = (start+end) // 2

    for i in range( len(arr) ):
      if arr[i] > up_limit:
        total += arr[i]-(arr[i]-up_limit)
      else:
        total += arr[i]
  
    if total > maximum:
      end = up_limit - 1
    else:
      start = up_limit + 1
      res = up_limit
  return res

# sort 필요 없다. arr은 합치는데만 쓰기 때문이고 일정한 범위를 순서대로 탐색하기 때문
sum = 0
for i in arr:
  sum += i
  
if sum <= m:
  print(max(arr))
else:
  print(binary_search(arr, m, 1, max(arr)))