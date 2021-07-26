<template>
<div class="inner">
  <nav></nav>
  <main>
    <form action="">
      <input type="text" v-model="query">
    </form>
    <div class="theme-list">
    </div>
  </main>
</div>
</template>

<script>
export default {
  props: {
    themes: Array,
  },
  data () {
    return {
      query: '',
    }
  },
}
</script>
