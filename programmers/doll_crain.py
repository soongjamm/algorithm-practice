# 카카오 인형뽑기 크레인

def solution(board, moves):
  answer = 0
  bucket = []
  # 하나씩 수행
  for m in moves:
    # 맨 위 행부터 맨 아래 행까지
    for i in range(len(board)):
      if board[i][m-1] > 0:
        if len(bucket) > 0 and board[i][m-1] == bucket[-1]:
          answer += 2
          bucket.pop()
        else:
          bucket.append(board[i][m-1])
        board[i][m-1] = 0
        break

  return answer

print(
  solution(
  [
  [0,0,0,0,0],
  [0,0,1,0,3],
  [0,2,5,0,1],
  [4,2,4,4,2],
  [3,5,1,3,1]],

  [1,5,3,5,1,2,1,4]
)
)