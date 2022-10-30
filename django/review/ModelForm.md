# ModelForm

articles

models.py  ->  forms.py-> migrate -> urls.py -> views.py -> html

## models.py

Article

- title
- content
- created_at
- updated_at

Comment

- content
- created_at
- updated_at



## forms.py

- ArticleForm

- CommentForm

  

## urls.py

- index : main page
- create : to create function (C)
- detail : Nth article access (R)
- delete : Nth article deletion (D)
- update : Nth article edit (U)
- comment_create : write comment on Nth article
- comment_delete : from Nth article, delete Mth comment



## views.py

- index : main page
  - 모델에있는 객체 전부 저장하기
  - 딕셔너리 형태로 담기
  - `index.html`로 보내기
- create : to create function (C)
  - 로그인 해야 게시글 쓸 수있음
  - 요청 방식이 포스트일때, 포스트로 온 요청 담기
  -  타당성 검사 및 저장
  -  리다이렉트 작성한 게시글로
  - 포스트 방식이 아닐때
  - 에러 메세지 담기
  - create화면으로 돌려 보내기
- detail : Nth article access (R)
  - n번째 글 객체로 가져오기
  - 그 글에 작성된 모든 댓글 가져오기
  - 댓글 작성창 가져오기
  - 한번에 담아서 `detail.html`로 보내기
- delete : Nth article deletion (D)
  - 지우려하는 글 가져오기
  - 로그인 된 유저만 접근가능
  - 글의 작성자와 로그인된 유저가 같은지 확인, 다를경우 `detail.html`
  - 삭제 후 `index.html` 리다이렉트
- update : Nth article edit (U)
  - 수정할 글 가져오기
  - 글 작성자와 로그인한 유저가 같은지 확인, 다를경우 `detail.html`
  - 일치할 경우 post로 요청된 정보, 원래 개시글 정보를 한곳에 담기
  - 타당성 검사 후 통과하면  저장 하고 `detail.html` 리다이렉트
  - 타당성 검사 실패하면  `index.html` 
  -  그 외의 경우 `update.html`로 돌려 보내기
- comment_create : write comment on Nth article
  - 로그인된 유저만 접근가능
  - 댓글을 적을 게시글 정보 가져오기
  - POST방식으로 요청된 정보 폼에 담기
  - 폼이 타당하다면, 저장하기, `detail.html`로 보내기
  - 로그인 하지 않았다면 로그인 화면으로 보내기
- comment_delete : from Nth article, delete Mth comment
  - 로그인된 유저만 접근 가능
  - 지울 댓글 정보 가져오기
  - 작성자와 로그인 유저가 같다면, 삭제
  - `detail.html`로 보내기



## html

index

- CREATE 링크 - 로그인된 유저만 보이게
- 모든 게시글 로드하기 `for ... in`
  - 디테일 페이지 링크

detail

- n번째 글 로드하기
- 글 작성자와 로그인 유저 같을때 업데이트 버튼,
- 삭제버튼은 폼테그 안에 작성
- 인덱스페이지로 돌아가기 버튼
- 해당 글의 댓글 로딩 `for ... in `, 없을때 나타낼 글 보이기
- 로그인 된 유저라면, 댓글 작성창 띄우기, 그외의 경우 로그인화면으로 보내주는 링크 만들기

create

- 폼테그 안에 모델폼 불러오기
- 뒤로가기 만들기

update

- create와 똑같음, (원래 작성된 게시글 보이게)