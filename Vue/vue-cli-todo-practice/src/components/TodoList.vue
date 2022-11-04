<template>
  <div>
    <p>Todo list</p>
    <ul >
      <!-- P3 모든 리스트를 for문을 통해 나열. 개별 값은 dynamic props로 :todo   -->
    <TodoListItem v-for="(todo,index) in todos" :key="index" :todo="todo" @delete-todo="deleteTodo"/>
    </ul>

  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'
export default {
  name: 'TodoList',
  components:{
    TodoListItem,
  },
  // P2. App 에서 props 된 todos가 여기옴
  props:{
    todos: Array,
  },
  // D1
  methods:{
    deleteTodo: function(todo){
      this.$emit('delete-todo',todo)
    }
  }
}
</script>

<style>

</style>