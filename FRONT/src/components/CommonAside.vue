<template>
    <el-menu :default-active="activeIndex" class="el-menu-vertical-demo" background-color="#304256" text-color="#fff"
        active-text-color="#67c23a" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
        <h3>{{ isCollapse ? '康复' : '术后康复子系统' }}</h3>
        <el-menu-item v-for="(item, inds) in menuData" :key="item.id" :index="item.id" @click="goPath(item)">
            <i :class="item.icon"></i>
            <span slot="title">{{ item.name }}</span>
        </el-menu-item>
    </el-menu>
</template>

  
<style lang="scss" scoped>
.el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 250px;
}

.el-menu {
    height: 100%;
    border-right: none;
    min-height: 100vh;
    // background-color: rgb(48, 66, 86)!important;

    h3 {
        color: #fff;
        text-align: center;
        line-height: 48px;
        font-size: 22px;
    }

    .el-menu-item {
        font-size: 18px;
        height: 80px;
        line-height: 80px;

        [class^=el-icon-] {
            margin-right: 15px;
            font-size: 24px;
        }
    }
}
</style>
  
<script>
export default {
    data() {
        return {
            activeIndex: '1',
            menuData: [
                {
                    name: '康复计划管理',
                    id: "1",
                    icon: 'el-icon-menu',
                    path: '/home'
                },
                {
                    name: '康复知识库',
                    id: "2",
                    icon: 'el-icon-notebook-2',
                    path: '/temp'
                },
                {
                    name: '进度跟踪',
                    id: "3",
                    icon: 'el-icon-s-order',
                    path: '/track'
                },
                {
                    name: '药物反馈管理',
                    id: "4",
                    icon: 'el-icon-sugar',
                    path: '/water'
                },
                {
                    name: '问诊反馈管理',
                    id: "5",
                    icon: 'el-icon-phone-outline',
                    path: '/pest'
                },
                // {
                //     name: '图片管理',
                //     id: "5",
                //     icon: 'el-icon-picture-outline',
                //     path: '/img/'
                // },
                // {
                //     name: '记事本',
                //     id: "6",
                //     icon: 'el-icon-edit-outline',
                //     path: '/note'
                // },
            ]
        };
    },
    computed: {
        isCollapse() {
            return this.$store.state.tab.isCollapse
        }
    },
    methods: {
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        },
        goPath(item) {
            if (this.$route.path !== item.path) {
                this.$router.push(item.path)
            }
            this.$store.commit('selectMenu', item)
        }
    },
    created() {
        console.log('commonAside created', this.$route)
        this.menuData.forEach(res => {
            if (res.path == this.$route.path) {
                this.activeIndex = res.id
                this.$store.commit('selectMenu', res)
            }
        })
    }
}
</script>