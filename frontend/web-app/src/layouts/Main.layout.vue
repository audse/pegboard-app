<template>

<div>
<nav class="px-3 pt-5 pb-2">
    <a href="http://localhost:3000/" class="text-blue-500">Home</a>
    <a href="http://localhost:8000/admin" class="text-blue-500">Django Admin</a>
    <a href="http://localhost:8000/api" class="text-blue-500">API Root</a>

    <section class="py-3">
        <span v-for="link in breadcrumbs" :key="link.name" class="text-sm">
            <span v-if="link.path">
                <router-link :to="link.path">{{ link.name }}</router-link>
                <small class="sm text-gray-500"> > </small>
            </span>
            <span v-else class="px-4">{{ link.name }}</span>
        </span>
    </section>
</nav>
<main class="p-3">
    <slot></slot>
</main>

<footer class="h-40">

</footer>
</div>

</template>
<script>

import { computed } from 'vue'
import { useRoute } from 'vue-router'

export default {
    name: 'MainLayout',

    setup () {

        const route = useRoute()

        const breadcrumbs = computed(() => {
          return route.meta.breadcrumb ? route.meta.breadcrumb(route) : []
        })

        return {
            breadcrumbs
        }

    }
}

</script>