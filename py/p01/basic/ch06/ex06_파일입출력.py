# 파일 입력

# 파일 모드
'''
open('파일명', '파일모드')
close()

r(read): 읽기 -> read()
w(write): 쓰기 ->  write(), 덮어 씌운다.
a(append): 추가 -> write()
'''
f = open('abc1.txt', 'w')
f.write('A B C D E F G')
f.close()

f = open("abc2.txt", "w")
f.write("a b c d e f g ")
f.close()

f = open("abc1.txt", "a")
f.write("H I J K L M N O P Q R S T U V W X Y Z")
f.close()

# 파일 출력: 파일 내용 읽기
# read(): 글자 1자씩 읽기
f = open('abc1.txt', 'r')
print(f.read())
f.close()

# readlines(): 한 줄씩 읽기
f = open("abc2.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()    

# with 문: close() 자동 처리 -> 일반적 실무작업때 사용
'''
with open('파일명', '파일모드', encoding='utf-8') as 별칭(변수):
    별칭.write()
    별칭.read()
'''
# 윈도우 기본값: encoding='cp949' (윈도우)
with open('일기.txt', 'w', encoding='utf8') as f:
    f.write('2026년 6월 22일 월요일\n')

with open('일기.txt', 'a', encoding='utf-8') as f:
    f.write('대체로 흐림')    

with open('일기.txt', 'r', encoding='utf-8') as f:
    print(f.read())