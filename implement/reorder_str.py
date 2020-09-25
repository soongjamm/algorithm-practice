# 문자열 재정렬

s = input()

n = 0
new = ''
for c in s:
  if c.isdigit():
    n += int(c)
  else:
    new += c
new = ''.join(sorted(new))
new += str(n)

print(new)