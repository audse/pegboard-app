<template>

<section class="p-10">
    <h1 class="text-3xl font-extrabold pb-3">Log In</h1>
    <!-- <button @click="loginWithGoogle()" class="bg-blue-500 text-white rounded-full px-6 py-3">
        Log in with Google
    </button> -->
    <form @submit.prevent="loginWithEmail">
        <input type="text" name="username" v-model="loginData.username" class="border-2 border-gray-200" />
        <input type="password" name="password" v-model="loginData.password" class="border-2 border-gray-200" />
        <button type="submit" class="bg-blue-500 text-white rounded-full px-6 py-3">
            Log in
        </button>
    </form>

    <p>{{ $auth.user }}</p>

</section>

</template>
<script>

export default {

    data () {
        return {
            loginData: {
                username: null,
                password: null,
            },
            user: null,
        }
    },

    mounted () {

    },

    methods: {
        async loginWithEmail() {
            this.$auth.loginWith('local', {data: this.loginData}).then( result => {

                this.$auth.setUserToken(`Token ${result.data.key}`).then( () => {
                    console.log(this.$store.state)
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