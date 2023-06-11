const port = 8080
module.exports = {
  devServer: {
    port: port,
    open: true,
    proxy: {
      // 将 /api 匹配到 http://localhost:3001
      "/api": {
        target: "http://localhost:3001",// 代理的后端地址
        changeOrigin: true, // 能否跨域
        // ws: true, // 这里默认是true
        secure: false,
        // pathRewite: {
        //   "^/api": ""
        // }
      }
    }
  }
}