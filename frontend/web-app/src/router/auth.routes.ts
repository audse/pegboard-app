import { SignUp, SignUpSuccess, SignIn } from '@/pages'

const authRoutes = [
    { 
        name: 'Sign Up',
        path: '/signup', 
        component: SignUp,
        meta: {
            requiresNoAuth: true,
            breadcrumb: ( () => [
                { name: 'Home', path: '/', icon: 'home-alt' },
                { name: 'Sign Up' }
            ])
        }
    },
    { 
        name: 'Sign Up Success',
        path: '/signup/success', 
        component: SignUpSuccess,
        meta: {
            requiresNoAuth: true,
            breadcrumb: ( () => [
                { name: 'Home', path: '/', icon: 'home-alt' },
                { name: 'Sign Up', path: '/signup', icon: 'user' },
                { name: 'Success' }
            ])
        }
    },
    { 
        name: 'Sign In',
        path: '/signin', 
        component: SignIn,
        meta: {
            requiresNoAuth: true,
            breadcrumb: ( () => [
                { name: 'Home', path: '/', icon: 'home-alt' },
                { name: 'Sign In' }
            ])
        }
    },
]

export default authRoutes