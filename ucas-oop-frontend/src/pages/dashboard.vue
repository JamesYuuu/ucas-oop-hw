<script setup lang="ts">
import axios from 'axios'
import { useRouter } from 'vue-router'
import CarbonSetting from '~icons/carbon/settings'
import CarbonUsers from '~icons/carbon/user-multiple'
import CarbonArticle from '~icons/carbon/document'
import CarbonTypes from '~icons/carbon/types'
import CarbonType from '~icons/carbon/type-pattern'

const router = useRouter()

const types_all = reactive<string[]>([])

get_all_types()

function get_all_types() {
  axios.get('/api/index').then(
    (response) => {
      types_all.values = response.data.types
    }).catch(() => {
    ElMessage.error('请先登录')
    router.push('/login')
  })
}
</script>

<template>
  <Nav />
  <el-row class="tac">
    <el-col :span="3">
      <el-menu
        default-active="1"
        class="el-menu-left"
      >
        <div class="header">
          <el-icon>
            <CarbonSetting />
          </el-icon>
          <span text-xl>
            后台管理
          </span>
        </div>
        <el-divider />
        <el-menu-item index="1">
          <el-icon><CarbonUsers /></el-icon>
          <span text-lg>用户管理</span>
        </el-menu-item>
        <el-menu-item index="2">
          <el-icon><CarbonType /></el-icon>
          <span text-lg>类别管理</span>
        </el-menu-item>
        <el-sub-menu index="3">
          <template #title>
            <el-icon><CarbonArticle /></el-icon>
            <span text-lg>文章管理</span>
          </template>
          <el-menu-item v-for="(item, index) in types_all.values" :key="index" :index="`3-${index}`">
            <el-icon><CarbonTypes /></el-icon>
            <span text-lg>{{ item }}</span>
          </el-menu-item>
        </el-sub-menu>
      </el-menu>
    </el-col>
  </el-row>
</template>

<style scoped>
.el-menu-left {
  height: 90vh;
}
.header {
  margin-left: 25%;
}
</style>
