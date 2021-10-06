<script lang="ts" setup>

import { computed } from 'vue'

import { Note } from '@/types'

const props = defineProps<{
    note:Note,
}>()

</script>
<template>

<card bg="scale-text-50" hover>

    <header class="my-4">
        <co-tag v-for="tag in note.tags" :key="tag.id" :label="tag.name" :tag="tag" class="mr-2" />
        <h3 class="font-semibold text-xl py-2 tracking-wide">
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