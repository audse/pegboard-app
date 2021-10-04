
import Folders from '@/pages/Pegboard/Folders.vue'
import Board from '@/pages/Pegboard/Board.vue'

const pegboardRoutes = [
    { 
        name: 'Folders',
        path: '/folders', 
        component: Folders,
        meta: {
            requiresAuth: true,
            breadcrumb: () => ([
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
            breadcrumb: (route:{params:{id:number,url:string}}) => ([
                { name: 'home', path: '/', icon: 'home-alt' },
                { name: 'folders', path: '/folders', icon: 'folder' },
                { name: route.params.url, icon: 'clipboard' },
            ])
        }
    },
]

export default pegboardRoutes