<template>
<div class="detail inner">
  <nav class="breadcrumbs">
    <router-link to="/">All themes</router-link>
    <span class="sep">/</span>
    <span class="detail_name" v-text="$route.params.slug"></span>
  </nav>
  <div class="detail_head">
    <div class="detail_images">
      <div class="browser">
        <div class="browser_toolbar"><span></span></div>
        <div class="browser_content"></div>
      </div>
    </div>
    <div class="detail_info">
      <table>
        <tbody>
          <tr v-for="d in names" :key="d[0]">
            <th v-text="d[0]"></th>
            <td v-text="d[1]"></td>
          </tr>
          <tr>
            <th>Author</th>
            <td v-text="theme.author"></td>
          </tr>
          <tr>
            <th>GitHub</th>
            <td><a :href="'https://github.com/' + theme.repo" target="_blank" v-text="theme.repo"></a></td>
          </tr>
        </tbody>
      </table>
      <div class="detail_action">
        <a class="button" :href="'https://theme-' + theme.name + '.typlog.com/'" target="_blank">Preview</a>
        <button class="js-use button" @click.prevent="onUse">Use</button>
      </div>
    </div>
  </div>
  <div class="detail_readme yue" v-html="theme.readme"></div>
</div>
</template>

<script>
import themes from '../index.json'
import bridge from './bridge'

export default {
  data () {
    const name = this.$route.params.slug
    const theme = themes.filter(d => d.name === name)[0]
    return { theme }
  },
  computed: {
    names () {
      const rv = [['Name', this.theme.name.toUpperCase()]]
      if (this.theme['name#zh']) {
        rv.push(['名稱', this.theme['name#zh']])
      }
      if (this.theme['name#ja']) {
        rv.push(['名前', this.theme['name#ja']])
      }
      return rv
    },
  },
  methods: {
    onUse () {
      bridge.emit('select', this.theme)
    },
  },
  async created () {
    const name = this.$route.params.slug
    const resp = await fetch(`/data/${name}.json`)
    const data = await resp.json()
    this.theme = data
  },
}
</script>


<style>
.detail_name {
  text-transform: uppercase;
}
.detail_head {
  display: flex;
  margin-top: 2em;
}
.detail_info {
  margin-left: 4em;
}
.detail_images {
  flex-grow: 1;
  max-width: 560px;
}
.detail_info table {
  min-width: 200px;
  border-collapse: collapse;
}
.detail_info th,
.detail_info td {
  padding: 10px 6px;
  border-bottom: 1px solid #efefef;
}
.detail_action {
  margin-top: 2em;
  text-align: center;
}
.detail_action .button + .button {
  margin-left: 1em;
}
.detail_readme {
  margin-top: 3.2em;
}
@media (max-width: 860px) {
  .detail_head {
    flex-direction: column;
  }
  .detail_images {
    max-width: 100%;
  }
  .detail_info {
    display: flex;
    justify-content: space-between;
    margin: 2em 0 0 0;
  }
  .detail_action {
    display: flex;
    flex-direction: column;
    margin: 0;
  }
  .detail_action .button {
    width: 100px;
  }
  .detail_action .button + .button {
    margin: 1em 0 0 0;
  }
}
</style>
