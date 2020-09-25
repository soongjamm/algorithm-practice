# 모험가 길드
# python greedy/adventurer_guild.py
## 입력
# 5
# 2 3 1 2 2
## 출력
# 2

n = int(input())
data = list(map(int, input().split()))
data.sort()

cnt = 0 # 현재 그룹에 포함된 모험가의 수
groups = 0 # 만들어진 그룹의 수

# data는 공포도의 집합
for i in data:
  cnt += 1 # 현재 그룹에 해당 모험가를 포함시킴
  if cnt >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    groups += 1 # 총 그룹의 수 증가
    cnt = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(groups)
