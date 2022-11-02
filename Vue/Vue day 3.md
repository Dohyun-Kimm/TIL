# Vue CLI

CLI : command line interface

프로젝트 구성을 도와주는 역할

다양한 툴 제공

### Vue CLI Quck Start

`vue create vue-cli` : 뷰 프로젝트 생성하기

`cd vue-cli` : 한단계 들어가야 서버를 실행 할 수 있음.

`npm run serve` 서버 실행하기



프로젝트 생성과 동시에 `git init`이 되어있음.

TIL에 반영하려면 vue안에 있는 git을 지워 주어야함.



`node_modules`에 모든 모듈이 들어있음. 가상환경을 만들 필요가 없다.

각각의 모듈은 서로 의존적임. 

git에 올리지 않기



**Babel**

ES6+ 코드를 구버전으로 번역하는 javascript Compiler

**Webpack**

static module **bundler**

모듈간의 의존성 문제를 해결하기위한 도구

내부적으로 종속성 그래프 작성



## SFC

component

UI를 독립적이고 재사용 가늫난 조각으로 나눈것

다시 사용할숭 있는 범용성



------

`vue-cli`  -> `component` 에 `vue`파일 만들기

프로젝트 풀 받은 경우 : `npm install`

`script` ,> `export` -> `name:` 등록

`template`에 최상위 태그 추가



불러오기 , 등록하기,  보여주기