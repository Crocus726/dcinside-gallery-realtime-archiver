# 디시인사이드 갤러리 실시간 PDF 변환기
디시인사이드 갤러리의 게시글을 PDF로 변환하여 컴퓨터에 저장하는 Python 코드입니다. 갤러리 ID와 PDF 변환을 시작할 글 번호를 입력하면 해당 번호의 글부터 오래된 순으로 PDF 변환을 진행하고, 새로운 게시글이 있는지 계속 모니터링하여 PDF 변환을 진행합니다.

## 확인된 작동 환경
* Python 3.11.3
* wkhtmltopdf 0.12.6

## 사용 설명
갤러리 ID와 글 번호는 해당 갤러리의 게시글 URL(PC 버전으로 접속)을 통해 알 수 있습니다.  
`https://gall.dcinside.com/mgallery/board/view/?id={갤러리 ID}&no={글 번호}`
최신 글 번호를 확인하기 위한 새로고침 빈도는 5초당 1회로 설정되어 있습니다. PDF 변환에 소요되는 시간은 5~6초 내외이며, 서버 환경에 따라 최대 10분까지도 소요될 수 있습니다. PDF 파일 하나당 크기는 평균 400~500 KB입니다.

## 주의 사항
본 Python 코드는 새로운 게시글이 있는지 계속 모니터링하는 기능이 있어 특정 주기로 웹 페이지에 요청을 보내는 코드가 포함되어 있습니다. 웹 페이지에 요청을 보내는 주기를 너무 짧게 수정하여 코드를 실행할 경우 서버로부터 IP 접속 차단 등의 조치를 받을 수 있습니다.  
음란 또는 혐오 이미지 게시자 형사 소송에 활용하는 등의 공익적인 목적으로만 사용하기를 권장합니다.
