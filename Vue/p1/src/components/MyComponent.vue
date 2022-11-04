<template>
  <div>
    <h1>THis is my Component</h1>
    <MyChild 
      static-props="component to child"
      :dynamic-props="dynamicProps"
      />
    
  </div>
</template>

<script>
import MyChild from '@/components/MyChild'

export default {
  name : "MyComponent",
  components:{
    MyChild,    
  },
  data : function(){
    return {
      dynamicProps : "it's in data"
    }
  }
}
</script>

<style>

</style>