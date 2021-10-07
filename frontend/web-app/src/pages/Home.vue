<script lang="ts" setup>

import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

import { AuthService } from '@/services'

const router = useRouter()
const store = useStore()

const currentUser = ref(store.state.auth.currentUser)

const signOut = async () => {
    await AuthService.signOut().then( () => {
        router.push({ name: 'Sign In' })
    }).catch( (e:any) => {
        throw e
    })
}

</script>
<template>

<page-layout>

    <template #header>
        <toolbar v-if="currentUser">
            <h1>
                Welcome,
                <span class="text-alert">{{ currentUser.username }}.</span>
            </h1>

            <!-- <template #right>
                <co-button class="secondary" @click="signOut" subtle color="scale-text-300">Sign Out</co-button>
            </template> -->
        </toolbar>
        <section v-else>

            <router-link :to="{ name: 'Sign In' }">
                <a class="pr-4">Sign In</a>
            </router-link>
            <router-link :to="{ name: 'Sign Up' }">
                <a>Sign Up</a>
            </router-link>

        </section>
    </template>

    <section v-if="currentUser" class="flex items-center page-padding">

        <router-link :to="{ name: 'Folders' }">
            <card bg="primary" hover>
                <template #header>
                    <h2 class="px-2 text-center">
                        <icon lg icon="folder" />
                        <span class="block mt-2">Folders</span>
                    </h2>
                </template>
                <template #footer></template>
            </card>
        </router-link>

        <router-link :to="{ name: 'Folders' }">
            <card bg="primary" hover>
                <template #header>
                    <h2 class="px-2 text-center">
                        <icon lg icon="color-bucket" />
                        <span class="block mt-2">Themes</span>
                    </h2>
                </template>
                <template #footer></template>
            </card>
        </router-link>

    </section>
</page-layout>

</template>