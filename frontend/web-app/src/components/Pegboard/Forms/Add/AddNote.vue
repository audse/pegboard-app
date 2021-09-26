<script lang="ts" setup>

import { reactive } from 'vue'

import NoteService from './../../../../services/note.service'

const props = defineProps({
    boardId: Number,
    pageId: Number,
})

interface noteForm {
    name:string,
    board:number|undefined,
    page:number|undefined,
}

let addNoteForm:noteForm = reactive({
    name: '',
    board: props.boardId || undefined,
    page: props.pageId || undefined,
})

const addBoard = async (boardId: string, data:noteForm) => {
    await NoteService.create(data)
}
</script>
<template>
    
<form @submit.prevent="addNote(addNoteForm, folder.id)">
    <label for="name">Note Name</label>
    <input v-model="addNoteForm.name" name="name" type="text" />
    <button type="submit">Add Note</button>
</form>

</template>
<script lang="ts">

export default {
    name: 'AddNote'
}

</script>