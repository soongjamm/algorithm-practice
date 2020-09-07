import sys

T = int(input())

for _ in range(T):
  ans = 0 # 채용 가능 최대 신입사원 수. 
  n = int(input())
  rank = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)])

  min = rank[0][1]
  for i in range(n):
    if i == 0:
      ans += 1
    elif rank[i][1] < min:
      # a 성적 순위 내림차순 정렬 상태에서 튜플을 순회하는데
      # 새 신입사원이 될 때 마다 새로운 기준이 된다. 
      min = rank[i][1]
      ans += 1
  
  print(ans)

  

