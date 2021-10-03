<script lang="ts" setup>

import { computed, ref, watch } from 'vue'
import { useStore } from 'vuex'

const store = useStore()

const isAuthenticated = computed( () => store.getters['auth/isAuthenticated'] )
const currentUser = computed( () => store.state.auth.currentUser )

const folders = computed( () => store.state.folders.folders )

const hidden = ref( store.state.auth.preferences.sidebarHidden )

watch( hidden, () => {
    store.commit('auth/setSidebarHiddenPreference', hidden)
})

</script>
<template>
    
<aside :class="[hidden?'w-8':'w-80', 'sidebar background-scale-secondary-1 flex']">

    <section v-if="!hidden" class="w-72 flex flex-col justify-between overflow-hidden h-full flex-none">

        <section v-if="isAuthenticated" class="pt-6">
            <h3 class="pb-1 px-4">Pegboard</h3>
            <h4 class="px-4">
                Welcome, 
                <strong class="font-normal text-scale-text-4">{{ currentUser?.username }}</strong>.
            </h4>

            <ul class="pt-4 routes">
                <li><router-link class="route" active-class="active" to="/">Home</router-link></li>
                <li><router-link class="route" active-class="active" to="/folders">Folders</router-link></li>
            </ul>
        </section>
        <section v-else>
            ...
        </section>

        <section class="w-full secret-links">
            <a href="http://localhost:3000/">Home</a>
            <a href="http://localhost:8000/admin">Django Admin</a>
            <a href="http://localhost:8000/api">API Root</a>
        </section>

    </section>
    <section @click="hidden=!hidden" class="flex items-center justify-center h-full md:hidden lg:flex sidebar-hidden">
        <button class="sidebar-hidden-button pb-10">
            <i v-if="hidden" class="gg-chevron-double-right"></i>
            <i v-if="!hidden" class="gg-chevron-double-left"></i>
        </button>
    </section>

</aside>

</template>
<script lang="ts">

export default {
    name: 'Sidebar'
}

</script>
<style scoped>

.sidebar {
    border-right: 1px solid var(--secondary);
}

.sidebar-hidden:hover {
    background: var(--scale-secondary-2);
    transition: background 200ms;
}

.sidebar-hidden-button {
    padding: 2pt;
    margin: 2pt;
    color: var(--text);
    background: none;
}

.secret-links {
    @apply pb-4;
}

.secret-links a {
    @apply block px-2 py-1;
}

.routes {
    @apply flex flex-col w-full;
}

.route {
    @apply block px-4 py-2 w-full;
}

.active {
    background: var(--scale-secondary-3);
}

</style>