<script>

</script>

<template>
  <el-affix position="top">
    <el-menu
      :default-active="$route.path"
      class="el-menu-nav"
      mode="horizontal"
      :ellipsis="false"
      router
    >
      <el-menu-item index="/home">
        Mark It Down
      </el-menu-item>
      <div class="flex-grow" />
      <el-menu-item index="/home">
        首页
      </el-menu-item>
      <el-menu-item index="/new">
        新增
      </el-menu-item>
      <el-menu-item index="/dashboard">
        管理
      </el-menu-item>
    </el-menu>
  </el-affix>
</template>

<style scoped>
.el-menu-item{
  @apply text-xl font-sans pt-5 pb-2;
}
.el-menu-nav{
  @apply m-auto px-1/10;
  @apply mb-5;
}
</style>
