from bs4 import BeautifulSoup

html_doc = """
<!doctype html>
<html>
    <head>
        <title>기초 웹 크롤링</title>
    </head>
    <body>
        <div> 첫 번째 부분 </div>
        <div> 두 번째 부분 </div>
    </body>
</html>
"""


soup = BeautifulSoup(html_doc, 'html.parser')
body = soup.find("body")
# print(body)

div1 = soup.find("div")
# print(div1)
# soup.find_all("선택자") -> 리스트로 리턴(인덱스 번호를 갖는다.)
div_total = soup.find_all("div")
# print(div_total)

div2 = div_total[1]
#print(div2)
print(div2.text)



