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
            Example Theme
        </h3>
    </template>

    <section class="m-2">
        <card :hex-bg="theme.main" :top-hex-bg="theme.scale_secondary[1]" class="my-2">
            <template #header>
                <strong class="block mb-2">Example Note</strong>
            </template>
            <p :style="{color:theme.scale_text[4]}">
                Some note content.
            </p>
            <template #footer>
                <co-tag :color="theme.emphasis" label="Emphasis" />
                <co-tag :color="theme.alert" label="Alert" />
                <co-tag :color="theme.danger" label="Danger" />
            </template>
        </card>
    </section>

    <template #footer>
        
    </template>

</card>

</template>
<script lang="ts">
export default {
    name: 'example-theme'
}
</script>
<style scoped>

.theme {
    color: v-bind('theme.text');
}

</style>