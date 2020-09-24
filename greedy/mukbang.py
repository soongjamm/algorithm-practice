# 무지의 먹방 라이브
# python greedy/mukbang.py

import heapq

def solution(food_times, k):
  # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
  if sum(food_times) <= k:
    return -1
    
  # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
  q = []
  for i in range(len(food_times)):
    # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
    heapq.heappush(q, (food_times[i], i+1))
  
  sum_value = 0 # 먹기 위해 사용한 시간
  previous = 0 # 직전에 다 먹은 음식 시간
  length = len(food_times) # 남은 음식 개수

  # sum_value + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
  # k를 넘으면 음식 시간을 빼지 않아야 하기 때문
  while sum_value + ((q[0][0] - previous) * length) <= k:
    now = heapq.heappop(q)[0]
    sum_value += (now - previous) * length
    length -= 1
    previous = now

  ## (k - sum_value) 시점에서는 배열 길이 끝까지 진행이 된 시점이기 때문에
  ## 첫 인덱스로 돌아가서 남은 시간만큼 음식을 먹어야 한다. 
  result = sorted(q, key=lambda x:x[1]) # 음식의 번호 기준으로 정렬
  return result[(k-sum_value)%length][1]


print(solution([10, 1, 2], 5))

print(solution([2, 4, 6, 1], 5))

print(solution([3, 1, 2], 5))

print(solution([10, 1, 2], 8))