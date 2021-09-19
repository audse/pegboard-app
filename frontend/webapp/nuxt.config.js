export default {
    // Global page headers: https://go.nuxtjs.dev/config-head
    head: {
        title: 'pegboard',
        htmlAttrs: {
            lang: 'en'
        },
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width, initial-scale=1' },
            { hid: 'description', name: 'description', content: '' },
            { name: 'format-detection', content: 'telephone=no' }
        ],
        link: [
            { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
        ]
    },

    // Axios module configuration: https://go.nuxtjs.dev/config-axios
    axios: {
        baseURL: 'http://localhost:8000/api/',
    },
    
    auth: {
        strategies: {
            local: {
                token: {
                  property: 'token',
                  global: true,
                  type: 'Token'
                },
                user: {
                  property: ''
                },
                endpoints: {
                    login: { url: '/auth/login/', method: 'post', propertyName: 'access_token' },
                    logout: { url: '/auth/logout/', method: 'post' },
                    user: { url: '/auth/user/', method: 'get', propertyName: false, }
                },
                tokenType: 'access',
                tokenName: 'Token',
                
            }
        },
    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [
        '~/static/css/app.scss'
    ],

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [
        '~/plugins/composition-api.js'
    ],

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: true,

    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: [
        // https://go.nuxtjs.dev/tailwindcss
        '@nuxtjs/tailwindcss',
        '@nuxt/typescript-build'
    ],

    // Modules: https://go.nuxtjs.dev/config-modules
    modules: [
        // https://go.nuxtjs.dev/axios
        '@nuxtjs/axios',
        '@nuxtjs/auth-next',
    ],

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {
    }
}
