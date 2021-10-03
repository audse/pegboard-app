
import { createApp } from 'vue'
import App from './App.vue'

import './assets/css/app.scss'

import router from './router/index.routes'
import store from './store/index.store'

import VWave from 'v-wave'

createApp(App)
.use(router)
.use(store)
.use(VWave)
.mount('#app')