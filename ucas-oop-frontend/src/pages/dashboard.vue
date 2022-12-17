<script setup lang="ts">
import axios, { Axios } from 'axios'
import { useRoute, useRouter } from 'vue-router'
import { watch } from 'vue'
import CarbonTypes from '~icons/carbon/types'
import CarbonSetting from '~icons/carbon/settings'
import CarbonUsers from '~icons/carbon/user-multiple'
import CarbonArticle from '~icons/carbon/document'
import CarbonType from '~icons/carbon/type-pattern'

const router = useRouter()

const route = useRoute()

const types_all = reactive<string[]>([])

const dialogFormVisible = ref(false)
const input_item = ref('')

interface form {
  index: number
  name: string
}

watch(route, (to, from) => {
  router.go(0)
})

const formdata = reactive<form[]>([])

const type = route.query.type ? route.query.type.toString() : 'user'
const type_name = route.query.type_name?.toString()

const title = type === 'user' ? '新增用户名' : type === 'type' ? '新增分类名' : '新增文章名'

const new_name_input = reactive<string[]>([])
get_all_types()

if (type === 'article')
  get_all_articles()

else if (type === 'user')
  get_all_users()

function get_all_types() {
  axios.get('/api/dashboard/type').then(
    (response) => {
      types_all.values = response.data.result
      if (type === 'type') {
        formdata.length = 0
        for (let i = 0; i < response.data.length; i++)
          formdata.push({ index: i, name: response.data.result[i] })
      }
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
  if (type_name === 'all') {
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
  else {
    axios.get('/api/article', { params: { type: type_name } }).then((response) => {
      formdata.length = 0
      for (let i = 0; i < response.data.length; i++)
        formdata.push({ index: i, name: response.data.result[i] })
    }).catch(() => {
      ElMessage.error('请先登录')
      router.push('/login')
    })
  }
}

function handle_article(item: string) {
  router.push({
    path: '/dashboard',
    query: {
      type: 'article',
      type_name: item,
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
  axios.post(`/api/dashboard/${type}`, {
    type: type_name,
    name: input_item.value,
  }).then(() => {
    ElMessage.success('添加成功')
    router.go(0)
  }).catch(() => {
    ElMessage.error('添加失败')
  })
  dialogFormVisible.value = true
}

const handleEdit = (index: number, row: form) => {
  axios.put(`/api/dashboard/${type}`, {
    type: type_name,
    name: row.name,
    new_name: new_name_input[index],
  }).then(() => {
    ElMessage.success('修改成功')
    router.go(0)
  }).catch(() => {
    ElMessage.error('修改失败')
  })
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
    <el-col :span="4">
      <el-menu
        :default-active="type"
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
        <el-menu-item index="user" @click="handle_user()">
          <el-icon><CarbonUsers /></el-icon>
          <span text-lg>用户管理</span>
        </el-menu-item>
        <el-menu-item index="type" @click="handle_type()">
          <el-icon><CarbonType /></el-icon>
          <span text-lg>类别管理</span>
        </el-menu-item>
        <el-sub-menu index="3">
          <template #title>
            <el-icon><CarbonArticle /></el-icon>
            <span text-lg>文章管理</span>
          </template>
          <el-menu-item @click="handle_article('all')">
            <el-icon><CarbonTypes /></el-icon>
            <span text-lg>所有</span>
          </el-menu-item>
          <el-menu-item v-for="(item, index) in types_all.values" :key="index" :index="`3-${index}`" @click="handle_article(item)">
            <el-icon><CarbonTypes /></el-icon>
            <span text-lg>{{ item }}</span>
          </el-menu-item>
        </el-sub-menu>
      </el-menu>
    </el-col>
    <el-col :span="20">
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
                clearable
              />
              <div class="col-span-1" />
              <el-button
                type="primary"
                class="col-span-1"
                @click="dialogFormVisible = true"
              >
                新增
              </el-button>
            </div>
          </template>
          <template #default="scope">
            <div class="grid grid-cols-11">
              <el-input v-model="new_name_input[scope.$index]" style="width:95%" class="col-span-7" clearable />
              <el-button class="col-span-2" @click="handleEdit(scope.$index, scope.row)">
                更新
              </el-button>
              <el-button
                type="danger"
                class="col-span-2" @click="handleDelete(scope.$index, scope.row)"
              >
                删除
              </el-button>
            </div>
          </template>
        </el-table-column>
      </el-table>
    </el-col>
  </el-row>

  <el-dialog v-model="dialogFormVisible" :title="title" width="450px">
    <el-input v-model="input_item" clearable />
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="add_new_item()">
          确认
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<style scoped>
.el-menu-left {
  height: 90vh;
}
.header {
  margin-left: 25%;
}
.dialog-footer button:first-child {
  margin-right: 10px;
}
.el-input {
  width: 400px;
}
</style>
