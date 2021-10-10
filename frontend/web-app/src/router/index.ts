import { createRouter, createWebHistory } from 'vue-router'

import { Route, Theme } from '@/types'
import store from '@/store'
import { AuthService, BoardService, ThemeService } from '@/services'

import authRoutes from './auth.routes'
import pegboardRoutes from './pegboard.routes'

import Home from '@/pages/Home.vue'

const routes:Array<Route> = [
    { 
        name: 'Home',
        path: '/', 
        component: Home,
        meta: {
            breadcrumb: ( () => [
                { name: 'Home' },
            ])
        }
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

    if ( to.name === 'Board' ) {
        const board = await BoardService.retrieve(to.params.id[0])
        if (board.theme) {
            await ThemeService.retrieve(board.theme)
            ThemeService.setTheme(store.state.themes.current)
        }
    }

    if ( to.meta.requiresAuth && !isAuthenticated ) {
        next({ name: 'Sign In' })
    } else if ( to.meta.requiresUnauth && isAuthenticated ) {
        next({ name: 'Home' })
    } else {
        next()
    }
})

export default router