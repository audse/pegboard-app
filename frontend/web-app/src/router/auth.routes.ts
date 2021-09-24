
import SignUp from './../pages/Auth/SignUp/SignUp.vue'
import SignUpSuccess from './../pages/Auth/SignUp/SignUp.success.vue'
import SignIn from './../pages/Auth/SignIn/SignIn.vue'

const authRoutes = [
    { 
        name: 'Sign Up',
        path: '/signup', 
        component: SignUp,
        meta: {
            requiresUnauth: true,
            breadcrumb: (route:string) => ([
                { name: 'Home', path: '/' },
                { name: 'Sign Up' }
            ])
        }
    },
    { 
        name: 'Sign Up Success',
        path: '/signup/success', 
        component: SignUpSuccess,
        meta: {
            requiresUnauth: true,
            breadcrumb: (route:string) => ([
                { name: 'Home', path: '/' },
                { name: 'Sign Up' }
            ])
        }
    },
    { 
        name: 'Sign In',
        path: '/signin', 
        component: SignIn,
        meta: {
            requiresUnauth: true,
            breadcrumb: (route:string) => ([
                { name: 'Home', path: '/' },
                { name: 'Sign In' }
            ])
        }
    },
]

export default authRoutes