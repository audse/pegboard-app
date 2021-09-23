
import Folders from './../pages/Pegboard/Folders.vue'
import Board from './../pages/Pegboard/Board.vue'

const pegboardRoutes = [
    { 
        name: 'Folders',
        path: '/folders', 
        component: Folders,
        meta: {
            requiresAuth: true,
            breadcrumb: (route:string) => ([
                { name: 'Home', path: '/' },
                { name: 'Folders' },
            ])
        }
    },
    { 
        name: 'Board',
        path: '/board/:id/:url', 
        component: Board,
        meta: {
            requiresAuth: true,
            breadcrumb: (route:string) => ([
                { name: 'Home', path: '/' },
                { name: 'Folders', path: '/folders' },
                { name: route.params.url, },
            ])
        }
    },
]

export default pegboardRoutes