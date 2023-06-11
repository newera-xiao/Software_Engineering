<template>
    <div class="tabs">
        <el-tag v-for="(tag, index) in tags" :key="tag.id" type='success' :round="false" :closable="tag.name != '康复计划管理'"
            :effect="tag.name == $route.meta.title ? 'dark' : 'plain'" size="medium" @click="changeMenu(tag)"
            @close="handleClose(tag, index)">
            {{ tag.name }}
        </el-tag>
    </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
export default {
    data() {
        return {

        }
    },
    computed: {
        ...mapState({
            tags: state => state.tab.tabList
        })
    },
    methods: {
        ...mapMutations(['closeTag']),
        //点击tag跳转
        changeMenu(item) {
            this.$router.push({ path: item.path })
        },
        //关闭tag
        handleClose(item, index) {
            //调用store中的mutation
            this.closeTag(item)
            const length = this.tags.length

            //删除之后的跳转
            if (item.name !== this.$route.meta.title) {
                return
            }
            //表示删除最一项
            if (index == length) {
                this.$router.push({
                    path: this.tags[index - 1].path
                })
            } else {
                this.$router.push({
                    path: this.tags[index].path
                })
            }
        }
    }
}
</script>

<style lang="scss" scoped>
.tabs {
    padding: 5px 20px;
    box-shadow: 5px 5px 5px #eee;

    .el-tag {
        margin-right: 15px;
        cursor: pointer;
    }
}
</style>
