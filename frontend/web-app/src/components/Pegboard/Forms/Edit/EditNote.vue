<script lang="ts" setup>

import { reactive } from 'vue'

import NoteService from './../../../../services/note.service'

const props = defineProps({
    note: Object,
})

const editNoteForm = reactive({...props.note})

const editNote = async (noteId: string, data:object) => {
    await NoteService.update(noteId, data)
}

</script>
<template>
    
<section>
    <h3>Edit {{ note.name }}</h3>

    <form @submit.prevent="editNote(note.id, editNoteForm)">

        <section class="pt-4 flex items-center">
            <label for="name" class="flex-none">Name</label>
            <input v-model="editNoteForm.name" name="name" type="text" />
        </section>

        <section class="pt-4 flex items-center">
            <label for="content" class="flex-none">Content</label>
            <textarea v-model="editNoteForm.content" name="content"></textarea>
        </section>

        <section class="pt-8">
            <button type="submit" class="secondary">Save Edit</button>
        </section>
    </form>

</section>

</template>

<script lang="ts">

export default {
    name: 'EditNote',
}

</script>