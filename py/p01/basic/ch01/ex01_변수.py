# 변수
# 5를 a에 할당(대입)
# =은 대입 연산자
a = 5
# ==(같다)
a == 5
# alt+위아래 방향키
print(a)

b = 3
print(b)

print(a + b)


# 문자열 데이터: '', ""
c = '가나다'
print(c)

#파이선 표기법(_: 스네이크 표기법)
radio_freq = 107.9
print(radio_freq)

# 잘못된 변수명
# 1. 숫자로 시작
# 2var = '행복'
# print(2var)

# 2. 공백이 들어있으면 안됨 -> 하나의 단어
# happy var = '행복'

# 3. _를 제외한 특수문자x
# happyvar! = '행복'

# 예약어는 사용x
# def = "함수"

# 영문의 대소문자 구별한다.
abc = 5
ABC =  'Apple'
#print() 내장함수의 인자의 수는 제한 없다.
print(abc, ABC)

#--------------------------------------

# 다중 변수 동시 선언
x, y, z = 'Apple', 'Banana', 'Carrot'
print(x, y, z)

# 변수명에 _(언더스코어) 사용
#-> 이는 주로 사용하지 않을 변수를 위한 자리표시자로 사용!
_, var = 3, 5
print(_, var)
add = - + var
print(add)

# 단일 값의 다중 변수 할당
x = y = z = '같은값'
print(x, y, z)