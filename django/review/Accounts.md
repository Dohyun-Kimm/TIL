# Accounts

`admin.py`  -> `settings.py` ->  `models.py`  ->  `forms.py`  -> `urls.py`  -> `views.py`  - >`templates`

## admin.py

- 관리자를 사이트에 등록하기( 모델, 유저 어드민)

## settings.py

- 어스_유저_모델 = 

## models.py

- 유저모델 만들기 임포트해오기

## forms.py

- 유저생성폼,유저 변경폼 불러오기
- 커스텀 클래스 만들기
- 메타 클래스 만들기
  - 모델
  - 필드

## urls.py

- login
- logout
- signup
- delete
- update
- change_password



## views.py

- login 
  - 로그인이 되어있는 사람이라면 , 메인 페이지로 보내기
  - 요청이 POST라면, 폼에 POST형식으로 들어온 정보를 받기
    - 형식이 타당하면, 로그인시키고, 반환.
  - 그 외의 경우라면, 폼을  알맞는 형식에 담아. 렌더링 해주기
- logout
  - 로그인 된 사람이라면, 로그아웃 해주고 리다이렉트
- signup
  - 로그인된 상태라면, 메인 페이지로 돌려보내기
  - 포스트 방식으로 들어온 정보라면
    - 정보를 폼에 담고 타당성 검사
  - 통과하면, 정보저장 - > 로그인 
  - 리다이렉트 메인페이지
  - 그 외의 방식으로 요청이 오면, 폼 인스턴스 생성하고 회원가입페이지로 렌더링
- delete
  - 유저가 로그인 되어잇다면
    - 삭제
    - 로그아웃
- update
  - POST 방식으로 온 정보들
    - 폼에 담기 ( 원래 정보, 들어온 정보)
    - 폼이 타당하다면, 수정 -> 메인페이지로 리다이렉트
  - 그 외의방식이라면, 
    - 폼 인스턴스 만들고 내용 채워서, 회원정보 변경 페이지 렌더링
- change_password
  - post 방식일때 
    - 폼에 담기( 원래 정보, 들어온 정보)
    - 폼이 타당하면 수정, `update_session_auth_hash` 작성하기 (이유 확인하기)
    - 그렇지 않다면, 폼 생성해서 렌더링 해주기



## Templates

```html
{% extends 'base.html' %}

{% block content %}
  <h1>LOGIN</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
{% endblock content %}

```

각 페이지마다 알맞게 고치기.
