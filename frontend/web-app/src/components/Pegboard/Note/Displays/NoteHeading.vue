<script lang="ts" setup>

import { computed } from 'vue'

import { Note } from '@/types'

const props = defineProps<{
    note:Note,
}>()

</script>
<template>

<card bg="primary" hover>

    <header class="my-4">
        <co-tag v-for="tag in note.tags" :key="tag.id" :label="tag.name" :color="tag.color.color" />
        <h3 class="font-semibold text-xl">
            {{ note.name }}
        </h3>
    </header>
    
</card>

</template>
<script lang="ts">

export default {
    name: 'note-heading',
}

</script>