# TEST CODE, STILL WRITING
import requests
import pdfkit # 웹 페이지를 PDF 파일로 바꿔 주는 모듈을 불러옴

headers = {
    'User-Agent': '유저 에이전트 적기'
}

gall_id = input("갤러리의 ID를 입력해주세요: ")

req = requests.get('https://gall.dcinside.com/board/lists/?id=' + gall_id, headers = headers).text

# 정갤 마갤 구분(URL 적을 때 필요함)
if(마갤이면):
    gall_type = 'major'
elif(정갤이면):
    gall_type = 'minor'

start_num = int(input("아카이빙을 시작할 글 번호를 입력해주세요: "))

now_num = start_num - 1

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe' # wkhtmltopdf가 설치된 경로를 지정함(환경변수 설정하기 귀찮음)
config = pdfkit.configuration(wkhtmltopdf = path_wkhtmltopdf)

while True:
    recent_num = (가장 최신 게시글 번호)

    if(recent_num > now_num):
        for i in range(recent_num - now_num):
            pdfkit.from_url('https://gall.dcinside.com/mgallery/board/view/?id=elsa&no=1', 'sample.pdf', configuration = config) # URL을 통해 접속한 웹 페이지를 PDF로 저장함
