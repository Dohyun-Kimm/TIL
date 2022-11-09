# Vue Router (day 8)



## UX & UI

### UX(User Experience)

유저가 느끼는 느낌, 태도, 행동 디자인

데이터 기반으로 유저를 조사하고 분석해서 개발자 디자이너가 이해할 수 있게 소통

유저 리서치, 데이터 설계 및 정제, 시나리오, 프로토타입 설계

### UI

유저에게 보여지는 화면 디자인

**Interface**: 사용자가 쉽게 사용 할 수있게 디자인 하는 것

통일된 디자인 시스템,  소통을 위한 프로토 타입 , 중간 산출물 필요



UX/UI : https://cantunsee.space/

**HCI** : 인간, 컴퓨터 사이의 상호작용

애플 디자인 원칙 :https://developer.apple.com/kr/design/tips/



## Prototyping

software prototyping: 애플리케이션 프로토타입 

FIGMA





## Routing

라우팅: 네트워크에서 경로를 선택 하는 프로세스

Routing in SSR 서버가 모든 라우팅을 통제. 장고로 보낸 요청의 응답 HTML은 완성본인 상태.

SPA -CSR 방식 

- 서버느 하나의 HTML만 제공 URL하나만 가짐
- 페이지 간 이동이 없음, 비동기 방식으로 처리

라우팅이 없다면

브라우저의 뒤로 가기 기능을 활용 할 수 없음

유저가 페이지의 변화를 감지할 수 없음

**Vue Router**

SPA 지만 MPA처럼 사용.

` vue create pjrname`

`cd pjrname`

`vue add router`



