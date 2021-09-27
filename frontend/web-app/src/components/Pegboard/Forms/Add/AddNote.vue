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

const addNote = async (data:noteForm) => {
    await NoteService.create(data)
}
</script>
<template>
    
<!-- <h4>Add Note</h4> -->
<form @submit.prevent="addNote(addNoteForm)" class="flex items-center">
    <input v-model="addNoteForm.name" name="name" type="text" placeholder="Add Note" />
    <button type="submit">+</button>
</form>

</template>
<script lang="ts">

export default {
    name: 'AddNote'
}

</script>