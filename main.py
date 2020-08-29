# first commit
age = int(input())
max_rate = 220-age

li = [0 for i in range(6)]
while True:
  rate = input()
  if ㄱㅁ:
        lines.append(line)
  else:
      break
  rate = int(rate)
  pcnt = int((rate/max_rate)*100)

  if pcnt < 60:
    li[5] += 1
  elif pcnt < 68:
    li[4] += 1
  elif pcnt < 75:
    li[3] += 1
  elif pcnt < 80:
    li[2] += 1
  elif pcnt < 90:
    li[1] += 1
  else :
    li[0] += 1

for i in range(len(li)):
  print(li[i],end = ' ')