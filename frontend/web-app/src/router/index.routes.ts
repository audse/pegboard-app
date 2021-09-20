import { createRouter, createWebHistory } from 'vue-router'
import store from './../store/index.store'
import AuthService from '../services/auth.service'

import Home from './../pages/Home.vue'
import SignUp from './../pages/Auth/SignUp/SignUp.vue'
import SignIn from './../pages/Auth/SignIn/SignIn.vue'

const routes = [
    { 
        name: 'Home',
        path: '/', 
        component: Home,
    },
    { 
        name: 'Sign Up',
        path: '/signup', 
        component: SignUp,
        meta: {
            requiresUnauth: true,
        }
    },
    { 
        name: 'Sign In',
        path: '/signin', 
        component: SignIn,
        meta: {
            requiresUnauth: true,
        }
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach( async (to, from, next) => {

    await new AuthService().loadCurrentUser()
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