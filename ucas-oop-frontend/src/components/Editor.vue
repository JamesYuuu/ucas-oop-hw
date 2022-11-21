<script setup>
import { ref } from 'vue'
import MdEditor from 'md-editor-v3'
import 'md-editor-v3/lib/style.css'

const text = ref('# Hello Editor')
</script>

<template>
  <MdEditor v-model="text" preview-theme="vuepress" class="editor" />
</template>

<style>
  .editor{
    height: 90vh;
    width: 80%;
    margin: auto;
  }
</style>
