<template>
  <div>
    <el-container>
      <el-aside width="auto">
        <common-aside></common-aside>
      </el-aside>
      <el-container>
        <el-header>
          <common-header></common-header>
        </el-header>
        <common-tag></common-tag>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import CommonAside from '@/components/CommonAside'
import CommonHeader from '@/components/CommonHeader'
import CommonTag from '@/components/CommonTag'
export default {
  components: {
    CommonAside,
    CommonHeader,
    CommonTag
  }
}
</script>
<style scoped>
* {
  font-size: 1.6rem;
  box-sizing: border-box;
}

.el-header {
  padding: 0;
}
</style>