array = [ 7, 5, 9, 0, 3, 1, 6, 2, 4, 8 ]

for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if array[j] < array[j-1]: # 한 칸씩 왼쪽 이동
      array[j], array[j-1] = array[j-1], array[j]
    else: # 자기보다 작은 수를 만나면 멈춤
      break

print(array)