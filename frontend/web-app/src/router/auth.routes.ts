import { Route } from '@/types'
import { SignUp, SignUpSuccess, SignIn } from '@/pages'

const authRoutes:Array<Route> = [
    { 
        name: 'Sign Up',
        path: '/signup', 
        component: SignUp,
        meta: {
            requiresUnauth: true,
            breadcrumb: ( () => [
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
            breadcrumb: ( () => [
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
            breadcrumb: ( () => [
                { name: 'Home', path: '/' },
                { name: 'Sign In' }
            ])
        }
    },
]

export default authRoutes