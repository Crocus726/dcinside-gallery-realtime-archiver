import time
import requests
from bs4 import BeautifulSoup
import pdfkit # 웹 페이지를 PDF 파일로 바꿔 주는 모듈을 불러옴

gall_id = input("갤러리의 ID를 입력해주세요: ") # 갤러리 ID를 입력받음

# Web 접속 시 필요한 사용자 에이전트를 지정함
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

default_link = 'https://gall.dcinside.com/board/' # 갤러리 기본 URL을 지정함

req = requests.get(default_link + 'lists/?id=' + gall_id, headers = headers) # 갤러리 메인 페이지에 GET 요청을 보냄

# 정식 갤러리, 마이너 갤러리 구분(URL 적을 때 필요함)
if 'location.replace' in req.text:
    default_link = default_link.replace('board/', 'mgallery/board/') # 갤러리 기본 URL을 마이너 갤러리용으로 변경함
    print("마이너 갤러리로 인식되었습니다.")
elif req.status_code == 200:
    print("정식(메이저) 갤러리로 인식되었습니다.")
else:
    print("해당 갤러리를 찾을 수 없습니다.")
    exit()

start_num = int(input("PDF 변환을 시작할 글 번호를 입력해주세요: ")) # PDF 변환을 시작할 글 번호를 입력받음
now_num = start_num - 1 # 현재 PDF 변환이 진행 중인 글 번호를 설정함

# wkhtmltopdf가 설치된 경로를 지정함(환경변수 설정 대체)
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf = path_wkhtmltopdf)

while True:
    time.sleep(5)

    req = requests.get(default_link + 'lists/?id=' + gall_id + '&list_num=30', headers = headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    gall_num_tags = soup.find_all(attrs = {'class': 'gall_num'}) # class가 'gall_num'인 태그를 찾아서 저장함
    
    # 이벤트, 공지, 최신 글의 글 번호를 배열에 담음
    gall_num_array = []
    for tag in gall_num_tags:
        gall_num_array.append(int(tag.get_text()))
    gall_num_array.sort() # 오름차순 정렬

    # 가장 최신 글 번호를 확인하고, 현재 PDF 변환이 진행 중인 글 번호보다 크면 PDF 변환을 시작함
    recent_num = gall_num_array[-1]
    if(recent_num > now_num):
        for num in range(recent_num - now_num):
            try:
                pdfkit.from_url(default_link + 'view/?id=' + gall_id + '&no=' + str(now_num + 1), gall_id + '_' + str(now_num + 1) + '.pdf', configuration = config) # URL을 통해 접속한 웹 페이지를 PDF로 저장함
            except: # Qt 폰트 관련 오류가 항상 발생하는데 그냥 무시함
                pass
            print(str(now_num + 1) + '번째 게시글을 저장했습니다.')
            now_num += 1
