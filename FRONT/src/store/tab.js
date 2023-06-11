export default {
    state: {
        isCollapse: false,   //控制菜单的展开与收起
        tabList: [
            {
                name: '康复计划管理',
                id: "1",
                icon: 'el-icon-menu',
                path: '/home'
            },
        ]//面包屑数据
    },
    mutations: {
        //修改菜单栏收起
        collapseMenu(state) {
            state.isCollapse = !state.isCollapse
        },
        //更新面包屑
        selectMenu(state, payload) {
            if (payload.name !== '首页') {
                const index = state.tabList.findIndex(item => item.name === payload.name)
                if (index === -1) {
                    state.tabList.push(payload)
                }
            }
        },
        //删除指定的tag数据
        closeTag(state, payload) {
            const inds = state.tabList.findIndex(item => item.name == payload.name)
            state.tabList.splice(inds, 1)
        }
    }
}