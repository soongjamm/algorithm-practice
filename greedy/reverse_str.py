# 문자열 뒤집기
# python greedy/reverse_str.py

## 입력
# 0001100
## 출력
# 1

data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
  count0 += 1
else:
  count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) -1):
  if data[i] != data[i+1]:
    # 다음 수에서 0으로 바뀌는 경우
    if data[i+1] == '0':
      count1 += 1
    # 다음 수에서 1로 바뀌는 경우
    else:
      count0 += 1

print(min(count0, count1))
  

## 내 아이디어
# s = input()

# flip = [0]*2 # 연속된 개수를 기록
# now = int(s[0]) 
# flip[now] += 1 # 

# for c in s:
#   c = int(c)
#   if c != now:
#     flip[c] += 1
#     now = c

# print(min(flip))
