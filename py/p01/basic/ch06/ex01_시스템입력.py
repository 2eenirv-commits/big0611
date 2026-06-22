# 시스템 입력
# input()
print("터미널에 출력 정보를 기록")
input("입력 메세지를 기록:")

# 사용자로부터 이름을 입력
'''
이름을 입력하세요: 홍길동
'''
name = input('이름을 입력하세요.')
print(name + '님, 안녕하세요')

# 키에 따른 권장체중
# input은 항상 문자열을 반환. -> int('160') -> 160
height = int(input('키를 입력하세요:'))
weight = (height - 100)* 0.85
#TypeError: unsupported operand type(s) for -: 'str' and 'int'
print('당신의 권장체중은' + str(weight) + 'kg입니다.')
# print('당신의 권장체중은 {}kg 입니다.'.format(weight))
# print(f'당신의 권장체중은{weight}kg입니다.') -> f-string방식을 사용하면 변환시킬 필요x

