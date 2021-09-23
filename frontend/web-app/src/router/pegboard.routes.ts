
import Folders from './../pages/Pegboard/Folders.vue'
import Board from './../pages/Pegboard/Board.vue'

const pegboardRoutes = [
    { 
        name: 'Folders',
        path: '/folders', 
        component: Folders,
        meta: {
            requiresAuth: true,
        }
    },
    { 
        name: 'Board',
        path: '/board/:id/:url', 
        component: Board,
        meta: {
            requiresAuth: true,
        }
    },
]

export default pegboardRoutes