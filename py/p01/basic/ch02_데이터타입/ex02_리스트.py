# 리스트(list) [아이템, ...]
# 튜플 (아이템, ...)
# 세트 {아이템, ...}
# 딕셔너리 {키:160, ...}

# 비효율적인 방법
#ctrl+d: 같은 텍스트를 선택
fruit1 = '사과'
fruit2 = '바나나'
fruit3 = '오렌지'


# 컨테이너 자료형
# : 리스트, 튜플, 세트, 딕셔너리
# 효율적인 방법

fruits = ['사과', '바나나', '오렌지']
print(fruits)

fruits2 = ['사과','바나나','오렌지','사과','바나나']
print(fruits2)
# CRUD(Create, Read, Update, Delete)
# 리스트 아이템 선택(Select)
# 인덱싱(index)
print(fruits[0]) # 사과
print(fruits[-1]) # 오렌지
# 슬라이싱[시작인덱스idx:종료인덱스idx]
# [1:3] -> 1~2번까지
print(fruits[1:3]) # 바나나 오렌지 


# 수정(Update)
fruit_list = ['사과', '바나나', '오렌지']
fruit_list[1] = '키위'
print(fruit_list)

# 추가
# list객체.insert(인덱스, 아이템): 인덱스에 추가 
fruit_list.insert(2, '망고')
print(fruit_list)
# list객체.append(아이템): 끝에 추가
fruit_list.append('수박')
print(fruit_list)

# 리스트1.extend(리스트2)
vegetable_list = ['당근', '토마토', '양파']
fruit_list.extend(vegetable_list)
print(fruit_list)

# + 연산
list1 = [1,2,3]
list2 = ['기','나','다']
print(list1+list2)

# 삭제
# 리스트.remove(아이템)
fruit_list.remove('토마토')
print('지운 후:', fruit_list)
# del 리스트[인덱스]
del fruit_list[-1]
print(fruit_list)
# del 리스트
# del fruit_list
# print(fruit_list)
# NameError: name 'fruit_list' is not defined

fruit_list = ['사과', '키위', '망고']
print(fruit_list)
# 리스트.clear(): 리스트의 아이템만 모두 삭제
fruit_list.clear()
print(fruit_list)

# 정렬(sort)
'''
-오름차순: 
1,2,3..
가,나,다...

-내림차순(역, reverse):
3,2,1,0,-1...
c,b,a
다,나,가

'''

fruit_list = ['딸기', '망고', '블루베리', '수박', '사과' ,'바나나', '오렌지']
print("정렬전:",fruit_list)

# 리스트.sort(): 오름차순
fruit_list.sort()
print("정렬후:",fruit_list)

# 리스트.sort(reverse = True): 내림차순
fruit_list.sort(reverse = True)
print(fruit_list)


