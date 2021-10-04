<script lang="ts" setup>

import { Note } from '@/types'
import {
    NoteAssignee,
    NoteCheckbox,
    NoteChecklist,
    NoteCountdown,
    NoteDate,
    NoteDefault,
    NoteDiscussion,
    NoteHeading,
    NoteImage,
    NoteReadme,
    NoteSmall,
    
    EditNote, NoteModal
} from '@/components'

import { ref } from 'vue'

const props = defineProps<{
    note:Note,
}>()

const showModal = ref(false)

</script>
<template>

<note-checklist v-if="note.display==='l'" :note="note" @click="showModal=true" />
<note-default v-if="note.display==='n'" :note="note" @click="showModal=true" />
<note-discussion v-if="note.display==='t'" :note="note" @show-modal="showModal=true" />
<note-heading v-if="note.display==='h'" :note="note" @click="showModal=true" />

<note-modal :note="note" :show="showModal" @hide="showModal=false" />

</template>
<script lang="ts">

export default {
    name: 'note'
}

</script>

        NoteDiscussion