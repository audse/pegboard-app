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
    
<aside :class="[hidden?'w-10':'w-72', 'sidebar bg-scale-secondary-100']">

    <section v-if="!hidden" class="w-72 sidebar-main flex flex-col justify-between overflow-hidden h-full flex-none">

        <section v-if="isAuthenticated" class="pt-6">
            <h3 class="pb-1 px-4 text-text">Pegboard</h3>
            <h4 class="px-4 text-scale-text-4">
                Welcome, 
                <strong class="font-normal">{{ currentUser?.username }}</strong>.
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
    <section @click="hidden=!hidden" class="w-10 absolute right-0 top-0 flex items-center justify-center h-full md:hidden lg:flex sidebar-hidden">
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
    @apply border-primary border-r;
    isolation: isolate;
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
    @apply border-l-4 border-emphasis;
    transition: border 250ms;
}

</style>