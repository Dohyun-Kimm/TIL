import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView'
import LoginView from '@/views/LoginView'
import DogView from '@/views/DogView'
import NotFound404 from '@/views/NotFound404'

Vue.use(VueRouter)
const isLoggedIn =true

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView,
  },
  {
    path:'/login',
    name:'login',
    component: LoginView,
    beforeEnter(to,from,next){
      // 로그인이 되어있다면
      if (isLoggedIn === true){
        console.log('logged in');
        next({name:'home'})
      }else{
        next()
      }
    }       
  },
  {
    path:'/dog/:bread',
    name:'dog',
    component: DogView,
  },
  {
    path: '/404',
    name:'NotFound404',
    component:NotFound404
  },
  {
    path:'*',
    redirect:'/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to,from, next)=>{
  // console.log('to',to);
  // console.log('form',from);
  // console.log('next',next);

  // login 여부
  // const isLoggedIn =false

  // 로그인이 필요한페이지
  // const authPages =['hello', 'home', 'about']

  const allowAllPages = ['login']
  
  // const isAuthRequired = authPages.includes(to.name)
  const isAuthRequired = !allowAllPages.includes(to.name)

  
  if (isAuthRequired && !isLoggedIn){
    console.log('move to login ');
    next({name : 'login'})
  }else{
    console.log('to to');
    next()
  }

})

export default router
