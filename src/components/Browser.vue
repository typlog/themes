<template>
<div class="browser">
  <div class="browser_toolbar"><span></span></div>
  <div class="browser_content">
    <div class="browser_inner">
      <button class="browser_prev" v-if="prev" @click.prevent="current = prev">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
      </button>
      <ul class="browser_scroll" :style="scrollStyle">
        <li class="browser_image" v-for="src in images" :key="src">
          <img :src="src" alt="screenshot" />
        </li>
      </ul>
      <button class="browser_next" v-if="next" @click.prevent="current = next">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </button>
    </div>
    <div class="browser_mask" v-if="images.length > 1"></div>
  </div>
</div>
</template>

<script>
// TODO: lazy load image
export default {
  props: {
    images: Array,
  },
  data () {
    return {
      current: 1,
    }
  },
  computed: {
    scrollStyle () {
      const x = 1 - this.current
      return {
        transform: `translateX(${x}00%)`,
      }
    },
    prev () {
      if (this.current > 1) {
        return this.current - 1
      } else {
        return null
      }
    },
    next () {
      if (this.current < this.images.length) {
        return this.current + 1
      } else {
        return null
      }
    },
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
.browser button {
  color: rgba(255, 255, 255, 0.6);
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
.browser_inner,
.browser_mask {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
.browser_mask {
  display: none;
  pointer-events: none;
}
.browser_content:hover .browser_mask {
  display: block;
  background: rgba(0, 0, 0, 0.5);
}
.browser_scroll {
  display: flex;
  height: 100%;
  list-style: none;
  margin: 0;
  padding: 0;
  transition: transform 0.2s linear;
}
.browser_image {
  width: 100%;
  flex-shrink: 0;
  overflow-y: auto;
  overflow-x: hidden;
}
.browser_image img {
  width: 100%;
}
.browser button > svg {
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  width: 18px;
  height: 18px;
}
.browser_prev, .browser_next {
  position: absolute;
  top: calc(50% - 16px);
  background: transparent;
  border: 2px solid currentColor;
  width: 32px;
  height: 32px;
  text-align: center;
  border-radius: 32px;
  cursor: pointer;
  z-index: 9;
}
.browser_prev {
  left: 20px;
}
.browser_next {
  right: 20px;
}

.browser ::-webkit-scrollbar {
  display: none;
}
/* firefox */
.browser_image {
  scrollbar-width: none;
}
</style>
