<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import { onBeforeMount } from 'vue'

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
  get_article(article_name)
})

function get_article(article: string | undefined) {
  axios.get('/api/article', {
    params: {
      type: type_name,
      article: article_name,
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
  {{ article_all }}
</template>
