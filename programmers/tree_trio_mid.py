# https://programmers.co.kr/learn/courses/30/lessons/68937
# ??


def solution(n, edges):
    answer = 0
    graph = [[] for _ in range(3)]
    for e in edges:
      a, b = e
      graph[a].append(b)
      graph[b].append(a)
    

    
    
    return answer

print(solution(4, [[1,2],[2,3],[3,4]])) # 2
print(solution(5, [[1,5],[2,5],[3,5],[4,5]])) # 2