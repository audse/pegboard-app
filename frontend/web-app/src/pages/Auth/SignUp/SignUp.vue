<template>

<form @submit.prevent="signUpWithEmail(signUpData)">

<section>
    <label for="username">Username</label>
    <input v-model="signUpData.username" name="username" type="text" />
</section>
<section>
    <label for="email">Email</label>
    <input v-model="signUpData.email" name="email" type="email" />
</section>
<section>
    <label for="password">Password</label>
    <input v-model="signUpData.password1" name="password" type="password" />
</section>
<section>
    <label for="confirmPassword">Confirm Password</label>
    <input v-model="signUpData.password2" name="confirmPassword" type="password" />
</section>
<section>
    <button type="submit">Sign Up</button>
</section>
</form>

<label>Already signed up?</label>
<router-link :to="{ name: 'Sign In' }">
    <button class="secondary">Sign In</button>
</router-link>


</template>

<script lang="ts">

import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import AuthService from './../../../services/auth.service'

export default {
    name: 'SignUp',

    setup () {

        const router = useRouter()

        const signUpData = reactive({
            username: '',
            email: '',
            password1: '',
            password2: '',
        })

        const auth = new AuthService()

        const signUpWithEmail = async ( data:object ) => {
            auth.signUpWithEmail( data ).then( (response:object) => {
                router.push({ name: 'Sign Up Success' })
            }).catch( (e:any) => {
                throw e
            })
        }

        return {
            signUpData,
            signUpWithEmail
        }
    }
}

</script>