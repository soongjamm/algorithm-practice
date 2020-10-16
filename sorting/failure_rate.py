# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

import heapq

def solution(N, stages):
    answer = []
    people_num = len(stages)
    failure = [0]*(N+2)
    reached = [0]*(N+2)
    rate = [0]*(N+2)

    # 단계별 실패자 수
    for i in stages:
      failure[i] += 1

    # 단계별 도달한 사람 수
    reached[1] = people_num
    for i in range(2, N+1):
      reached[i] = (reached[i-1]-failure[i-1])
    
    # 실패율 계산
    h = []
    for i in range(1, N+1):
      if failure[i] ==0 or reached[i] == 0:
        rate[i] = 0
      else:
        rate[i] = failure[i] / reached[i]
      heapq.heappush(h, (-rate[i],i))
    for i in range(N):
      answer.append(heapq.heappop(h)[1])

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))