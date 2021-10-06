<script lang="ts" setup>

import { Note } from '@/types'
import { EditNote, Checklist, Comments, AddComment } from '@/components'

const props = defineProps<{
    note:Note,
    show:boolean
}>()

const emits = defineEmits([
    'hide'
])

const slotLabel = `label-${props.note?.name}`
const slotSection = `section-${props.note?.name}`

</script>
<template>

<modal :show="show" :tabs="[note.name, 'Edit', 'Checklists']" @hide="$emit('hide')">

    <template v-slot:[slotSection]>
        <co-tag v-for="tag of note.tags" :key="tag.id" :tag="tag" :label="tag.name" />
        <h2 class="my-2">{{ note.name }}</h2>
        <p class="text-scale-text-700 w-2/3 mt-4 mb-10 content">{{ note.content }}</p>

        <card bg="scale-secondary-300" v-for="checklist of note.checklists" :key="checklist.id" class="w-2/3">
            <checklist :checklist="checklist" />
        </card>

        <card bg="scale-secondary-300">
            <comments :comments="note.comments" height-class="h-full" class="mt-4" />
            <span v-if="note.comments.length<1" class="text-scale-text-500">No comments here.</span>
            <div class="border-t-2 opacity-50 border-second my-4" />
            <add-comment :note="note" />
        </card>
    </template>

    <template #section-Edit>
        <edit-note :note="note" @save="$emit('hide')" />
    </template>

    <template #section-Checklists>
        <!-- <edit-checklist -->
    </template>

</modal>

</template>
<script lang="ts">

export default {
    name: 'note-modal'
}

</script>
<style>

.content {
    white-space: pre-line;
}

</style>