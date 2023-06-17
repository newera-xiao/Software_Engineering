<template>
    <div class="header-container">
        <div class="l-content">
            <el-button style="margin-right: 20px" @click="handleMenu" icon="el-icon-menu" size="mini"></el-button>
            <el-breadcrumb separator="/">
                <el-breadcrumb-item v-for="item in tags" :key="item.id" :to="{ path: item.path }">{{ item.name
                }}</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="r-content">
            <el-dropdown @command="handleCommand">
                <span class="el-dropdown-link">
                    菜单<i class="el-icon-arrow-down el-icon--right"></i>
                </span>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="password">修改密码</el-dropdown-item>
                    <el-dropdown-item command="logOut">退出</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
        </div>

        <el-dialog title="修改密码" :visible.sync="dialogVisible" width="50%" :before-close="handleClose">

            <el-form ref="passForm" :model="passForm" :rules="rules" label-width="80px">
                <el-form-item label="原密码" prop="old_password">
                    <el-input placeholder="请输入原密码" v-model="passForm.old_password"></el-input>
                </el-form-item>
                <el-form-item label="新密码" prop="new_password">
                    <el-input placeholder="请输入新密码" v-model="passForm.new_password"></el-input>
                </el-form-item>
            </el-form>

            <span slot="footer" class="dialog-footer">
                <el-button @click="handleClose">取 消</el-button>
                <el-button type="primary" @click="confirmSubmit">确 定</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
import { mapState } from 'vuex' //辅助函数
import { logout, password } from '@/api/login'
export default {
    data() {
        return {
            dialogVisible: false,
            passForm: {
                old_password: '',
                new_password: '',
            },
            rules: {
                old_password: [
                    { required: true, message: '请输入原密码', trigger: 'blur' }
                ],
                new_password: [
                    { required: true, message: '请输入新密码', trigger: 'blur' }
                ],
            }
        }
    },
    computed: {
        ...mapState({
            tags: state => state.tab.tabList
        })
    },
    methods: {
        handleMenu() {
            this.$store.commit('collapseMenu')
        },
        handleCommand(command) {
            if (command == 'password') {
                this.dialogVisible = true
            } else if (command == 'logOut') {
                logout().then(res => {
                    console.log('res: ', res)
                    this.$message.success(res.data.message)
                    localStorage.clear();
                    this.$router.replace('/login')
                })
            }
        },
        //弹窗关闭的时候
        handleClose() {
            this.passForm = {
                old_password: '',
                new_password: '',
            }
            this.$refs.passForm.resetFields()
            this.dialogVisible = false
        },
        //提交表单
        confirmSubmit() {
            this.$refs.passForm.validate((valid) => {
                if (valid) {
                    let params = Object.assign({}, this.passForm)
                    password(params).then(res => {
                        console.log('res: ', res)
                        if (res.status == 'success') {
                            this.$message.success('修改成功')
                            this.dialogVisible = false
                        } else {
                            this.$message.error(`修改失败：${res.data.message}`)
                        }
                    })
                }
            })
        },
    }
}
</script>

<style lang="scss" scoped>
.header-container {
    background-color: #fff;
    height: 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
    box-shadow: 2px 2px 2px #eee;

    .text {
        font-size: 14px;
        color: #fff;
        margin-left: 10px;
    }

    .l-content {
        display: flex;
        align-items: center;

        /deep/.el-breadcrumb__item {
            .el-breadcrumb__inner {
                font-weight: normal !important;
                color: #000 !important;

                &.is-link {
                    color: #666;
                }
            }

            &:last-child {
                .el-breadcrumb__inner {
                    color: #fff;
                }
            }
        }

    }
}
</style>