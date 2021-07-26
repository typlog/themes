<template>
<div class="detail inner">
  <nav class="breadcrumbs">
    <router-link to="/">All themes</router-link>
    <span class="sep">/</span>
    <span v-text="$route.params.slug"></span>
  </nav>
</div>
</template>

<style>
.sep {
  margin: 0 3px;
  color: #ccc;
  font-weight: 700;
  font-size: 12px;
}
</style>
