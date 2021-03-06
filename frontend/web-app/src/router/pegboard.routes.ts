import { Folders, Board, Themes } from '@/pages'
import { RouteLocationNormalizedLoaded } from 'vue-router'

const pegboardRoutes = [
    { 
        name: 'Folders',
        path: '/folders', 
        component: Folders,
        meta: {
            requiresAuth: true,
            breadcrumb: ( () => [
                { name: 'home', path: '/', icon: 'home-alt' },
                { name: 'folders', icon: 'folder' },
            ])
        }
    },
    { 
        name: 'Board',
        path: '/board/:id/:url', 
        component: Board,
        meta: {
            requiresAuth: true,
            breadcrumb: ( (route:RouteLocationNormalizedLoaded) => route?[
                { name: 'home', path: '/', icon: 'home-alt' },
                { name: 'folders', path: '/folders', icon: 'folder' },
                { name: route.params.url, icon: 'clipboard' },
            ]:undefined)
        }
    },
    {
        name: 'Themes',
        path: '/themes',
        component: Themes,
        meta: {
            requiresAuth: true,
            breadcrumb: ( () => [
                { name: 'home', path: '/', icon: 'home-alt' },
                { name: 'themes', icon: 'color-bucket' },
            ])
        }
    }
]

export default pegboardRoutes