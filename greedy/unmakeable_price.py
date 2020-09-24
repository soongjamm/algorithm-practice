# 만들 수 없는 금액
# python greedy/unmakeable_price.py
## 입력
# 5
# 3 2 1 1 9
## 출력
# 8

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
# 화폐 하나씩 꺼내
for x in data:
  # 만들 수 없는 금액을 찾았을 때 반복 종료
  if target < x:
    break
  target += x
print(target) # 만들 수 없는 금액 출력


## 내 아이디어
# from itertools import combinations

# n = int(input())
# arr = list(map(int, input().split()))
# maximum = sum(arr)

# result = []
# for i in range(1, n+1):
#   c = list(combinations(arr, i))
#   for r in c:
#     result.append(sum(r))

# for i in range(1, maximum):
#   if i not in result:
#     print(i)
#     break


  