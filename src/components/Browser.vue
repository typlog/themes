<template>
<div class="browser">
  <div class="browser_toolbar"><span></span></div>
  <div class="browser_content">
    <div class="browser_inner">
      <div class="browser_scroll">
        <slot>
          <img :src="src" alt="screenshot" v-for="src in images" :key="src">
        </slot>
      </div>
    </div>
  </div>
</div>
</template>

<script>
// TODO: lazy load image
export default {
  props: {
    images: Array,
  },
}
</script>

<style>
.browser {
  display: block;
  position: relative;
  border-radius: 6px;
  overflow: hidden;
  box-shadow: 2px 5px 10px rgba(0, 0, 0, 0.08);
}
.browser_toolbar {
  position: relative;
  background-color: #f2f2f2;
  border-radius: 6px 6px 0 0;
  padding: 10px 12px;
}
.browser_toolbar span,
.browser_toolbar span:before,
.browser_toolbar span::after {
  display: block;
  content: '';
  background-color: #c4c4c4;
  border-radius: 50%;
  height: 6px;
  width: 6px;
}
.browser_toolbar span {
  position: relative;
}
.browser_toolbar span:before {
  position: absolute;
  left: 10px;
}
.browser_toolbar span::after {
  position: absolute;
  left: 20px;
}
.browser_content {
  position: relative;
  padding-bottom: 62.5%;
  border-radius: 0 0 3px 3px;
}
.browser_inner {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
.browser_inner img {
  width: 100%;
}
.browser_scroll {
  overflow-y: auto;
}
</style>
