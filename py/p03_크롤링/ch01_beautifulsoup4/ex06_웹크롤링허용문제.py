from urllib.robotparser import RobotFileParser

# 웹 크롤링 허용문제
# robots.txt는 크롤링하는 데 필요한 규칙을 정리해 놓은 페이지이다.
# https://www.google.com/robots.txt


rp = RobotFileParser()
# 확인하려는 사이트의 robots.txt 주소 입력
rp.set_url("https://www.google.com/robots.txt")
rp.read()

# 내 크롤러봇(*)이 특정 URL을 긁어도 되는지 확인 (True/False 반환)
can_fetch = rp.can_fetch("*", "https://www.naver.com/main/home.naver")
print("크롤링 가능 여부:", can_fetch)