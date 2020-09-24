# 모험가 길드
# python greedy/adventurer_guild.py
## 입력
# 5
# 2 3 1 2 2
## 출력
# 2

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

now = 1
cnt = 0
groups = 0
for i in arr:
  if now == i:
    cnt += 1
    if cnt == now:
      cnt = 0
      groups += 1
  elif now < i:
    now += 1
    cnt = 1

print(groups)
