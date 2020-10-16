from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index - left_index

# 모든 단어를 길이마다 나누어서 저장하기 위한 리스트
array = [[] for _ in range(10001)]
# 모든 단어를 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
  answer = []

  for word in words: # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
    array[len(word)].append(word)
    reversed_array[len(word)].append(word[::-1])
  
  for i in range(10001):
    array[i].sort()
    reversed_array[i].sort()
  
  for q in queries: # 쿼리를 하나씩 확인하며 처리
    if q[0] != '?': # 접미사에 와일드카드가 붙은 경우
      res = count_by_range(array[len(q)], q.replace('?','a'), q.replace('?', 'z'))
    else:
      res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
    answer.append(res)

  return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))


# 길이별로 단어를 배열에 넣어넣고 정렬한 다음 조건에 부합하는 단어의 시작과 끝을 찾아서 차이를 구하면 그것이 개수임
