<template>
  <div id="app">    
    <!-- TodoList라는 자식component에 todos 동적 props보내기 delete-todo -->
    <TodoList :todos="todos" @delete-todo="deleteTodo"/>
    <!-- C4. @ emit받기 createTodo 함수실행 -->
    <TodoForm @create-todo="createTodo"/>
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'
export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  data : function() {
    return {
      // props 할 데이터 형식이 리스트
      todos:[]
    }
  },
  methods: {
    // C5. createTodo 메소드 실행 되면서
    createTodo : function(todoTitle){
       // C6. todo에  키는 title value는 todoTitle인 객체 생성
      const todo ={
        title: todoTitle
      }
      // C7. todo라는 객체를 vue 객체 안에 있는 todos에 추가하기
      // todoList의 todos에 값이 저장되고 props 된다.
      this.todos.push(todo)
    },
    // deleteTodo
    deleteTodo: function(todo){
      const index = this.todos.indexOf(todo)
      this.todos.splice(index,1)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
