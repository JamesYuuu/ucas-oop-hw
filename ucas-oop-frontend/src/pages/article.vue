<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import { onBeforeMount } from 'vue'
import MdEditor from 'md-editor-v3'
import CarbonDocument from '~icons/carbon/document'
import 'md-editor-v3/lib/style.css'

const route = useRoute()
const router = useRouter()

const type_name = route.query.type
const article_name = route.query.article?.toString()

const text = ref('')

const article_all = reactive<string[]>([])

onBeforeMount(() => {
  axios.get('/api/article', { params: { type: type_name } }).then((response) => {
    article_all.length = 0
    for (let i = 0; i < response.data.length; i++)
      article_all.push(response.data.result[i])
    article_all.length = response.data.length
  }).catch(() => {
    ElMessage.error('请先登录')
    router.push('/login')
  })
  get_article(article_name!)
})

function get_article(item_name: string) {
  axios.get('/api/article', {
    params: {
      type: type_name,
      article: item_name,
    },
  }).then((response) => {
    text.value = response.data
  }).catch(() => {
    ElMessage.error('请先登录')
    router.push('/login')
  })
}
</script>

<template>
  <Nav />
  <el-row>
    <el-col :span="3">
      <el-menu
        :default-active="article_name!"
        class="el-menu-left"
      >
        <p text-center text-2xl>
          {{ type_name }}
        </p>
        <el-divider />
        <el-menu-item
          v-for="(item, index) in article_all"
          :key="index"
          :index="item"
          @click="get_article(item)"
        >
          <el-icon> <CarbonDocument /></el-icon>
          <span text-lg text-center> {{ item }} </span>
        </el-menu-item>
      </el-menu>
    </el-col>
    <el-col :span="21">
      <MdEditor v-model="text" preview-theme="vuepress" class="editor" :tab-width="4" />
    </el-col>
  </el-row>
</template>

<style>
.el-menu-left {
  height: 90vh;
}

.editor{
    height: 90vh;
    width: 90%;
    margin: auto;
  }
</style>
