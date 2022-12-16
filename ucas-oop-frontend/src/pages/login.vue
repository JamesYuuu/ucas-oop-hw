<script setup lang="ts">
import { useRouter } from 'vue-router'
import axios from 'axios'
import type { FormRules } from 'element-plus'
import CarbonUser from '~icons/carbon/user'
import CarbonPassword from '~icons/carbon/password'
import SimpleIconsMarkdown from '~icons/simple-icons/markdown'
import CarbonLogin from '~icons/carbon/login'
import CarbonReset from '~icons/carbon/reset'
import CarbonNewTab from '~icons/carbon/new-tab'

const router = useRouter()
const load = ref(false)

interface loginData {
  username: string
  password: string
}
const loginForm = ref<loginData>({
  username: '',
  password: '',
})
const loginRules = reactive<FormRules>({
  username: [
    { required: true, message: '请输入用户名' },
  ],
  password: [
    { required: true, message: '请输入密码' },
  ],
})
function login() {
  axios.get('/api/login', {
    params: {
      username: loginForm.value.username,
      password: loginForm.value.password,
    },
  }).then(() => {
    ElMessage.success('登录成功')
    router.push('/home')
  }).catch(() => {
    ElMessage.error('请输入正确的用户名和密码')
    reset()
  })
}
function reset() {
  loginForm.value.username = ''
  loginForm.value.password = ''
  load.value = false
}
function register() {
  router.push('/register')
}
</script>

<template>
  <div class="bg">
    <el-card shadow="always">
      <el-icon
        :size="30"
      >
        <SimpleIconsMarkdown />
      </el-icon>
      <p>登录 Mark It Down</p>
      <br>
      <el-form
        class="login"
        :model="loginForm"
        :rules="loginRules"
      >
        <el-form-item>
          <el-input
            v-model="loginForm.username"
            placeholder="请输入用户名"
            :prefix-icon="CarbonUser"
            size="large"
          />
        </el-form-item>
        <el-form-item>
          <el-input
            v-model="loginForm.password"
            placeholder="请输入密码"
            show-password
            :prefix-icon="CarbonPassword"
            size="large"
          />
        </el-form-item>
        <el-form-item m-auto>
          <el-button
            size="large"
            m-auto
            :icon="CarbonLogin"
            :loading="load"
            @click="login"
          >
            登录
          </el-button>
          <el-button
            size="large"
            m-auto
            :icon="CarbonReset"
            @click="reset"
          >
            清空
          </el-button>
          <el-button
            size="large"
            m-auto
            :icon="CarbonNewTab"
            @click="register"
          >
            前往注册
          </el-button>
        </el-form-item>
      </el-form>
      <el-divider />
      Visit <a href="https://www.jamesyuuu.me" target="_blank" hover-text-blue>
        My Home Page
      </a>
      For More Information
    </el-card>
  </div>
</template>

<style scoped>
  .el-card{
    @apply w-480px text-center absolute top-1/3 left-1/2 transform -translate-x-1/2 -translate-y-1/2;
  }
  .el-form{
    @apply items-center
  }
  .el-button{
    @apply bg-blue-500 text-white
  }
</style>
