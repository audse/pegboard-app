<script lang="ts" setup>

import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const breadcrumbs = computed( () => {
    return route.meta.breadcrumb ? route.meta.breadcrumb(route) : []
})

</script>
<template>

<nav class="pl-6 pr-10 pt-8 pb-4 bg-scale-secondary-100 flex items-center">

    <slot></slot>

    <div v-for="link of breadcrumbs" :key="link.name">
        <span v-if="link.path" class="flex items-center">
            <router-link :to="link.path" class="pl-4 lg:pl-0 flex items-center">
                <i :class="[`gg-${link.icon}`, 'flex-1 block mr-1 pt-1']"></i>
                {{ link.name }}
            </router-link>
            <span class="sm opacity-30 px-3 flex-1"> / </span>
        </span>
        <span v-else class="flex items-center">
            <i :class="[`gg-${link.icon}`, 'flex-1 block mr-1 pt-1']"></i>
            {{ link.name }}
        </span>
    </div>
    
</nav>

</template>
<script lang="ts">

export default {
    name: 'Navbar',
}

</script>