# 세트(set) 집합
# 생성
fruit_set = {'사과', '바나나', '오렌지'}
print(fruit_set)
# 중복x 
fruit_set = {'사과', '바나나', '오렌지', '사과', '바나나'}
print(fruit_set)

# 순서가 없기 때문에 -> 인덱싱x (0,1,2 ...선택할수 없음)
#fruit_set[1]
#TypeError: 'set' object is not subscriptable

# 추가, 순서가 없다.
fruit_set.add('키위')
print(fruit_set)

# 확장
vegetable_set = {'당근', '토마토', '양파'}
fruit_set.update(vegetable_set)
print(fruit_set)

# 삭제
fruit_set.remove('양파')
print(fruit_set)

fruit_set.clear()
print(fruit_set) # set()

del fruit_set
#print(fruit_set)