<template>

<section class="p-10">
    <h1 class="text-3xl font-extrabold pb-3">Log In</h1>
    
    <form @submit.prevent="loginWithEmail">
        <section>
            <label for="username">Username</label>
            <input type="text" name="username" v-model="loginData.username" />
        </section>
        <section>
            <label for="password">Password</label>
            <input type="password" name="password" v-model="loginData.password" />
        </section>
        <section>
            <button type="submit" class="bg-blue-500 text-white rounded-full px-6 py-3">
                Log in
            </button>
            <NuxtLink to="signup">
                <button class="bg-white text-blue-500 px-6 py-3 rounded-full">Sign Up</button>
            </NuxtLink>
        </section>
    </form>

</section>

</template>
<script>

export default {

    data () { return {
        loginData: {
            username: null,
            password: null,
        },
    }},

    middleware: 'unauth',

    methods: {
        async loginWithEmail () {
            this.$auth.loginWith('local', {data: this.loginData}).then( result => {
                this.$auth.setUserToken(`Token ${result.data.key}`).then( () => {
                    console.log('Successfully logged in.')
                }).catch( e => {
                    throw e
                })
            }).catch( e => {
                throw e
            })
        }
    },
};

</script>