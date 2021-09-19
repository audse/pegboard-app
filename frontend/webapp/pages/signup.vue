<template>

<section class="p-10">
    <h1 class="text-3xl font-extrabold pb-3">Sign Up</h1>

    <form @submit.prevent="signUpWithEmail">
        <section>
            <label for="username">Username</label>
            <input type="text" name="username" v-model="signUpData.username" />
        </section>
        <section>
            <label for="email">Email</label>
            <input type="email" name="email" v-model="signUpData.email" />
        </section>
        <section>
            <label for="password">Password</label>
            <input type="password" name="password" v-model="signUpData.password1" />
        </section>
        <section>
            <label for="confirmPassword">Confirm Password</label>
            <input type="password" name="confirmPassword" v-model="signUpData.password2" />
        </section>
        <section>
            <button type="submit" class="bg-blue-500 text-white rounded-full px-6 py-3">
                Sign Up
            </button>
            <NuxtLink to="login">
                <button class="bg-white text-blue-500 px-6 py-3 rounded-full">Log In</button>
            </NuxtLink>
        </section>
    </form>

</section>

</template>
<script>

export default {

    data () { return {
        signUpData: {
            username: null,
            email: null,
            password1: null,
            password2: null,
        },
    }},

    middleware: 'unauth',

    methods: {

        async signUpWithEmail () {
            this.$axios.$post('auth/signup/', this.signUpData).then( response => {
                this.$nuxt.$router.push('/success/signup')
            }).catch( e => {
                throw e
            })
        }

    }

}

</script>