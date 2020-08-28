# 빠르게 입력 받기
## 입력 개수가 많은 경우 input()은 느리기 때문에 시간초과 될 수 있음
## rstrip() - readline()으로 입력하면 enter가 줄 바꿈 기호로 입력되어서 이 공백 문자를 제거하기 위함

import sys

data = sys.stdin.readline().rstrip()
print(data)
