<script lang="ts" setup>

import { reactive } from 'vue'
import { useRouter } from 'vue-router'

import { AuthService } from '@/services'

const router = useRouter()

interface signUpData {
    username:string,
    email:string,
    password1:string,
    password2:string
}

const signUpData = reactive({
    username: '',
    email: '',
    password1: '',
    password2: '',
})

const signUpWithEmail = async ( data:signUpData ) => {
    AuthService.signUpWithEmail( data ).then( (response:object) => {
        router.push({ name: 'Sign Up Success' })
    }).catch( (e:any) => {
        throw e
    })
}

</script>
<template>

<page-layout>

    <template #header>
        <h1>Sign Up</h1>
    </template>

    <section class="page-padding">

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

    </section>
</page-layout>

</template>

<script lang="ts">
export default {
    name: 'SignUp', 
}
</script>