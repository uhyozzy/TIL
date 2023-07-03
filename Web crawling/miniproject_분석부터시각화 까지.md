# 2.1.1 유튜브 랭킹 데이터 수집하기 
```python
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# webdriver로 크롬 브라우저 실행하기

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url="https://youtube-rank.com/board/bbs/board.php?bo_table=youtube"
driver.get(url)

# 페이지 정보 가져오기
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

# BeautifulSoup로 tr 태그 추출하기
channel_list=soup.select('tr')
print(len(channel_list), '\n')
print(channel_list[0])

# tr태그 확인하기
channel_list = soup.select('form > table > tbody > tr')
print(len(channel_list))

# 채널태그 출력 및 태그 구조 확인하기 
channel = channel_list[0]
print(channel)

# 카테고리 정보 추출하기
category = channel.select('p.category')[0].text.strip()
print(category)

# 채널명 찾아오기
title = channel.select('h1 > a')[0].text.strip()
print(title)

# 구독자 수, view 수, 동영상 수 추출하기
subscriber = channel.select('.subscriber_cnt')[0].text
view = channel.select('.view_cnt')[0].text
video = channel.select('.video_cnt')[0].text

print(subscriber)
print(view)
print(video)

channel_list = soup.select('tbody>tr')
for channel in channel_list:
    title = channel.select('h1>a')[0].text.strip()
    category = channel.select('p.category')[0].text.strip()
    subscriber = channel.select('.subscriber_cnt')[0].text
    view = channel.select('.view_cnt')[0].text
    video = channel.select('.video_cnt')[0].text
    print(title, category, subscriber, view, video)

# 페이지별 URL 만들기
page = 1
url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={}'.format(page)
print(url)

# 반복문으로 유튜브 랭킹 화면의 여러 페이지를 크롤링하기
results = []
for page in range(1,11):
    url=f"https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={page}"
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    channel_list = soup.select('form > table > tbody > tr')
    for channel in channel_list:
        title = channel.select('h1>a')[0].text.strip()
        category = channel.select('p.category')[0].text.strip()
        subscriber = channel.select('.subscriber_cnt')[0].text
        view = channel.select('.view_cnt')[0].text
        video = channel.select('.video_cnt')[0].text
        data = [title, category, subscriber, view, video]
        results.append(data)

# 데이터 칼럼명을 설정하고 엑셀 파일로 저장하기
import os
if not os.path.exists('files'):
    os.makedirs('files')

df = pd.DataFrame(results)
df.columns = ['title', 'category', 'subscriber', 'view', 'video']
df.to_excel('./files/youtube_rank.xlsx', index=False)
```

# 2.1.2 유튜브 랭킹 데이터 시각화 하기
```python

# 라이브러리 추가하기
import pandas as pd
import matplotlib.pyplot as plt

# 그래프에서 한글을 표기하기 위한 글꼴 변경(윈도우, macOS에 대해 각각 처리)
from matplotlib import font_manager, rc
import platform
if platform.system() == 'Windows':
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family = font_name)
elif platform.system() == 'Darwin':
    rc('font', family = 'AppleGothic')
else:
    print('Check your OS system')

# 엑셀 파일 불러오기
df = pd.read_excel('./files/youtube_rank.xlsx')
df.head()

# 데이터 살펴보기
df.tail()

# 데이터 살펴보기
df['subscriber'][0:10]

# 데이터 살펴보기
df['subscriber'].str.replace('만','0000')[0:10]

# replaced_subscriber 시리즈 문자열 변경하기
df['replaced_subscriber'] = df['subscriber'].str.replace('만', '0000')
df.head()

# 데이터 상세정보
df.info()

# Serires 데이터 타입 변환하기
df['replaced_subscriber']=df['replaced_subscriber'].astype('int')
df.info()

# 카테고리별 구독자 수, 채널 수 피봇 테이블 생성하기
pivot_df = df.pivot_table(index='category', values = 'replaced_subscriber', aggfunc=['sum','count'])
pivot_df.head()

# 데이터프레임의 컬럼명 변경하기
pivot_df.columns = ['subscriber_sum','category_count']
pivot_df.head()

# 데이터프레임의 인덱스 초기화하기
pivot_df = pivot_df.reset_index()
pivot_df.head()

# 데이터프레임을 내림차순 정렬하기
pivot_df = pivot_df.sort_values(by='subscriber_sum', ascending=False)
pivot_df.head()

plt.figure(figsize=(30,10))
plt.pie(pivot_df['subscriber_sum'], labels=pivot_df['category'], autopct='%1.1f%%')
plt.show()
```
