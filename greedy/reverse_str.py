# 문자열 뒤집기
# python greedy/reverse_str.py

s = input()

flip = [0]*2 # 연속된 개수를 기록
now = int(s[0]) 
flip[now] += 1 # 

for c in s:
  c = int(c)
  if c != now:
    flip[c] += 1
    now = c

print(min(flip))
