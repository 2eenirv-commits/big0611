# 제어문
# 1. 조건문: if~elif~else
# 2. 반복문: for, while

# for
'''
for 변수 in 반복자:
    수행문
    수행문
    ...

반복자(iterable): 컬렉션, range()
'''

scores = [80, 90,70, 65, 85, 95, 90, 80, 75, 80]
new_scores = []

for score in scores:
    new = score + 5
    new_scores.append(new)
print(new_scores) 

# 100점 만점
scores = [80, 90,70, 65, 85, 100, 90, 80, 75, 80]
new_scores = []

for score in scores:
    if score < 100:
        new = score + 5
    else:
        new = score        
    new_scores.append(new)

print(new_scores) 

# 리스트 컴프리헨션
'''
변수 = [수행문1 if 조건문 else 수행문2 for 변수 in 리스트]

'''
new_score2 = [score + 5 if score < 100 else score for score in scores]
print(new_score2)

# while
'''
무한루프(loop, 반복)
while True:
    수행문
'''

# len(scores): 아이템 수
scores = [80, 90, 70, 65, 95, 100, 90, 80, 75, 80]

print(len(scores))
new_scores = []
idx = 0

while idx < len(scores):
    if scores[idx] < 100:
        new = scores[idx] + 5
    else:
        new = scores[idx]    
    new_scores.append(new)    
    idx = idx + 1

print(new_scores)   

# ctrl+c: keyboardInterrupt -> 예외처리(try~)
# 흐름제어: break

time = 0
while True:
    #print('현재 사용량:' + str(time))
    print('현재 사용량: {}'.format(time))
    if time >= 300:
        print('[사용중단]하루 사용 권장량에 도달 또는 초과하였습니다.')
        break
    else:
        time = time + 50

time = 0
while True:
    print('현재 사용량: {}'.format(time))
    if time < 150:
        print('안전')
    if time >= 300:
        print('[사용중단]하루 사용 권장량에 도달 또는 초과하였습니다.')
        break
    else:
        time = time + 50      

# pass
time = 0
while True:
    print('현재 사용량: {}'.format(time))
    if time < 150:
        pass
        #print('안전')
    if time >= 300:
        print('[사용중단]하루 사용 권장량에 도달 또는 초과하였습니다.')
        break
    else:
        time = time + 50        

# 반복문 연습

shopping_dict = {'주문번호': 123, 
                 '주문자': '김**', 
                 '주소': '서울 마포구 상암동',
                 '주문항목': ['맛좋은 김치', '맛좋은 라면', '시원한 물']}
for key in shopping_dict:
    print(key)

for item in shopping_dict.items():
    print(item)

# key와 값을 따로 출력
for key, value in shopping_dict.items():
    print(key)
    print(value)
    print('-----')

menu = {'고구마':200, '떡볶이':600,"라면":800}
for key, value in menu.items():
    if value > 500:
        print("{} 메뉴는 추천하지 않습니다.".format(key))
    else:
        print("{} 메뉴는 추천합니다.".format(key))

# '토'는 몇 번?
# 반복자: 컬랙션, 문자열, range
lyric = """산토끼 토끼야. 어디를 가느냐. 깡충깡충 뛰면서. 어디를 가느냐. 
산고개 고개를. 나혼자 넘어서. 토실토실 알밤을. 주워 올 테야."""
count = 0
for txt in lyric:
    if txt == '토':
        count += 1
print(count)        

# 구구단: 3단
# range([시작값],[끝값],[증폭값]) 함수
# 시작값의 기본값:0
# 증감값의 기본값: 1 (증가 또는 감소)
# range(9)
for num in range(9):
    print('3 * {} = {}'.format(num + 1, (num + 1) * 3))

for num in range(1,10):
    print('3 * {} = {}'.format(num, num * 3))

# 공부 스케쥴
bookmark = 0
for day in range(20):
    print('[{}일차 공부계획]'.format(day+1))
    for s in range(5):
        print(" {}쪽 공부".format(bookmark+s+1))
    bookmark = bookmark + s + 1 

# 구구단 2단~9단
# 2단부터 9단까지 반복
for dan in range(2, 10):
    print(f"--- {dan}단 ---")
    # 각 단의 1부터 9까지 곱하기 반복
    for num in range(1, 10):
        print(f"{dan} x {num} = {dan * num}")
    print()  # 단이 끝날 때마다 한 줄 띄우기


# 상품 재고 관리 시스템
# 다음 기능을 모두 포함한 상품 재고 관리 시스템을 작성하시오.
'''
1. 초기 재고 설정: '사과': 50개, '바나나': 30개, '오렌지': 25개로 시작
2. 상품 관리 기능: 새 상품 추가(포도 40개 추가), 기존 상품 재고 수정, 상품 삭제
3. 재고 조회 기능: 전체 재고 현황 출력, 특정 상품 재고 확인, 재고 부족 상품 찾기(30개 미만)
4. 재고 변경 기능: 상품 판매 시재고 차감, 상품 입고 시 재고 증가, 재고 부족 시 경고 메시지
'''
# 출력 예시
'''
포도 재고 추가 완료
=== 현재 재고 현황 ===
사과: 50개
바나나: 30개
오렌지: 25개
포도: 40개
사과 재고: 50개
=== 재고 부족 상품 ===
오렌지: 25개(재고 부족)
사과 10개 판매 완료
사과 현재 재고: 40개
'''

# 상품 재고 관리 시스템
#1. 초기 재고 설정: '사과': 50개, '바나나': 30개, '오렌지': 25개로 시작
inventory = {
    '사과': 50,
    '바나나': 30,
    '오렌지': 25
}
# 새 상품 추가
#2. 상품 관리 기능: 새 상품 추가(포도 40개 추가), 기존 상품 재고 수정, 상품 삭제
inventory['포도'] = 40  #딕셔너리니까 키값으로 입력
print("포도 재고 추가 완료")

# 재고 현황 출력

print("=== 현재 재고 현황 ===")
for product, quantity in inventory.items():
    # print(f'문자열 {표현식}')
    print(f"{product}: {quantity}개")

# 특정 상품 재고 확인
product_name = "사과"
if product_name in inventory: # inventory안에 사과가 있는가(true)
    print(f"{product_name} 재고: {inventory[product_name]}개")
else:
    print(f"{product_name} 재고: 0개")

# 재고 부족 상품 찾기
#3. 재고 조회 기능: 전체 재고 현황 출력, 특정 상품 재고 확인, 재고 부족 상품 찾기(30개 미만)
print("=== 재고 부족 상품 ===")
for product, quantity in inventory.items():
    if quantity < 30:
        print(f"{product}: {quantity}개(재고 부족)")

# 상품 판매 시 재고 차감
product_name = "사과"
sale_cnt = 10
inventory[product_name] = inventory[product_name] - sale_cnt
print(f"{product_name} {sale_cnt}개 판매 완료")
print(f"{product_name} 현재 재고: {inventory[product_name]}개")
   

