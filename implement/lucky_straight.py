# 럭키 스트레이트

# 점수 n
n = input()

l1 = list(map(int, n[:len(n)//2]))
l2 = list(map(int, n[len(n)//2:]))

if sum(l1) == sum(l2):
   print("LUCKY")
else:
   print("READY")