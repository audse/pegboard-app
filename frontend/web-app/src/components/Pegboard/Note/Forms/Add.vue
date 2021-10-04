<script lang="ts" setup>

import { reactive } from 'vue'

import { NoteService } from '@/services'

const props = defineProps({
    boardId: Number,
    pageId: Number,
})

const addNoteForm = reactive({
    name: '',
    board: props.boardId || null,
    page: props.pageId || null,
})

const addNote = async (data:object) => {
    await NoteService.create(data)
    addNoteForm.name = ''
}
</script>
<template>
    
<!-- <h4>Add Note</h4> -->
<form @submit.prevent="addNote(addNoteForm)" class="flex items-center mx-2 mt-2">
    <input v-model="addNoteForm.name" name="name" type="text" placeholder="Add Note" class="bg-scale-secondary-300" />
    <co-button icon="math-plus" subtle color="alert" type="submit" class="ml-1"></co-button>
</form>

</template>
<script lang="ts">

export default {
    name: 'AddNote'
}

</script>