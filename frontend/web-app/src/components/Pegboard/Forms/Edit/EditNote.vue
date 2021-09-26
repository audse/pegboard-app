<script lang="ts" setup>

import { reactive } from 'vue'

import NoteService from './../../../../services/note.service'

const props = defineProps({
    note: Object,
})

interface noteForm {
    name:string,
}

let editNoteForm:noteForm = reactive({
    name: props.note.name
})

const editBoard = async (noteId: string, data:noteForm) => {
    await NoteService.update(noteId, data)
}

</script>
<template>
    
<section class="pt-6">
    <p>Edit {{ note.name }}</p>
    <form @submit.prevent="editNote(note.id, editNoteForm)">
        <label for="name">Note Name</label>
        <input v-model="editNoteForm.name" name="name" type="text" />
        <button type="submit">Submit</button>
    </form>
</section>

</template>

<script lang="ts">

export default {
    name: 'EditNote',
}

</script>