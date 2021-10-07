<script lang="ts" setup>

import parseISO from 'date-fns/parseISO'
import format from 'date-fns/format'

import { Note } from '@/types'
import { EditNote, Checklist, EditChecklist, Comments, AddComment } from '@/components'

const props = defineProps<{
    note:Note,
    show:boolean
}>()

const emits = defineEmits([
    'hide'
])

const slotLabel = `label-${props.note?.name}`
const slotSection = `section-${props.note?.name}`

const noteDate = format(parseISO(props.note.date_created), 'MMM d, h:mm aaaa') || ''

</script>
<template>

<modal :show="show" :tabs="[note.name, 'Edit', 'Checklists']" @hide="$emit('hide')">

    <template v-slot:[slotSection]>
        <co-tag v-for="tag of note.tags" :key="tag.id" :tag="tag" :label="tag.name" />
        <h2 class="mt-2">{{ note.name }}</h2>
        <small class="block text-scale-text-500 mb-4">{{ noteDate }}</small>
        <p class="text-scale-text-700 md:w-2/3 mt-4 whitespace-pre-line">{{ note.content }}</p>

        <h3 v-if="note.checklists.length>0" class="mt-12 mb-2">Checklists</h3>
        <card bg="scale-secondary-300" v-for="checklist of note.checklists" :key="checklist.id" class="w-2/3">
            <checklist :checklist="checklist" />
        </card>

        <h3 class="mt-12 mb-2">Comments</h3>
        <card bg="scale-secondary-300">
            <comments :comments="note.comments" :note="note" height-class="h-full" class="my-4" />
            <span v-if="note.comments.length<1" class="block mb-4 text-scale-text-700">No comments here.</span>
        </card>
        <add-comment :note="note" class="mx-2" />
    </template>

    <template #section-Edit>
        <edit-note :note="note" @save="$emit('hide')" />
    </template>

    <template #section-Checklists>
        <edit-checklist v-for="checklist in note.checklists" :key="checklist.id" :checklist="checklist" class="mb-6" />
    </template>

</modal>

</template>
<script lang="ts">

export default {
    name: 'note-modal'
}

</script>