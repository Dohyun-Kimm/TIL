import Vue from 'vue'
import VueRouter from 'vue-router'

import IndexView from '../views/IndexView.vue'
// createView 컴포넌트 등록하기 
import CreateView from '../views/CreateView'

Vue.use(VueRouter)

// django의 urls.py와 역할이 비슷함
const routes = [
  {
    path:'/',
    name:'index',
    component: IndexView
  },
  // createView.vue로 가는 루트 등록하기
  {
    path:'/create',
    name:'create',
    // createView.vue 에서 정한 컴포넌트 name 여기에 등록
    component: CreateView
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
