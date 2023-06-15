<template>
    <div class="login" :style="'background-image:url(' + Background + ');'">
        <el-form ref="loginForm" :model="loginForm" :rules="loginRules" label-position="left" label-width="0px"
            class="login-form">
            <h3 class="title">
                术后康复子管理系统
            </h3>
            <el-form-item prop="username">
                <el-input v-model="loginForm.username" type="text" auto-complete="off" placeholder="账号">
                    <i slot="prefix" class="el-icon-user el-input__icon input-icon" />
                </el-input>
            </el-form-item>
            <el-form-item prop="password">
                <el-input v-model="loginForm.password" type="password" auto-complete="off" placeholder="密码"
                    @keyup.enter.native="handleLogin">
                    <i slot="prefix" class="el-icon-lock el-input__icon input-icon" />
                </el-input>
            </el-form-item>
            <el-form-item prop="email" v-if="isRegister">
                <el-input v-model="loginForm.email" type="email" auto-complete="off" placeholder="email">
                    <i slot="prefix" class="el-icon-message el-input__icon input-icon" />
                </el-input>
            </el-form-item>
            <div style="width: 100%;text-align: right;">
                <span class="register-button" v-if="!isRegister" @click="toRegister">注册新用户</span>
                <span class="register-button" v-else @click="toLogin">登录系统</span>
            </div>
            <el-form-item style="width:100%;" v-if="!isRegister">
                <el-button :loading="loading" size="medium" type="primary" style="width:100%;"
                    @click.native.prevent="handleLogin">
                    <span v-if="!loading">登 录</span>
                    <span v-else>登 录 中...</span>
                </el-button>
            </el-form-item>
            <el-form-item style="width:100%;" v-else>
                <el-button :loading="loading" size="medium" type="primary" style="width:100%;"
                    @click.native.prevent="handleRegister">
                    <span v-if="!loading">注 册</span>
                    <span v-else>注 册 中...</span>
                </el-button>
            </el-form-item>
        </el-form>
    </div>
</template>
  
<script>
import Background from '@/assets/background.webp'
import { login,register } from '@/api/login'
export default {
    name: 'Login',
    data() {
        return {
            Background: Background,
            codeUrl: '',
            cookiePass: '',
            loginForm: {
                username: 'admin',
                password: '123456',
            },
            loginRules: {
                username: [{ required: true, trigger: 'blur', message: '用户名不能为空' }],
                password: [{ required: true, trigger: 'blur', message: '密码不能为空' }],
                // email: [{ required: true, trigger: 'blur', message: 'email不能为空' }],
            },
            loading: false,
            redirect: undefined,
            isRegister: false,
        }
    },
    created() {

    },
    methods: {
        handleRegister() {
            this.$refs.loginForm.validate(valid => {
                const user = {
                    username: this.loginForm.username,
                    password: this.loginForm.password,
                    email: this.loginForm.email,
                }
                if (valid) {
                    this.loading = true
                    register(user).then((res) => {
                        console.log('res: ', res, typeof res)
                        this.loading = false
                        this.$message.success('注册成功')
                        this.isRegister = false
                    }).catch(() => {
                        this.loading = false
                        this.$message.error('注册失败')
                    })
                } else {
                    console.log('error submit!!')
                    return false
                }
            })
        },
        handleLogin() {
            this.$refs.loginForm.validate(valid => {
                const user = {
                    username: this.loginForm.username,
                    password: this.loginForm.password,
                }
                if (valid) {
                    this.loading = true
                    login(user).then((res) => {
                        console.log('res: ', res, typeof res)
                        this.loading = false
                        window.localStorage.setItem('userInfo', JSON.stringify(res))
                        if(res.status == "success"){
                            location.replace('/home')
                        }else{
                            this.$message.error('登录失败')
                        }
                    }).catch(() => {
                        this.loading = false
                        this.$message.error('登录失败')
                    })
                } else {
                    console.log('error submit!!')
                    return false
                }
            })
        },
        toRegister() {
            this.isRegister = true
        },
        toLogin() {
            this.isRegister = false
        }
    }
}
</script>
  
<style rel="stylesheet/scss" lang="scss" scoped>
#app {
    height: 100%;
}

.login {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-size: cover;
}

.title {
    margin: 0 auto 30px auto;
    text-align: center;
    color: #707070;
}

.login-form {
    border-radius: 6px;
    background: #ffffff;
    width: 385px;
    padding: 25px 25px 5px 25px;

    .el-input {
        height: 38px;

        input {
            height: 38px;
        }
    }

    .input-icon {
        height: 39px;
        width: 14px;
        margin-left: 2px;
    }
}

.login-tip {
    font-size: 13px;
    text-align: center;
    color: #bfbfbf;
}

.login-code {
    width: 33%;
    display: inline-block;
    height: 38px;
    float: right;

    img {
        cursor: pointer;
        vertical-align: middle
    }
}

.register-button {
    font-size: 12px;
    cursor: pointer;

    &:hover {
        color: #66b1ff;
    }
}
</style>
  