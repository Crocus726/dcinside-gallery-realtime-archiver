# TEST CODE, STILL WRITING
import requests
import time
from bs4 import BeautifulSoup
import pdfkit # 웹 페이지를 PDF 파일로 바꿔 주는 모듈을 불러옴

# Web 접속 시 필요한 사용자 에이전트를 지정함
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

gall_id = input("갤러리의 ID를 입력해주세요: ") # 갤러리 ID를 입력받음(예: )

default_link = 'https://gall.dcinside.com/board/lists/?id='

req = requests.get(default_link + gall_id, headers = headers)

print(req.status_code)

# 정갤 마갤 구분(URL 적을 때 필요함)
if 'location.replace' in req.text:
    default_link = default_link.replace('board/', 'mgallery/board/') # 갤러리 URL을 변경함
    gall_type = 'minor'
    print("마이너 갤러리로 인식되었습니다.")
elif req.status_code == 200:
    gall_type = 'major'
    print("정식(메이저) 갤러리로 인식되었습니다.")
else:
    print("해당 갤러리를 찾을 수 없습니다.")
    exit()

start_num = int(input("아카이빙을 시작할 글 번호를 입력해주세요: "))

now_num = start_num - 1

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe' # wkhtmltopdf가 설치된 경로를 지정함(환경변수 설정하기 귀찮음)
config = pdfkit.configuration(wkhtmltopdf = path_wkhtmltopdf)

# 프로그램을 종료할 때까지 계속 반복함
while True:
    time.sleep(1) # 실행 전 1초 지연

    req = requests.get(default_link + gall_id, headers = headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    gall_num_tags = soup.find_all(attrs = {'class': 'gall_num'}) # class가 'gall_num'인 태그 찾아서 gall_num_tags에 저장함
    gall_num_array = []
    
    #
    for tag in gall_num_tags:
        gall_num_array.append(int(tag.get_text()))
    
    gall_num_array.sort()
    recent_num = gall_num_array[-1]

    if(recent_num > now_num):
        for i in range(recent_num - now_num):
            pdfkit.from_url('https://gall.dcinside.com/mgallery/board/view/?id=elsa&no=' + 번호, 'sample.pdf', configuration = config) # URL을 통해 접속한 웹 페이지를 PDF로 저장함
