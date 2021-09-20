
import { createApp } from 'vue'
import App from './App.vue'
import './assets/css/app.scss'

// import Vuex from 'vuex'
import router from './router/index.routes'
import store from './store/index.store'

createApp(App).use(router).use(store).mount('#app')