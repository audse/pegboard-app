import { createRouter, createWebHistory } from 'vue-router'
import authRoutes from './auth.routes'
import pegboardRoutes from './pegboard.routes'

import store from './../store/index.store'
import AuthService from '../services/auth.service'

import Home from './../pages/Home.vue'

const routes = [
    { 
        name: 'Home',
        path: '/', 
        component: Home,
    },
    
    ...authRoutes,
    ...pegboardRoutes
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach( async (to, from, next) => {

    await AuthService.loadCurrentUser()
    const isAuthenticated = store.getters['auth/isAuthenticated']

    if ( to.meta.requiresAuth && !isAuthenticated ) {
        next({ name: 'Sign In' })
    } else if ( to.meta.requiresUnauth && isAuthenticated ) {
        next({ name: 'Home' })
    } else {
        next()
    }
})

export default router