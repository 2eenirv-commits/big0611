# 제어문
# 조건문
'''
탭키과 스페이스바를 섞어쓰면x
4칸 스페이스바
들여쓰기(indent)
if 조건식:
    수행문1

if 조건식:
    수행문1
else
    수행문2            

조건식은 결과가 true 또는 false
비교(> < >= <= == !=), 논리(and, or, not) 연산의 결과는 true 또는 false    
'''

today_temp = -30
if today_temp > 0:
    print("아이스 아메리카노")
#IndentationError: expected an indented block after 'if' statement on line 20

today_temp = -10
if today_temp > 0:
    print("아이스 아메리카도")
else:
    print("따뜻한 아메리카노")   

'''
if 조건식1:
    수행문1
elif 조건식2:
    수행문2    
...    
else: 
    수행문3    
'''
today_temp = -10
if today_temp > 0:
    print("아아")     
elif today_temp == 0:
    print("미아")
else:
    print("뜨아")    

# 중첩 if
weather = '맑음'    
today_temp = 30

if weather == '맑음':
    if today_temp > 0:
        print("아아")     
    elif today_temp == 0:
        print("미아")
    else:
        print("뜨아")  
else:
    print('먹지마!')

math_score = 80
eng_score = 100

if eng_score >= 90 and math_score >= 90:
    print('오예! 용돈 인상')
elif eng_score <= 80 and math_score <= 80:
    print('용돈 삭감ㅠㅠ')    
else:
    print('동결')    


math_score = 80
eng_score = 100

if eng_score >= 90 or math_score >= 90:
    print('오예! 용돈 인상')
elif eng_score <= 80 or math_score <= 80:
    print('용돈 삭감ㅠㅠ')    
else:
    print('동결')    


