import Vue from 'vue'
import VueRouter from 'vue-router'

import Layout from '../layout/index'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    // route level code-splitting
    // this generates a separate chunk (first.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "first" */ '../views/Login.vue')
  },
  {
    path: '/',
    component: Layout,
    redirect: '/home',
    name: 'Layout',
    children: [
      {
        path: 'home',
        component: (resolve) => require(['@/views/Home'], resolve),
        name: 'Home',
        meta: { title: '康复计划管理', icon: 'index', affix: true, noCache: true }
      },
      {
        path: 'temp',
        component: (resolve) => require(['@/views/Temp'], resolve),
        name: 'Temp',
        meta: { title: '康复知识库', icon: 'index', affix: false, noCache: true }
      },
      {
        path: 'track',
        component: (resolve) => require(['@/views/Track'], resolve),
        name: 'Track',
        meta: { title: '进度跟踪', icon: 'index', affix: false, noCache: true }
      },
      {
        path: 'water',
        component: (resolve) => require(['@/views/Water'], resolve),
        name: 'Water',
        meta: { title: '药物反馈管理', icon: 'index', affix: false, noCache: true }
      },
      {
        path: 'pest',
        component: (resolve) => require(['@/views/Pest'], resolve),
        name: 'Pest',
        meta: { title: '问诊反馈管理', icon: 'index', affix: false, noCache: true }
      },
      // {
      //   path: 'img',
      //   component: (resolve) => require(['@/views/Img'], resolve),
      //   name: 'Img',
      //   meta: { title: '图片管理', icon: 'index', affix: false, noCache: true }
      // },
      // {
      //   path: 'note',
      //   component: (resolve) => require(['@/views/Note'], resolve),
      //   name: 'Note',
      //   meta: { title: '记事本', icon: 'index', affix: false, noCache: true }
      // }
    ]

  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.path !== "/login") {
    const userInfo = localStorage.getItem("userInfo");
    console.log('userInfo:', userInfo)
    if (!userInfo) {
      next({ path: "/login" })
    }
  }
  next()
});

export default router
