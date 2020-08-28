n, m = map(int, input().split())

## 1. 정렬 이용
# cards = list()
# for i in range(n):
#   cards.append(list(map(int, input().split()))) 
#   cards[i].sort()
# cards.sort(reverse=True)
# print(cards[0][0])

## 2. min() 함수 활용
answer = 0
for i in range(n):
  cards = list(map(int, input().split()))
  min_value = min(cards)
  answer = max(answer, min_value)
print(answer)

## 3. 이중 반복문에서 min() 함수
# answer = 0
# for i in range(n):
#   cards = list(map(int, input().split()))
#   min_val = 10001
#   for a in cards:
#     min_val = min(a, min_val)
#   answer = max(min_val, answer)

# print(answer)

