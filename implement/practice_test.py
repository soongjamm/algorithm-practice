def solution(answers):
  patterns = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
  count = [0, 0, 0]
  for i, ans in enumerate(answers):
    if ans == patterns[0][i%len(patterns[0])]:
      count[0] += 1
    if ans == patterns[1][i%len(patterns[1])]:
      count[1] += 1
    if ans == patterns[2][i%len(patterns[2])]:
      count[2] += 1

  res = list()
  for i in range(3):
    if max(count) == count[i]:
      res.append(i+1)
  print(count)
  return res


answers = [1,2,3,4,5]
solution(answers)