# 외벽 점검

from itertools import permutations

def solution(n, weak, dist):
  # 범위를 넘어갔을 때 인덱스 에러를 방지하기 위해 weak의 길이를 2배로 늘려준다.
  length = len(weak)
  for i in range(length):
    weak.append(weak[i]+n) 
  answer = len(dist) + 1 # 최대로 투입될 수 있는 친구 수 + 1로 초기화

  # 시작점으로 모든 weak의 원소를 시도해본다.
  for start in range(length):
    # n명이 투입될 수 있는 모든 경우의 수를 시도한다.
    for friends in list(permutations(dist, len(dist))):
      count = 1 # 투입된 친구의 수
      # 현재 투입된 친구가 마지막으로 점검할 수 있는 위치
      # position은 인덱스가 아닌 위치의 값을 의미한다.
      position = weak[start] + friends[count-1] 
      # 어디까지 점검할 수 있는지 확인한다.
      # 출발지가된 취약점부터 +'취약점의 크기'까지 '인덱스'를 돌면서 확인한다.
      # weak은 현재 원래 크기의 두배가 되어있고, 
      # 원래 크기만큼만 확인하면 되기 때문에 start + length 이다.
      for index in range(start, start+length):
        # 지금 친구가 확인할 수 있는 마지막 위치를 벗어나면 친구를 추가로 투입한다.
        if position < weak[index]:
          count += 1
          # 투입된 친구의 수가 최대치를 넘기면 종료
          if count > len(dist):
            break;
          # 새 출발지를 정할 때, 마지막 포지션에서 투입되는 것이 아니라, 아예 새로운 위치에 투입될 수 있다.
          # 그러므로 새로운 취약점에 투입되는게 효율적이다.
          position = weak[index] + friends[count-1]
      answer = min(answer, count)
  # 투입된 인원이 친구의 수를 초과하면 -1
  if answer > len(dist):
    return -1
  return answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4])) # 2
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7])) # 1