import { createRouter, createWebHashHistory } from 'vue-router'
import ThemeList from './components/ThemeList.vue'
import ThemeDetail from './components/ThemeDetail.vue'

const routes = [
  { path: '', component: ThemeList, name: 'Home' },
  { path: '/:slug', component: ThemeDetail, name: 'Detail' },
]

export default createRouter({
  routes,
  history: createWebHashHistory(),
})
