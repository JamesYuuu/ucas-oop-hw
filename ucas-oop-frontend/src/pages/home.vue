<script setup lang= "ts">
import axios from 'axios'
import { useRouter } from 'vue-router'
import { onBeforeMount } from 'vue'
import CarbonDocument from '~icons/carbon/document'
import CarbonEdit from '~icons/carbon/edit'

const router = useRouter()

const page_data = reactive(
  {
    page_num: 1,
    current_page: 1,
  },
)

interface typedata {
  type: string
  article: Array<string>
}

const type_data = reactive<typedata[]>(
  [{
    type: '',
    article: [],
  }],
)

onBeforeMount(() => {
  axios.get('/api/index').then(
    (response) => {
      page_data.page_num = response.data.page_num
    }).catch(() => {
    ElMessage.error('请先登录')
    router.push('/login')
  })
  get_data()
})

function get_data() {
  axios.get('/api/index', {
    params: {
      page: page_data.current_page,
    },
  }).then(
    (response) => {
      type_data.length = 0
      for (let i = 0; i < response.data.length; i++) {
        type_data.push(
          {
            type: response.data.result[i].type,
            article: response.data.result[i].article,
          },
        )
      }
      type_data.length = response.data.length
    }).catch(
    () => {
      ElMessage.error('请先登录')
      router.push('/login')
    })
}

function get_more(type_name: string, article_name: string) {
  router.push({
    path: '/article',
    query: {
      type: type_name,
      article: article_name,
    },
  })
}
</script>

<template>
  <Nav />
  <el-row v-for="rindex in Math.ceil(type_data.length / 3)" :key="rindex" justify="center">
    <el-col v-for="(type_item, tindex) in type_data.slice((rindex - 1) * 3, Math.min(type_data.length, rindex * 3))" :key="tindex" :span="6" mx-4 my-4>
      <el-card class="box-card" shadow="hover">
        <template #header>
          <div class="card-header">
            <div class="p">
              {{ type_item.type }}
            </div>
            <el-button class="button" text :icon="CarbonEdit" @click="get_more(type_item.type, type_item.article[0])">
              <div class="p">
                查看更多
              </div>
            </el-button>
          </div>
        </template>
        <div v-for="(item, index) in type_item.article" :key="index" class="text item">
          <el-button class="button" text :icon="CarbonDocument" @click="get_more(type_item.type, item)">
            <div class="p">
              {{ item }}
            </div>
          </el-button>
        </div>
      </el-card>
    </el-col>
  </el-row>
  <div class="page">
    <el-pagination v-model:current-page="page_data.current_page" background layout="prev, pager, next" :total="page_data.page_num * 10" hide-on-single-page @current-change="get_data()" />
  </div>
  <Footer />
</template>

<style>
.page {
    position: absolute;
    left: 50%;
    bottom: 12%;
    transform:translate(-50%,0);
    z-index: 3;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.p {
  font-size: 16px;
}

.item {
  margin-bottom: 3px;
}

.box-card {
  width: 480px;
  height: 300px ;
}
</style>
