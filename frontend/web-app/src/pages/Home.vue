<script lang="ts" setup>

import { reactive } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

import { AuthService } from '@/services'

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

</script>
<template>

<section v-if="currentUser">
    Welcome, {{ currentUser.username }}.

    <button class="secondary" @click="signOut">Sign Out</button>

    <router-link :to="{ name: 'Folders' }">
        <a>Go To Folders</a>
    </router-link>

</section>
<section v-else>
    <router-link :to="{ name: 'Sign In' }">
        <a class="pr-4">Sign In</a>
    </router-link>
    <router-link :to="{ name: 'Sign Up' }">
        <a>Sign Up</a>
    </router-link>
</section>

</template>