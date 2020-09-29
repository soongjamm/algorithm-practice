# 기둥과 보 설치

# 설치된 구조물이 가능한 구조물인지 확인하는 함수
def check(answer):
  for x, y, stuff in answer:
    if stuff == 0: # 설치된 것이 기둥인 경우
      # 바닥 위 or 보의 한쪽 끝부분 위 or 다른 기둥 위 이면 정상
      if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
          continue
      return False
    elif stuff == 1:
      # 한쪽 끝부분이 기둥 위 or 양쪽 끝부분이 다른 보와 동시에 연결 이면 정상
      if [x, y-1, 0] in answer or [x+1, y-1, 0]in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
        continue
      else:
        return False
  return True

def solution(n, build_frame):
  answer = []

  # order index
  # 0 = x, 1 = y, 2 = a(기둥-보), 3 = b(삭제-설치)
  for order in build_frame:
    x, y, a, b = order
    # 명령 수행
    if b == 0:
      answer.remove([x, y, a])
      if not check(answer):
        answer.append([x, y, a])
    if b == 1: 
      answer.append([x, y, a])
      if not check(answer):
        answer.remove([x, y, a])
  return sorted(answer)


# 실행

# build_frame : [x, y, a, b]
# a : 0 - 기둥, 1 - 보 
# b : 0 - 삭제, 1 - 설치

build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame2 = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

solution(5, build_frame)
# = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
solution(5, build_frame2)
# = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

solution(5, [[0,0,0,1], [0,1,0,1],[1,1,0,1],[2,1,0,1], [2,0,0,1], [2,2,0,1], [2,1,0,1], [2,1,1,1]])