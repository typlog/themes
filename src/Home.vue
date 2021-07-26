<template>
<div class="home inner">
  <nav class="home_nav">
    <strong>Categories</strong>
    <ul>
      <li><router-link to="/">All</router-link></li>
      <li><router-link :to="{ query: { tag: 'blog' } }">Blog</router-link></li>
      <li><router-link :to="{ query: { tag: 'podcast' } }">Podcast</router-link></li>
      <li><router-link :to="{ query: { tag: 'doc' } }">Documentation</router-link></li>
    </ul>
  </nav>
  <main class="home_main">
    <form @submit.prevent="onSearch">
      <input type="search" v-model="q" placeholder="theme name ...">
    </form>
    <div class="theme-list">
      <div class="theme" v-for="theme in themes" :key="theme.name">
        <router-link class="browser" :title="theme.name" :to="theme.name">
          <div class="browser_toolbar"><span></span></div>
          <div class="browser_content" :style="thumbnail(theme)"></div>
        </router-link>
        <div class="theme_info">
          <div class="theme_name">
            <strong v-text="theme.name"></strong>
            <span class="sep">/</span>
            <span v-text="theme['name#ja']"></span>
          </div>
          <div class="theme_action">
            <button @click.prevent="onUse(theme)">Use</button>
          </div>
        </div>
      </div>
    </div>
  </main>
</div>
</template>

<script>
import themes from '../index.json'
import bridge from './bridge'

export default {
  data () {
    const q = this.$route.query.q || ''
    return { themes, q }
  },
  methods: {
    thumbnail (theme) {
      if (theme.images && theme.images.length) {
        const url = theme.images[0]
        const src = `https://cdn.jsdelivr.net/gh/${theme.repo}/${url}`
        return {'background-image': `url(${src})`}
      } else {
        return {}
      }
    },
    onSearch () {
      this.$router.push({ query: { q: this.q }})
      this.themes = themes.filter(theme => {
        const text = [theme.name, theme.repo].join(' ')
        return text.indexOf(this.q) !== -1
      })
    },
    onUse (theme) {
      bridge.emit('select', theme)
    },
  },
}
</script>

<style>
.home {
  display: flex;
}
.home_nav {
  width: 180px;
  flex-shrink: 0;
  margin-right: 32px;
}
.home_nav > strong {
  text-transform: uppercase;
  color: var(--subtext-color);
  font-weight: 500;
  font-size: 12px;
}
.home_nav ul {
  list-style-type: none;
  margin: 10px 0 0 0;
  padding: 0;
}
.home_nav li {
  padding: 2px 0;
}
.home_nav a {
  display: block;
  padding: 6px 16px;
  color: var(--text-color);
  text-decoration: none;
  border-radius: 3px;
}
.home_nav a:hover {
  text-decoration: none;
  background-color: rgba(var(--highlight-rgb), 0.1);
}
.home_main {
  flex-grow: 1;
}
.home_main input {
  appearance: none;
  width: 100%;
  max-width: 480px;
  box-sizing: border-box;
  border: 1px solid #dadada;
  border-radius: 40px;
  font: normal normal 14px/1.42 var(--sans-font), sans-serif;
  padding: 4px 18px;
  outline: none;
}
.theme-list {
  display: flex;
  flex-wrap: wrap;
  margin-top: 1em;
  margin-left: -8px;
  margin-right: -8px;
}
.theme {
  margin: 8px;
}
.theme .browser_content {
  width: 200px;
  height: 125px;
  border-radius: 3px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
.theme_info {
  display: flex;
  margin-top: 1.2em;
  justify-content: space-between;
}
.theme_name {
  text-transform: capitalize;
}

@media (max-width: 900px) {
  .home {
    flex-direction: column;
  }
  .home_nav {
    width: 100%;
    margin: 0 0 1em 0;
  }
  .home_nav > strong {
    display: none;
  }
  .home_nav li {
    display: inline-block;
    margin-right: 1em;
  }
  .home_nav a {
    padding: 0;
  }
}
</style>
