import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
music_info = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for music in music_info:
    title = music.select('td.info > a.title.ellipsis')
    if len(title) > 0:
        print(title[0].text.strip())
    number = music.select('td.number')
    if len(number) > 0:
        print(number[0].text.strip())
    artists = music.select('td.info > a.artist.ellipsis')
    if len(artists) > 0:
        print(artists[0].text.strip())
#############################
# (입맛에 맞게 코딩)
#############################
# 순위 / 곡제목 / 가