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
        </toolbar>
        <section v-else>

            <h1>Welcome to <span class="text-alert">Pegboard.</span></h1>

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
    <section v-else class="flex items-center page-padding">
        <router-link :to="{ name: 'Sign In' }">
            <card bg="primary" hover>
                <template #header>
                    <h2 class="px-2 text-center">
                        <icon lg icon="user" />
                        <span class="block mt-2">Sign In</span>
                    </h2>
                </template>
                <template #footer></template>
            </card>
        </router-link>
        <router-link :to="{ name: 'Sign Up' }">
            <card bg="scale-text-100" hover>
                <template #header>
                    <h2 class="px-2 text-center">
                        <icon lg icon="user-add" />
                        <span class="block mt-2">Sign Up</span>
                    </h2>
                </template>
                <template #footer></template>
            </card>
        </router-link>
    </section>

</page-layout>

</template>