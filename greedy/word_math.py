# 단어를 각 알파벳을 미지수로 갖는 다항식으로 생각
# ex. ABC = 100A + 10B + C

n = int(input())
w = list()
for _ in range(n):
  w.append(input())
w.sort(key=len, reverse=True)


# 각 알파벳에 가중치 부여해서 딕셔너리에 저장
alp = {}
for i in range(len(w)):
  l = len(w[i])
  for j in range(len(w[i])):
    if w[i][j] in alp:
      alp[w[i][j]] += 10 ** l
    else:
      alp[w[i][j]] = 10 ** l
    l -= 1

# alp 딕셔너리를 value 내림차순 정렬해서 다시 딕셔너리에 저장
alp = sorted(alp.items(), key = lambda x:x[1], reverse = True)
rep = {}
m = 9
for i in range(len(alp)):
  item = alp[i]
  rep[item[0]] = str(m)
  m -= 1

# 알파벳을 숫자로 변환
for i in range(len(w)):
  for k in rep:
    w[i] = w[i].replace(k, rep[k])

# 더하기
ans = 0
for v in w:
  ans += int(v)

print(ans)