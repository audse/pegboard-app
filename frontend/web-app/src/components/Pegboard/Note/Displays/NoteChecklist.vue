<script lang="ts" setup>

import { computed } from 'vue'

import { Note } from '@/types'
import { Checklist } from '@/components'

const props = defineProps<{
    note:Note,
}>()

</script>
<template>
    
<card bg="primary" hover>

    <template #header>
        <co-tag v-for="tag in note.tags" :key="tag.id" :label="tag.name" :color="tag.color.color" />
        <strong class="block font-semibold mt-1">{{ note.name }}</strong>
    </template>

    <section v-if="note.checklists.length > 0" class="py-2 mt-2 border-scale-secondary-300 border-t">
        <checklist v-for="checklist in note.checklists" :checklist="checklist" :key="checklist.id" />
    </section>

</card>

</template>
<script lang="ts">

export default {
    name: 'note-checklist',
}

</script>