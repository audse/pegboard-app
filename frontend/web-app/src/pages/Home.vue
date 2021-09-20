<template>

<nav>

<section v-if="currentUser">
    Welcome, {{ currentUser.username }}.

    <button class="secondary" @click="signOut">Sign Out</button>

</section>
<section v-else>

<router-link :to="{ name: 'Sign In' }">
    <a class="text-blue-500 pr-4">Sign In</a>
</router-link>
<router-link :to="{ name: 'Sign Up' }">
    <a class="text-blue-500">Sign Up</a>
</router-link>

</section>

</nav>

<h1>Hello world!</h1>

</template>
<script lang="ts">

import { reactive } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import AuthService from './../services/auth.service'

export default {
    setup () {

        const router = useRouter()
        const store = useStore()

        const currentUser = reactive(store.state.auth.currentUser)

        const signOut = async () => {
            await AuthService.signOut().then( () => {
                router.push({ name: 'Sign In' })
            }).catch( (e:any) => {
                throw e
            })
        }

        return {
            currentUser,
            signOut
        }

    }
}

</script>