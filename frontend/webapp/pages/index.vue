<template>

<section>
    
    <h1 class="text-3xl font-extrabold pb-3">Pegboard <small class="text-3xl font-medium pl-1">Home</small></h1>

    <NuxtLink to="login">
        <button class="bg-white text-blue-500 px-6 py-3 rounded-full">Log In</button>
    </NuxtLink>
    <NuxtLink to="signup">
        <button class="bg-blue-500 text-white px-6 py-3 rounded-full">Sign Up</button>
    </NuxtLink>

</section>

</template>

<script>

export default {
    
    data () { return {

    }},

    middleware: 'unauth',

    methods: {
        async logout () {
            this.$auth.logout().then( results => {
                console.log('Successfully logged out.', results)
            }).catch( e => {
                throw e
            })
        }
    }
}

</script>
