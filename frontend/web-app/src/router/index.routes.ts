import { createRouter, createWebHistory } from 'vue-router'

import Home from './../pages/Home.vue'
import About from './../pages/About.vue'
import SignUp from './../pages/Auth/SignUp/SignUp.vue'
import SignIn from './../pages/Auth/SignIn/SignIn.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
  { path: '/signup', component: SignUp },
  { path: '/signin', component: SignIn }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router