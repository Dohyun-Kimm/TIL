<template>
  <div>
    <!-- C1. enter 누르면 crateTodo 실행 -->
    <input 
      type="text"
      v-model = "todoTitle"
      @keyup.enter="createTodo"
    >
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function(){
    return {
      todoTitle: null,
    }
  },
  methods: {
    // C2. 부모 component에 emit 보냄. todoTitle 보내고, null로 초기화.
    createTodo: function() {
      // C3. 부모 component에 create-todo 트리거 내용물은 todoTitle
      this.$emit('create-todo',this.todoTitle)
      this.todoTitle = null
    }
  }
}
</script>

<style>

</style>