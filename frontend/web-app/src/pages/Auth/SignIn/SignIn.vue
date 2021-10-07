<script lang="ts" setup>

import { reactive, computed, watch } from 'vue'
import { useRouter } from 'vue-router'

import { AuthService } from '@/services'

const router = useRouter()

const signInData = reactive({
    username: '',
    password: '',
})

const signIn = async ( data:{username:string,password:string} ) => {
    await AuthService.signIn( data ).then( (userResponse:object) => {
        router.push({ name: 'Home' })
    }).catch( (e:any) => {
        throw e
    })
}

</script>
<template>

<page-layout>

    <template #header>
        <h1>Sign In</h1>
    </template>

    <section class="page-padding">
            
        <form @submit.prevent="signIn(signInData)">

            <section class="flex items-center my-2">
                <label for="username" class="w-20">Username</label>
                <input v-model="signInData.username" name="username" type="text" />
            </section>
            <section class="flex items-center my-2">
                <label for="password" class="w-20">Password</label>
                <input v-model="signInData.password" name="password" type="password" />
            </section>
            <toolbar class="ml-20 pl-2">
                <co-button type="submit" color="emphasis">Sign In</co-button>
                <template #right>
                    <label class="text-right">Not signed up yet?</label>
                    <router-link :to="{ name: 'Sign Up' }">
                        <co-button subtle color="scale-text-500">Sign Up</co-button>
                    </router-link>
                </template>
            </toolbar>

        </form>

        

    </section>

</page-layout>

</template>
<script lang="ts">

export default {
    name: 'sign-in'
}

</script>