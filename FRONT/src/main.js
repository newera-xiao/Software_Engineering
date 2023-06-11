import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// require('./mock')  //引入 mock 入口文件

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import * as echarts from 'echarts'
Vue.prototype.$echarts = echarts

Vue.prototype.$apiUrl = process.env.VUE_APP_API_URL

import '@/style/main.scss'

Vue.use(ElementUI);

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
