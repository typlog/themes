<template>
<div class="home">
  <nav class="home_nav inner">
    <strong>Categories</strong>
    <ul>
      <li><router-link :class="{active: hasTag()}" to="/">All</router-link></li>
      <li><router-link :class="{active: hasTag('blog')}" :to="{ query: { tag: 'blog' } }">Blog</router-link></li>
      <li><router-link :class="{active: hasTag('podcast')}" :to="{ query: { tag: 'podcast' } }">Podcast</router-link></li>
      <li><router-link :class="{active: hasTag('doc')}" :to="{ query: { tag: 'doc' } }">Documentation</router-link></li>
    </ul>
  </nav>
  <main class="home_main inner">
    <p>You can design and use your own theme as well. Learn <a href="https://docs.typlog.com/en/topic/theme/" target="_blank" rel="noopener noreferrer nofollow">how to use the theme builder</a>.</p>
    <div class="theme-list">
      <div class="theme" v-for="theme in themes" :key="theme.id">
        <router-link class="theme_image" :title="theme.name" :to="theme.id">
          <browser :images="theme.images" />
          <span class="theme_star" v-if="theme.stars">★ {{ theme.stars }}</span>
        </router-link>
        <div class="theme_info">
          <div class="theme_name">
            <strong v-text="theme.name"></strong>
            <div v-text="theme['name#ja']"></div>
          </div>
          <div class="theme_price">Free</div>
        </div>
      </div>
    </div>
  </main>
</div>
</template>

<script>
import themes from '../index.json'
import bridge from './bridge'
import Browser from './components/Browser.vue'

export default {
  components: { Browser },
  data () {
    const q = this.$route.query.q || ''
    return { themes, q }
  },
  watch: {
    "$route.query.tag": {
      immediate: true,
      handler (tag) {
        this.filterThemes(tag)
      },
    }
  },
  methods: {
    hasTag (tag) {
      return this.$route.query.tag === tag
    },
    onUse (theme) {
      bridge.emit('select', theme)
    },
    filterThemes (tag) {
      if (!tag) {
        this.themes = themes
      } else {
        this.themes = themes.filter(theme => {
          const tags = theme.tags || []
          return tags.indexOf(tag) !== -1
        })
      }
    }
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
  font-weight: 500;
  padding: 6px 16px;
  color: var(--text-color);
  text-decoration: none;
  border-radius: 3px;
}
.home_nav a.active {
  background-color: rgba(var(--highlight-rgb), 0.2);
}
.home_nav a:hover {
  text-decoration: none;
  background-color: rgba(var(--highlight-rgb), 0.1);
}
.home_main {
  flex-grow: 1;
}
.theme-list {
  display: flex;
  flex-wrap: wrap;
  margin-top: 1em;
  margin-left: -10px;
  margin-right: -10px;
}
.theme {
  margin: 10px;
  width: 280px;
}
.theme_image {
  display: block;
  position: relative;
  transition: all 0.2s ease;
}
.theme_image:hover {
  transform: translate3d(0, -6px, 0);
  box-shadow: 2px 5px 10px rgba(0, 0, 0, 0.1);
}
.theme_info {
  display: flex;
  margin-top: 1.2em;
  justify-content: space-between;
}
.theme_name {
  text-transform: uppercase;
}
.theme_star {
  position: absolute;
  display: block;
  right: 10px;
  bottom: 10px;
  color: white;
  background-color: rgba(0, 0, 0, 0.68);
  padding: 2px 10px;
  border-radius: 20px;
}
.theme_price {
  color: rgba(0, 0, 0, 0.48);
}

@media (max-width: 900px) {
  .home {
    flex-direction: column;
  }
  .home_nav {
    position: sticky;
    top: 0;
    left: 0;
    width: 100%;
    margin: 0 0 1em 0;
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(20px);
    z-index: 9;
  }
  .home_nav > strong {
    display: none;
  }
  .home_nav ul {
    margin-top: 0;
  }
  .home_nav li {
    display: inline-block;
    margin-right: 1em;
  }
  .home_nav a {
    padding: 0;
    border-radius: 0;
    border-bottom: 3px solid transparent;
  }
  .home_nav a.active {
    background-color: transparent;
    border-color: rgba(var(--highlight-rgb), 0.8);
  }
  .home_nav a:hover {
    color: rgba(var(--highlight-rgb), 0.8);
    background-color: transparent;
    border-color: rgba(var(--highlight-rgb), 0.6);
  }
  .home_main {
    margin-top: 40px;
  }
}
@media (max-width: 560px) {
  .theme {
    width: 100%;
    margin-bottom: 2em;
  }
}
</style>
