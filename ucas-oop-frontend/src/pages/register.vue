<script setup lang="ts">
import { useRouter } from 'vue-router'
import axios from "axios"
import CarbonUser from '~icons/carbon/user'
import CarbonPassword from '~icons/carbon/password'
import CarbonEmail from '~icons/carbon/email'
import CarbonCheckmark from '~icons/carbon/checkmark'
import CarbonReset from '~icons/carbon/reset'
import SimpleIconsMarkdown from '~icons/simple-icons/markdown'
import { FormRules } from 'element-plus'
import CarbonLogin from '~icons/carbon/login'


const router = useRouter()
const load = ref(false)

interface loginData {
  username: string
  password: string
  email: string
}
const registerForm = ref<loginData>({
  username: '',
  password: '',
  email: '',
})
const registerRules = reactive<FormRules>({
  username: [
    { required: true, message: '请输入用户名' },
  ],
  password: [
    { required: true, message: '请输入密码' },
  ],
  email: [
    { required: false, message: '请输入邮箱' },
  ],
})
function submit() {
  axios.post('/api/login', {
    username: registerForm.value.username,
    password: registerForm.value.password,
    email: registerForm.value.email,
  }).then(() => {
    ElMessage.success('注册成功')
    router.push('/login')
  }).catch((err) => {
    if (err.response.status === 409)
      ElMessage.error('用户名已存在')
    else
      ElMessage.error('请输入正确的用户名以及密码')
    reset()
  })
}
function reset() {
  registerForm.value.username = ''
  registerForm.value.password = ''
  load.value = false
}
function goLogin() {
  router.push('/login')
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
      <p>注册 Mark It Down</p>
      <br>
      <el-form
        class="register"
        :model="registerForm"
        :rules="registerRules"
      >
        <el-form-item>
          <el-input
            v-model="registerForm.username"
            placeholder="请输入用户名"
            :prefix-icon="CarbonUser"
            size="large"
          />
        </el-form-item>
        <el-form-item>
          <el-input
            v-model="registerForm.password"
            placeholder="请输入密码"
            show-password
            :prefix-icon="CarbonPassword"
            size="large"
          />
        </el-form-item>
        <el-form-item>
          <el-input
            v-model="registerForm.email"
            placeholder="请输入邮箱"
            :prefix-icon="CarbonEmail"
            size="large"
          />
        </el-form-item>
        <el-form-item m-auto>
          <el-button
            size="large"
            m-auto
            :icon="CarbonCheckmark"
            :loading="load"
            @click="submit"
          >
            确定
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
            :icon="CarbonLogin"
            @click="goLogin"
          >
            前往登录
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
