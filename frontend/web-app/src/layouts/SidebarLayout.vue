<script lang="ts" setup>

import { computed, ref, watch } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

import { AuthService } from '@/services'
import { FolderList } from '@/components'

const store = useStore()
const router = useRouter()

const isAuthenticated = computed( () => store.getters['auth/isAuthenticated'] )
const currentUser = computed( () => store.state.auth.currentUser )

const folders = computed( () => store.state.folders.folders )

const hidden = ref( store.state.auth.preferences.sidebarHidden )

watch( hidden, () => {
    store.commit('auth/setSidebarHiddenPreference', hidden)
})

const signOut = async () => {
    await AuthService.signOut().then( () => {
        router.push({ name: 'Sign In' })
    }).catch( (e:any) => {
        throw e
    })
}

</script>
<template>
    
<aside :class="[hidden?'lg:w-10 w-72':'w-72', 'sidebar bg-main']">

    <section v-if="!hidden" class="w-72 sidebar-main flex flex-col justify-between overflow-hidden h-full flex-none">

        <section v-if="isAuthenticated" class="pt-6">
            <h3 class="pb-1 px-4 text-text">Pegboard</h3>
            <h4 class="px-4 text-scale-text-700">
                Welcome, 
                <strong class="font-medium text-alert">{{ currentUser?.username }}</strong>.
            </h4>

            <ul class="pt-4 routes">
                <li class="mx-4 my-1">
                    <router-link class="route" v-slot="{ isActive }" to="/">
                        <co-button :subtle="!isActive" :light="isActive" :color="isActive?'emphasis':'scale-text-500'" icon="home-alt">Home</co-button>
                    </router-link>
                </li>
                <li class="mx-4 my-1">
                    <router-link class="route" v-slot="{ isActive }" to="/folders">
                        <co-button :subtle="!isActive" :light="isActive" :color="isActive?'emphasis':'scale-text-500'" icon="folder">Folders</co-button>
                    </router-link>
                </li>
                <li class="mx-4 my-1">
                    <router-link class="route" v-slot="{ isActive }" to="/themes">
                        <co-button :subtle="!isActive" :light="isActive" :color="isActive?'emphasis':'scale-text-500'" icon="color-bucket">Themes</co-button>
                    </router-link>
                </li>

                <div class="border-t-2 opacity-50 border-second mx-4 mt-6" />

                <folder-list />
            
            </ul>
        </section>
        <section v-else class="py-6 px-4">
            <h3 class="pb-1 text-text">
                <span class="text-alert">Pegboard</span>
            </h3>

            <router-link :to="{ name: 'Home' }">
                <co-button color="scale-text-500" light class="my-2">Home</co-button>
            </router-link>
            <router-link :to="{ name: 'Sign In' }">
                <co-button color="emphasis" light class="my-2">Sign In</co-button>
            </router-link>
            <router-link :to="{ name: 'Sign Up' }">
                <co-button color="emphasis" light class="my-2">Sign Up</co-button>
            </router-link>

        </section>

        <section class="w-full secret-links">
            <co-button v-if="isAuthenticated" @click="signOut" subtle left color="scale-text-300">Sign Out</co-button>
            <a href="http://localhost:8000/admin"><co-button subtle left color="scale-text-300">Admin</co-button></a>
        </section>

    </section>
    <section @click="hidden=!hidden" class="w-10 absolute right-0 top-0 items-center justify-center h-full hidden lg:flex sidebar-hidden">
        <button class="sidebar-hidden-button pb-10">
            <switch-icon :switch="hidden" icon-true="chevron-double-right" icon-false="chevron-double-left" />
        </button>
    </section>

</aside>

</template>
<script lang="ts">

export default {
    name: 'sidebar-layout'
}

</script>
<style scoped>

.sidebar {
    @apply border-second border-r;
    isolation: isolate;
    z-index: 900;
}

.sidebar-main {
    z-index: 1;
}

.sidebar-hidden {
    z-index: 10;
    height: 100%;
}

.sidebar-hidden:hover {
    @apply backdrop-filter backdrop-invert-5;
    transition: all 100ms;
    transition-delay: 25ms;
}

.sidebar-hidden-button {
    padding: 2pt;
    margin: 2pt;
    color: var(--text);
    background: none;
}

.secret-links {
    @apply pb-4 px-2;
}

.secret-links a {
    @apply block px-2 py-1;
}

.routes {
    @apply flex flex-col w-full;
}

</style>