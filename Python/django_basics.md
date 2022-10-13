```python
python -m venv venv		# virtual environment folder creatioin
source venv/Scripts/activate # 가상환경안에 스크립트 안에 실행
deactivate # 가상환경 종료
pip install django==3.2.13 	# 장고설치
pip list 		# 가상환경이 실행된 상태라면, 가상환경에 설치된 것들 목록보여줌
pip freeze > requirements.txt # 나중에 이파일 실행시키면 이 내부에 있는 파일들 자동설치
pip install -r requirements.txt # 위에말한거 실행시키는 코드
django-admin startproject firstpjt . # 프로젝트 생성. '.' 찍어주면 지금 디렉토리에 생성
python manage.py runserver # 가상환경실행 시키기???
python manage.py startapp articles # 가상환경이 꺼진 상태에서 해야함

```

