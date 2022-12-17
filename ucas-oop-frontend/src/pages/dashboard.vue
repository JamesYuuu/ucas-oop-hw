<script setup lang="ts">
import axios, { Axios } from 'axios'
import { useRoute, useRouter } from 'vue-router'
import { watch } from 'vue'
import CarbonSetting from '~icons/carbon/settings'
import CarbonUsers from '~icons/carbon/user-multiple'
import CarbonArticle from '~icons/carbon/document'
import CarbonType from '~icons/carbon/type-pattern'

const router = useRouter()

const route = useRoute()

const types_all = reactive<string[]>([])

interface form {
  index: number
  name: string
}

watch(route, (to, from) => {
  router.go(0)
})

const formdata = reactive<form[]>([])

const type = route.query.type ? route.query.type.toString() : 'user'

if (type === 'type')
  get_all_types()

else if (type === 'article')
  get_all_articles()

else if (type === 'user')
  get_all_users()

function get_all_types() {
  axios.get('/api/dashboard/type').then(
    (response) => {
      types_all.values = response.data.result
      formdata.length = 0
      for (let i = 0; i < response.data.length; i++)
        formdata.push({ index: i, name: response.data.result[i] })
    }).catch(() => {
    ElMessage.error('请先登录')
    router.push('/login')
  })
}

function get_all_users() {
  axios.get('/api/dashboard/user').then(
    (response) => {
      formdata.length = 0
      for (let i = 0; i < response.data.length; i++)
        formdata.push({ index: i, name: response.data.result[i] })
    }).catch(() => {
    ElMessage.error('请先登录')
    router.push('/login')
  })
}

function get_all_articles() {
  axios.get('/api/dashboard/article').then(
    (response) => {
      formdata.length = 0
      for (let i = 0; i < response.data.length; i++)
        formdata.push({ index: i, name: response.data.result[i] })
    }).catch(() => {
    ElMessage.error('请先登录')
    router.push('/login')
  })
}

function handle_article() {
  router.push({
    path: '/dashboard',
    query: {
      type: 'article',
    },
  })
}

function handle_type() {
  router.push({
    path: '/dashboard',
    query: {
      type: 'type',
    },
  })
}

function handle_user() {
  router.push({
    path: '/dashboard',
    query: {
      type: 'user',
    },
  })
}

function add_new_item() {

}
const handleEdit = (index: number, row: form) => {
  console.log(index, row)
}
const handleDelete = (index: number, row: form) => {
  ElMessageBox.confirm(
    '删除操作将执行，且不可恢复',
    '警告',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    },
  )
    .then(() => {
      axios.delete(`/api/dashboard/${type}`, {
        params: {
          name: row.name,
        },
      }).then((response) => {
        if (response.status === 200) {
          ElMessage.success('删除成功')
          formdata.splice(index, 1)
        }
        else { ElMessage.error('删除失败') }
      }).catch(() => {
        ElMessage.error('请先登录')
        router.push('/login')
      })
    })
    .catch(() => {
      ElMessage({
        type: 'info',
        message: '取消删除',
      })
    })
}

const search = ref('')
const filterTableData = computed(() =>
  formdata.filter(
    data =>
      !search.value
      || data.name.toLowerCase().includes(search.value.toLowerCase()),
  ),
)
</script>

<template>
  <Nav />
  <el-row :gutter="80">
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
        <el-menu-item index="1" @click="handle_user()">
          <el-icon><CarbonUsers /></el-icon>
          <span text-lg>用户管理</span>
        </el-menu-item>
        <el-menu-item index="2" @click="handle_type()">
          <el-icon><CarbonType /></el-icon>
          <span text-lg>类别管理</span>
        </el-menu-item>
        <el-menu-item index="3" @click="handle_article()">
          <el-icon><CarbonArticle /></el-icon>
          <span text-lg>文章管理</span>
        </el-menu-item>
      </el-menu>
    </el-col>
    <el-col :span="21">
      <el-table :data="filterTableData" stripe border highlight-current-row style="width: 95%; font-size: large;">
        <el-table-column label="Index" prop="index" />
        <el-table-column label="Name" prop="name" />
        <el-table-column align="right">
          <template #header>
            <div class="grid grid-cols-6">
              <el-input
                v-model="search"
                placeholder="输入以搜索"
                class="col-span-4"
              />
              <div class="col-span-1" />
              <el-button
                type="primary"
                class="col-span-1"
                @click="add_new_item()"
              >
                新增
              </el-button>
            </div>
          </template>
          <template #default="scope">
            <el-button @click="handleEdit(scope.$index, scope.row)">
              编辑
            </el-button>
            <el-button
              type="danger"
              @click="handleDelete(scope.$index, scope.row)"
            >
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
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
