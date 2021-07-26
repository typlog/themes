import { createRouter, createWebHashHistory } from 'vue-router'
import Home from './Home.vue'
import Detail from './Detail.vue'

const routes = [
  { path: '', component: Home, name: 'Home' },
  { path: '/:slug', component: Detail, name: 'Detail' },
]

export default createRouter({
  routes,
  history: createWebHashHistory(),
})
