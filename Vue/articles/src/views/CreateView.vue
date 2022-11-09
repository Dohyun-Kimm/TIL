<template>
<!-- create1.  컴포넌트 작성하기 div 태그만 만들기 -->
  <div>
    <h1>게시글 작성</h1>
    <!-- create 2. 게시글 작성에 필요한 양식 작성하기 -->
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <!-- v-model을 통해 script와 바인딩 입력 값이 title에 저장됨-->
      <input type="text" id="title" v-model.trim='title'><br>
      <label for="content">내용:</label>
      <!-- content에 저장되도록 바인딩 -->
      <textarea 
        id="content" cols="30" rows="10"
        v-model.trim="content" 
        ></textarea><br>
        <!-- 섭밋 누르면 위으ㅔ 양식 전송 -->
      <input type="submit">
    </form>
    <router-link :to="{ name:'index'}"> 뒤로가기</router-link>
  </div>
</template>

<script>
// crate 1. 이름 등록하기 (파일명과 똑같이) router에 등록될 component기 때문에
//router/index로 ㄱㄱ
export default {
  name: 'CreateView',
  // 입력될 데이터들의 초기 값과 데이터 이름을 정해줌 여기서는 title, content라는 필드가 있음
  data(){
    return {
      title: null,
      content: null,
    }
  },
  // 입력 된 내용을 하나의 객체 payload에 담아서 전달
  methods:{
    createArticle(){
      const title = this.title
      const content =this.content
      if(!title){
        alert('제목 입력')
      }else if(!content){
        alert('내용 입력')
      }else{
        const payload ={
          title, content
        }
        // actions 호출하는 매서드 dispatch
        this.$store.dispatch('createArticle', payload)
        // 라우터 에서 인덱스 보여지도록 푸시하기
        this.$router.push({ name:'index'})
      }
    }
  }
}
</script>

<style>

</style>