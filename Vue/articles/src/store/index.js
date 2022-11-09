import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    article_id:3,
    articles:[
      {
      id:1,
      title: 'title',
      content:'content',
      createdAt:new Date().getTime()
      },
      
      {
      id:2,
      title: 'title2',
      content:'content2',
      createdAt:new Date().getTime()
      },
      
    ]
  },
  getters: {
  },
  mutations: {
    // actions의 commit으로 인해 호출됨.
    // actions의 createArticle에서 만들어진 객체 Article을 인자로 받음
    CREATE_ARTICLE(state, article){
      // state에 데이터 추가하는 push 매서드에 article 담아서 보내기
      state.articles.push(article)
      // id 값은 따로 관리 추가되는 글을 위해 id +1해놓기
      state.article_id= state.article_id +1
    },

  },
  // dispatch로 호출되면 actions 안에 있는 createArticle 실행
  actions: {
    // 전달 받은 값인 payload 인자로 받고
    createArticle(context, payload){
      console.log('actions');
      // article이라는 객체 안에 받은 정보 넣기
      // id 값을 별개로 자동으로 부여 
      const article = {
        id: context.state.article_id,
        title: payload.title,
        content: payload.content,
        // DB를 사용하는 것이 아니기때문에 게속 시간이 업데이트된다.
        createdAt: new Date().getTime(),
      }
      // Mutation을 호출하는 매서드 commit
      context.commit('CREATE_ARTICLE', article)
    }
  },
  modules: {
  }
})
