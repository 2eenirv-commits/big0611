# 자료형
# 1. 숫자형
# 2. 불리언: True, False -> 예약어
# 3. 문자형

'''
데이터 타입
1) 기본 데이터
- 숫자(int,float)
- 문자(str)
- 불(bool)
2) 복합 데이터

'''

# 정수
x, y = 10, -25
# 실수
z = 3.14
# print(): 터미널 출력 내장 함수
# type(): 자료형 확인 내장 함수
print(type(x), type(y), type(z))

# 지수 표현식(e: exponential)
# e3 -> 10의 3승 -. 10*10*10
# 대소문자 구별 없음
# 17곱하기 10의 3승
a = 17e3
b = 17E3
c = -35.2e2
d = 275e-2
print(a, b, c, d)

# 불(bool): True, False -> 논리값
# 대입(할당) 연산자: =
# 비교 연산자: > < ==
# 100이 50보다 큰가? 참
a = 100 > 50
# 100이 50보다 작은가? 거짓
b = 100 < 50
# 100이 50보다 같은가? 거짓
c = 100 == 50
print(a, b, c)
# type(): 데이터의 유형을 확인 내장 함수
type(a)
print(type(a))

# 문자형(str): "", ''
a = 'Hello'
b = '123'
c = "How are you"
#다중커서: ctrl+alt+위아래 방향키
#alt+클릭
#ctrl+a -> 전체선택
#crtl+s -> 저장
#crtl+z -> 취소
print(type(a))
print(type(b))
print(type(c))

#다중 행 문자열(''', """")
x = """Twinkle,twinkle, little star,
How I wonder what tou are!
Up above the world so higt,
Like a diamond in the sky."""
print(x)

y = """Twinkle,twinkle, little star,\
How I wonder what tou are!\
Up above the world so higt,\
Like a diamond in the sky."""
print(y)

# 타입 변환
# int(), float(), str(), bool()
temperature = '20'
humidity = '50'
# 문자끼리는 문자열 연결
# 숫자끼리는 덧셈
# 문자 숫자 덧셈은 오류
print(temperature + humidity)

print(int(temperature)+int(humidity))

a = 0 #  False
b = 500 # True -> 0 이외의 숫자는 모두  True
c = '' # 빈값 -> False(' '공백도 True)
d = '하하호호' # True
e = None
print(bool(a), bool(b), bool(c), bool(d))
# False True False True False






