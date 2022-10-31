# Vue day 1

어우 졸려

- 상대적으로  낮은 진입장벽이 낮음.
-  구조가 직관적임.
- 다른 프레임워크 배우기 쉬워짐.
- React 크게 다르지 않음.



## Vue CDN

- 뷰로 작업 하기위해 필요함
- 

## Why Vue

- 변경 사항 한번에 관리가능

- 안정적인 측면에서 vue2 > vue3



## MVVM Pattern

Model, View, View-Model

Model -  real data

View - visible part DOM

view-Model = view와 binding되어 Action 주고받음. 연결고리 

MVC에서 controller가 빠지고 ViewModel

view, model은 서로 독립적이다. 서로 의존성이 낮다. 직접 소통할 수 없다.



### 생성자 함수

동일한 구조의 객체를 여러개 만들떄 사용

함수이름 대문자로 시작

`new` 연산자 사용

### el(element)

vue instance와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음

### data

데이터 객체는 반드식 기본객체여야함

interpolation을 통해 view에 렌더링 가능

`this.message`를 통해 접근 가능함.

### methods

`s`  있어야함.

### ArrowFunction

`arrowfunction`의 `this`가 상위 스코프를 가리킴 (window)

-> 매서드를 **정의 할때**, Arrow Function 사용하면 안됨.

매서드안에서는 써도됨. 거기서 상위 스코프는 객체를 가리킴.



# Basic Syntex

interpolation : 가장 기본적인 바인딩. 

```html
<div id="app">
	<p>{{ 데이터 이름}}</p>
</div>

<scripts>
생성자 선언
  const app = new Vue({
  	el : '#app', vue 내용을 html에 적용시키기위한태그 
  	data: {
  	  데이터 이름 :'interpolation',
  	}
  })
</scripts>
```







### v-text

```
<div id="app">
	<p>{{ message }}</p>
    <p v-text='message'></p>
</div>

<script>
  const app2 = new Vue({
  	el : '#app2',
  	data : {
  		message: 'hello',
  	}
  })
</script>

==> 둘다 같은 값 나옴

```

### v-html

RAW HTML 표현하는 방법

 `v-html`을 사용하여 data와 바인딩

vue 함수 안에서 html 문법을 따른 코드를 전달 해주는 directive

사용자가 입력하거나 제공하는 컨텐츠에는 사용하면 안됨 **(XSS공격)**

```
<div id="app2">
  <p v-html='html'></p>
</div>

<script>
  const app2 = new Vue({
  	el : '#app2',
  	data : {
  		html : <a href = 'google.com'> Google </a>
    }
  })
</script>
```

### v-show

