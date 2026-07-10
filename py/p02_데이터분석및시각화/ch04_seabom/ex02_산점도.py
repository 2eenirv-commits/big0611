# 산점도(scatterplot)
# - 연속형 변수 간의 상관관계 분석
# - 데이터 포인트가 많은 경우(50개 이상)
# - 이상치나 패턴 감지
# - 다중 변수의 관계를 색상, 크기, 모양으로 표현할 때
## tips 데이터를 활용한 산점도 실습

#%%
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("tips")


# 1. (기본 산점도) 음식가격과 팁의 상관관계
# sns.scatterplot(x,y)
#%%
sns.scatterplot(x=df['total_bill'], y=df['tip'])
plt.show()

# 2. 색상을 활용한 그룹별 분석
#sns.scatterplot(data=df, x='total_bill', y='tip', hue='sex')
#  hue: 범주형 변수를 지정해서 색상으로 구분 -> 범례
sns.scatterplot(x=df['total_bill'], y=df['tip'], hue=df['sex'])
plt.show()

# 3. (버블차트)크기를 활용한 3차원 정보 표현
# size: 크기를 지정하여 원의 크기로 표현 -> 크기 범례
sns.scatterplot(x=df['total_bill'], y=df['tip'], hue=df['sex'], size=df['size'])
plt.show()

# 4. 다차원 시각화
# 4개의 변수를 동시에 표현
sns.scatterplot(x=df['total_bill'], y=df['tip'],
                hue=df['sex'],     # 색상으로 성별 구분
                size=df['size'],   # 크기로 인원수 표현
                style=df['time'],  # 모양으로 시간대 구분
                alpha=0.7)         # 투명도 조절
plt.show()

 # 막대 그래프
#  - 카테고리별 수치 비교
#  - 데이터 포인트가 적은 경우(20개 미만)
#  - 정확한 수치 값을 강조하고 싶을 때
#  - 순위나 크기 순서를 명확히 보여주고 싶을 때

# 막대 그래프
x= [1,2,3,4,5]
y= [10,20,25,30,42]
sns.scatterplot(x=x, y=y)
plt.show()

sns.barplot(x=x, y=y)
plt.show()
