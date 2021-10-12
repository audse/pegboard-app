import { createRouter, createWebHistory } from 'vue-router'

import store from '@/store'
import { Board } from '@/types'
import { AuthService, BoardService, ThemeService } from '@/services'

import authRoutes from './auth.routes'
import pegboardRoutes from './pegboard.routes'

import { Home, Error } from '@/pages'

const routes = [
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
    {
        name: 'Error',
        path: '/error',
        component: Error,
        meta: {
            breadcrumb: ( () => [
                { name: 'Home', path: '/', icon: 'home-alt' },
                { name: 'Error' }
            ])
        }
    }
    
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

    // if ( to.name === 'Board' ) {
    //     const board:Board = await BoardService.retrieve(to.params.id[0])
    //     if (board.theme && board.theme !== store.state.themes.current.id ) {
    //         await ThemeService.retrieve(board.theme)
            // ThemeService.setTheme(store.state.themes.current)
    //     }
    // }

    if ( to.meta.requiresAuth && !isAuthenticated ) {
        next({ name: 'Sign In' })
    } else if ( to.meta.requiresNoAuth && isAuthenticated ) {
        next({ name: 'Home' })
    } else {
        next()
    }
})

export default router