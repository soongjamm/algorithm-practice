def isCorrect(p):
  stack = []
  s = ''
  for i in p:
    if i == '(':
      stack.append('(')
    else:
      if stack:
        s += stack.pop()
      else:
        return False
  
  if stack:
    False
  
  return True
    
def pair_index(p):
  cnt = 0 
  idx = 0
  for i in range(len(p)):
    if p[i] == '(':
      cnt += 1
    else:
      cnt -= 1
    if cnt == 0:
      idx = i
      return idx

def solution(p):
  u, v = '', ''
  if p == '':
    return ''
  i = pair_index(p)
  u = p[:i+1]
  v = p[i+1:]
  if isCorrect(u):
    u += solution(v)
  else:
    s = '('
    s += solution(v)
    s += ')'
    new_u = u[1:-1]
    new_u = new_u.replace('(','1').replace(')','(').replace('1',')')
    s += new_u
    return s

  return u

# print(solution("(()())()")) # "(()())()"
# print(solution(")(")) # "()"
print(solution("()))((()")) # "()(())()"
