# TEST CODE, STILL WRITING

import pdfkit # 웹 페이지를 PDF 파일로 바꿔 주는 모듈을 불러옴

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe' # wkhtmltopdf가 설치된 경로를 지정함(환경변수 설정하기 귀찮음)
config = pdfkit.configuration(wkhtmltopdf = path_wkhtmltopdf)

pdfkit.from_url('https://gall.dcinside.com/mgallery/board/view/?id=elsa&no=1', 'sample.pdf', configuration = config) # URL을 통해 접속한 웹 페이지를 PDF로 저장함
