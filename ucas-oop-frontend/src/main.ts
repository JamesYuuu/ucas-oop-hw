import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import routes from 'virtual:generated-pages'
import App from './App.vue'
import './styles/main.css'

import '@unocss/reset/tailwind.css'
import 'uno.css'

import axios from 'axios'
import VueAxios from 'vue-axios'

const app = createApp(App)
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})
app.use(router)
app.use(VueAxios, axios)
app.mount('#app')
