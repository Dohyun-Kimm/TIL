import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store',
  },
  getters: {
    messageLength(state){
      return state.message.length
    },
    doubleLength(state, getters){
      return getters.messageLength *2
    }
  },
  mutations: {
    CHANGE_MESSAGE(state, newMessage){
      console.log(state);
      console.log(newMessage);
      // 입력 한 값으로 state의 message 값이 변경됨.
      state.message = newMessage
    }
  },
  actions: {
    //context - export default 전체를 갖는 객체
    // changeMessage(context, newMessage){
      //   console.log(context);
      //   console.log(newMessage);
      // }

    // mutaions 호출
    changeMessage(context, newMessage){
      // context.commit('mutation 호출', 추가 데이터)
      context.commit('CHANGE_MESSAGE',newMessage)
    }
  },
  modules: {
  }
})
