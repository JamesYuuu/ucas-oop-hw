<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import type { AxiosResponse } from 'axios'
import axios from 'axios'
import { watch } from 'vue'
import MdEditor from 'md-editor-v3'
import CarbonDocument from '~icons/carbon/document'
import CarbonEdit from '~icons/carbon/edit'
import 'md-editor-v3/lib/style.css'

const route = useRoute()
const router = useRouter()

const type_name = route.query.type
const article_name = route.query.article?.toString()

const dialogFormVisible = ref(false)
const formLabelWidth = '100px'
const form = reactive({
  type: '',
  article: '',
})

const text = ref('# Hello World')

const article_all = reactive<string[]>([])
const types_all = reactive<string[]>([])

const is_collpase = type_name === undefined

const span = is_collpase ? 1 : 3

if (is_collpase === false) {
  get_all_article()
  get_article(article_name!)
}
else {
  get_all_types()
}

watch(route, (to, from) => {
  router.go(0)
})

function get_all_article() {
  axios.get('/api/article', { params: { type: type_name } }).then((response) => {
    article_all.length = 0
    for (let i = 0; i < response.data.length; i++)
      article_all.push(response.data.result[i])
    article_all.length = response.data.length
  }).catch(() => {
    ElMessage.error('请先登录')
    router.push('/login')
  })
}

function get_all_types() {
  axios.get('/api/dashboard/type').then(
    (response) => {
      types_all.values = response.data.result
    }).catch(() => {
    ElMessage.error('请先登录')
    router.push('/login')
  })
}

function get_article(item_name: string) {
  axios.get('/api/article', {
    params: {
      type: type_name,
      article: item_name,
    },
  }).then((response) => {
    text.value = response.data
  }).catch((error) => {
    deal_error(error)
  })
}

function change_data(item_name: string) {
  router.push({
    path: '/article',
    query: {
      type: type_name,
      article: item_name,
    },
  })
}

function update_data() {
  axios.put('/api/article', {
    type: type_name,
    article: article_name,
    text: text.value,
  }).then(() => {
    ElMessage.success('更新成功')
  }).catch((error) => {
    deal_error(error)
  })
}

function save() {
  if (is_collpase === true)
    dialogFormVisible.value = true
  else
    update_data()
}

function create_new_post() {
  axios.post('/api/article', {
    type: form.type,
    article: form.article,
    text: text.value,
  }).then(() => {
    ElMessage.success('创建成功')
  }).catch((error) => {
    deal_error(error)
  })
  dialogFormVisible.value = false
}

function deal_error(err: AxiosResponse) {
  if (err.status === 401) {
    ElMessage.error('请先登录')
    router.push('/login')
  }
  else { ElMessage.error('文件不存在') }
}
</script>

<template>
  <Nav />
  <el-row>
    <el-col :span="span">
      <el-menu
        :default-active="article_name!"
        class="el-menu-left"
        :collapse="is_collpase"
      >
        <div class="header">
          <el-icon>
            <CarbonEdit />
          </el-icon>
          <span text-2xl>
            {{ type_name }}
          </span>
        </div>
        <el-divider />
        <el-menu-item
          v-for="(item, index) in article_all"
          :key="index"
          :index="item"
          @click="change_data(item)"
        >
          <el-icon> <CarbonDocument /></el-icon>
          <span text-lg text-center> {{ item }} </span>
        </el-menu-item>
      </el-menu>
    </el-col>
    <el-col :span="24 - span">
      <MdEditor v-model="text" preview-theme="vuepress" class="editor" :tab-width="4" no-upload-img @save="save()" />
    </el-col>
  </el-row>

  <ElDialog v-model="dialogFormVisible" title="请输入相关信息" width="500px" draggable>
    <el-form :model="form">
      <el-form-item label="类别" :label-width="formLabelWidth">
        <el-select v-model="form.type" placeholder="请选择类别">
          <el-option v-for="(item, index) in types_all.values" :key="index" :label="item" :value="item" />
        </el-select>
      </el-form-item>
      <el-form-item label="标题" :label-width="formLabelWidth">
        <el-input v-model="form.article" autocomplete="on" autosize clearable />
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="create_new_post()">
          确定
        </el-button>
      </span>
    </template>
  </ElDialog>
</template>

<style scoped>
.el-menu-left {
  height: 90vh;
}

.editor{
    height: 90vh;
    width: 90%;
    margin: auto;
  }

.header {
  margin-left: 5%;
}

.el-button--text {
  margin-right: 15px;
}
.dialog-footer button:first-child {
  margin-right: 10px;
}
.el-select {
  width: 300px;
}
.el-input {
  width: 300px;
}
</style>
