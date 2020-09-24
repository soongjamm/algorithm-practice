# 만들 수 없는 금액
# python greedy/unmakeable_price.py
## 입력
# 5
# 3 2 1 1 9
## 출력
# 8

from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))
maximum = sum(arr)

result = []
for i in range(1, n+1):
  c = list(combinations(arr, i))
  for r in c:
    result.append(sum(r))

for i in range(1, maximum):
  if i not in result:
    print(i)
    break


  