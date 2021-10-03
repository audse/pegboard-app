
import { createApp } from 'vue'
import App from './App.vue'

import './assets/css/app.scss'

import router from './router/index.routes'
import store from './store/index.store'

import VWave from 'v-wave'

import Page from './layouts/Page.layout.vue'
import Card from './components/Elements/Card.vue'
import Toolbar from './components/Elements/Toolbar.vue'
import Expandable from './components/Elements/Expandable.vue'
import CoButton from './components/Elements/Button.vue'
import Modal from './components/Elements/Modal.vue'
import Tag from './components/Elements/Tag.vue'


createApp(App)
.use(router)
.use(store)
.use(VWave)
.component('page', Page)
.component('card', Card)
.component('toolbar', Toolbar)
.component('expandable', Expandable)
.component('co-button', CoButton)
.component('modal', Modal)
.component('tag', Tag)
.mount('#app')