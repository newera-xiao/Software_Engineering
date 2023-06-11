import axios from 'axios'
import { Message } from 'element-ui';

const service = axios.create({
  baseURL: '',
  headers: {
    'Content-Type': 'application/json'
  },
  timeout: 120000 // 请求超时时间
})

// request拦截器
service.interceptors.request.use(
  config => {
    return config
  },
  error => {

    Promise.reject(error)
  }
)

// response 拦截器
service.interceptors.response.use(
  response => {

    return response.data
  },
  error => {
    console.log('error:', error)
    Message.error(error.response.data.message)
    return Promise.reject(error)
  }
)


export default service