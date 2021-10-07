<script lang="ts" setup>

import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const breadcrumbs = computed( () => {
    return route.meta.breadcrumb ? route.meta.breadcrumb(route) : []
})

</script>
<template>

<toolbar align-top no-col class="px-4 lg:pl-6 lg:pr-10 pt-8 pb-4 bg-scale-secondary-100">

    <template #icon>
        <slot />
    </template>

    <template #default>
    <div v-for="link of breadcrumbs" :key="link.name" class="mb-2 lg:my-0">

        <span v-if="link.path" class="flex items-center">
            <router-link :to="link.path" class="flex items-center mx-1">
                <co-button :icon="link.icon" subtle color="alert" sm>
                    {{ link.name }}
                </co-button>
            </router-link>

            <span class="sm opacity-30 px-3 flex-1"> / </span>
        </span>
        <span v-else class="flex items-center mx-1">
            <co-button :icon="link.icon" light color="alert" sm>
                {{ link.name }}
            </co-button>
        </span>
    </div>
    </template>

</toolbar>

</template>
<script lang="ts">

export default {
    name: 'navbar-layout',
}

</script>