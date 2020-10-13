# 언어를 pypy2로 해야 통과
# https://www.acmicpc.net/problem/14888
from itertools import permutations
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
operations = list(map(int, sys.stdin.readline().split())) # 연산자 개수. + - * / 순

op = []
for i in range(len(operations)):
  for j in range(operations[i]):
    if i == 0:
      op.append('+')
    if i == 1:
      op.append('-')
    if i == 2:
      op.append('*')
    if i == 3:
      op.append('//')

perm_op = list(permutations(op, n-1))
max_n = -999999
min_n = 1e9
for op_arr in perm_op:
  op_arr = list(op_arr)
  op_arr.insert(0,0) # 인덱스 맞추기 위해
  res = arr[0]
  for i in range(n):
    if op_arr[i] == '+':
      res += arr[i]
    if op_arr[i] == '-':
      res -= arr[i]
    if op_arr[i] == '*':
      res *= arr[i]
    if op_arr[i] == '//':
      if res < 0:
        res *= -1
        res //= arr[i]
        res *= -1
      else:
        res //= arr[i]
  max_n = max(res, max_n)
  min_n = min(res, min_n)

print(max_n)
print(min_n)
