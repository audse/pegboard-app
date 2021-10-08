<script lang="ts" setup>

import { Theme } from '@/types'

const props = defineProps<{
    theme:Theme,
}>()

</script>
<template>
    
<card :bg="theme?.second" class="theme">

    <template #header>
        {{ theme.name }}
    </template>

</card>

</template>
<script lang="ts">
export default {
    name: 'theme'
}
</script>
<style scoped>

</style>