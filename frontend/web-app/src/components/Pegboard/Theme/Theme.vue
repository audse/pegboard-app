<script lang="ts" setup>

import { Theme } from '@/types'

const props = defineProps<{
    theme:Theme,
}>()

</script>
<template>

<card :top-hex-bg="theme.second" :hex-bg="theme.scale_secondary[3]" class="theme">

    <template #header>
        <h3 class="theme pt-4 px-6 pb-4">
            {{ theme.name }}
        </h3>
    </template>

    <template #footer>
        
    </template>

</card>

</template>
<script lang="ts">
export default {
    name: 'theme'
}
</script>
<style scoped>

.theme {
    color: v-bind('theme.text');
}

</style>