
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
.component('co-button',Component.CoButton)
.component('co-tag', Component.CoTag)
.component('expandable', Component.Expandable)
.component('form-text-field', Component.FormTextField)
.component('form-textarea-field', Component.FormTextAreaField)
.component('icon', Component.Icon)
.component('modal', Component.Modal)
.component('switch-icon', Component.SwitchIcon)
.component('toolbar', Component.Toolbar)
.mount('#app')