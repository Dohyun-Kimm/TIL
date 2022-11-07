# VUEX

상태관리 (stage management)

component는 각각의 상태를 가짐. 앱을 구성하기 위해 component들이 같은상태를 유지해야함.

상태 관리 필요



### Vuex = Centralized Store

모든 component들이 중앙 저장소를 사용

vue의 반응성을 효율적으로 사용하는 상태관리 기능 제공

state management pattern + library

## vuex project

`vue create vue-app` -> `cd vue-app`

`vue add vuex`

1. state

   `index.js` . state:{ 데이터 정의}

   ```js
   state : {
   	message : 'message in state',
   }
   ```

   

   `app.vue`. template에서 state 사용 `computed`에 정의 후 접근.

   ```vue
   <template>
     <div id="app">
       <!-- <h1>{{$store.state.message}}</h1> -->
       <h1> {{ message }}</h1>    
     </div>  
   </template>
   
   <script>
       export default {
         name: 'App',  
           // computed 에 state message 정의하기
         computed:{
           message(){
             return this.$store.state.message
           },
   </script>
   ```

   

   

2. mutations

   - 실제로 state를 변경하는 방법 (유일함)
   - mutations action에서 호출되는 함수를 handler라고 함. 반드시 동기적. state의 변화의 시기를 특정할 수 없기 때문

3.  Actions

   - mutaion과 비슷하지만, 비동기 작업이 포함 될 수 있음.
   - 직접 state변경하지 않고 commit으로 mutation 호출 해서 state변경
   - mutation이 하지 않는 모든일을 함.
   - dispatch() 매서드에 의해 호출됨

   ```
   구현순서
   1. actions에 정의된 changeMesage 함수에 데이터 전달
   2. component에서 actions는 dispatch()에 의해 호출됨.
   ```

   

4.  Getters

   - vue 인스턴스의 computed와 동일
   - 



## Lifecycle Hooks

각 vue

- created
  - vue instance 생성 직후 호출
  - data comuted 설정이 완료된 상태
  - 서버에서 받은 데이터를 vue instance의 데이터에 할당하는 로직 구현하기 적합.
  - mount되지 않아 요소에 접근 할 수 없음. DOM요소에 접근 x
  - 
- 