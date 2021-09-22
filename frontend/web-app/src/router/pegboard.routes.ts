
import Folders from './../pages/Pegboard/Folders.vue'

const pegboardRoutes = [
    { 
        name: 'Folders',
        path: '/folders', 
        component: Folders,
        meta: {
            requiresAuth: true,
        }
    },
]

export default pegboardRoutes