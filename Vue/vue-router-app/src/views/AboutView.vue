<template>
  <div class="about">
    <h1>This is an about page</h1>
    <input type="text" @keyup.enter="toHello" v-model="inputData">
    <router-link :to="{name:'home'}"> 홈으로 </router-link>
    <button @click='toHome'>호믕로!</button>

  </div>
</template>

<script>


export default {
  name:'AboutView',
  data(){
    return{
      inputData : null
    }
  },
  methods:{
    toHome(){
      this.$router.push({ name:'home'})
    },
    toHello(){
      this.$router.push({ name: 'hello', params:{ userName: this.inputData }})
    }
  }
}
</script>
