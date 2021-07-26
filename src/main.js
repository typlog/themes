import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import bridge from './bridge'

bridge.on('load', () => {
  document.body.className = 'embed'
  bridge.emit('ready')
})

const app = createApp(App)
app.use(router)
app.mount('#app')
