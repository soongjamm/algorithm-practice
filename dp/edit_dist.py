# 편집 거리
# A -> B 문자열로 수정할 때 삽입, 삭제, 교체의 사용 횟수

#str1 to str2
def edit_dist(str1, str2):
  n = len(str1)
  m = len(str2)

  # dp 테이블 초기화
  dp = [[0]*(m+1) for _ in range(n+1)]

  for i in range(1, n+1):
    dp[i][0] = i
  for i in range(1, n+1):
    dp[0][i] = i
  
  # 최소 편집 거리 계산
  for i in range(1, n+1):
    for j in range(1, m+1):
      # 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 대입
      if str1[i-1] == str2[j-1]:
        dp[i][j] = dp[i-1][j-1]
      else:
        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
  
  return dp[n][m]

# 두 문자열 입력받기
str1 = input()
str2 = input()

# 최소 편집 거리 출력
print(edit_dist(str1, str2))