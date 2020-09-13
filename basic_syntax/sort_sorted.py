# sort와 sorted의 차이

## sort
### list형에 한해서 동작
### list 내부에서 정렬

## sorted 
### iterable(순회가능한) 자료형이면 동작
### 정렬된 값을 반환. 그래서  n = sorted()... 형식으로 사용

## 공통적으로 key는 함수여야 함
### key 매개 변수 입력
array = [('바나나', 2), ('사과', 1), ('포도', 5)]
def setting(data):
  return data[1]
array = sorted(array, key=setting) # 1.
array.sort(key=setting) # 2.
print(array)