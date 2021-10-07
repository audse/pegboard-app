
import { createApp } from 'vue'
import App from './App.vue'
import VWave from 'v-wave'
import router from '@/router'
import store from '@/store'
import '@/assets/css/app.scss'

/* Components */
import { PageLayout } from '@/layouts'
import * as Component from '@/components/Elements'

createApp(App)
.use(router)
.use(store)
.use(VWave)
.component('page-layout', PageLayout)
.component('card', Component.Card)
.component('toolbar', Component.Toolbar)
.component('expandable', Component.Expandable)
.component('co-button',Component.CoButton)
.component('modal', Component.Modal)
.component('co-tag', Component.CoTag)
.component('icon', Component.Icon)
.component('switch-icon', Component.SwitchIcon)
.mount('#app')