<script lang="ts" setup>

import { computed } from 'vue'

import { Note } from '@/types'
import { Checklist } from '@/components'

const props = defineProps<{
    note:Note,
}>()

const emits = defineEmits([
    'show-modal'
])

const showModal = (event:any) => {
    event.stopPropagation()
    if ( !event.currentTarget.className.includes('checklists') ) {
        emits('show-modal')
    }
}

</script>
<template>
    
<card bg="main" hover @click="showModal">

    <template #header>
        <co-tag v-for="tag in note.tags" :key="tag.id" :label="tag.name" :tag="tag" />
        <strong class="block font-semibold mt-1">{{ note.name }}</strong>
    </template>

    <section @click="showModal" v-if="note.checklists.length > 0" class="checklists py-2 mt-2 border-scale-secondary-300 border-t">
        <checklist v-for="checklist in note.checklists" :checklist="checklist" :key="checklist.id" />
    </section>

</card>

</template>
<script lang="ts">

export default {
    name: 'note-checklist',
}

</script>