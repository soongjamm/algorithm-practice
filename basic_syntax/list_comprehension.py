# 리스트 컴프리핸션

## 0~9 까지 수 중에서 짝수만 저장하는 리스트
even = [i for i in range(10) if i % 2 == 0]
print(even)

## n X m 크기의 2차원 리스트 초기화
n = 3
m = 5
li = [
    [0] * m for _ in range(n)
]  # li = [[0]*m] * n 은 동일한 객체에 대한 레퍼런스를 n개 생성하는게 된다. 다른 의미.
print(li)

