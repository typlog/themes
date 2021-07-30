import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import bridge from './bridge'

bridge.on('load', () => {
  document.body.className = 'embed'
  bridge.emit('ready')
})

const app = createApp(App)

app.directive('cover', {
  mounted (el, binding) {
    if (binding.value) {
      setTimeout(() => {
        el.setAttribute('style', 'background-image: url(' + binding.value + ')')
      }, 100)
    }
  }
})

app.use(router)
app.mount('#app')
