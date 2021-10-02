<script lang="ts" setup>

import Expandable from '../../../Elements/Expandable.vue'
import SelectTags from '../Select/SelectTags.vue'
import AddChecklist from '../Add/AddChecklist.vue'

import { reactive, ref } from 'vue'

import NoteService from './../../../../services/note.service'

const props = defineProps({
    note: Object,
})

const editNoteForm = reactive({
    name: props.note.name,
    content: props.note.content,
    tags: props.note.tags
})

const editNote = async (noteId: string, data:any, noteHasChecklist:boolean) => {
    if (noteHasChecklist) {
        // ChecklistService.create(checklistData...)
    }
    await NoteService.update(noteId, data)
}

const hasChecklist = ref(false)
const updateHasChecklist = (event:{value:boolean}) => hasChecklist.value = event.value

</script>
<template>
    
<section>
    <h3>Edit {{ note.name }}</h3>

    <form @submit.prevent="editNote(note.id, editNoteForm, hasChecklist)">

        <section class="pt-6 flex items-center">
            <label for="name" class="flex-none">Name</label>
            <input v-model="editNoteForm.name" name="name" type="text" />
        </section>

        <section class="pt-6 flex items-center">
            <label for="content" class="flex-none">Content</label>
            <textarea v-model="editNoteForm.content" name="content"></textarea>
        </section>

        <section class="pt-6 flex items-center">
            <label for="tags" class="flex-none">Add Tags</label>
            <select-tags v-model="editNoteForm.tags" />
        </section>

        <section class="pt-10">
            <add-checklist @has-checklist="updateHasChecklist" />
        </section>

        <section class="pt-8">
            <button type="submit" @click="this.$emit('save')" class="secondary">Save Edit</button>
        </section>
    </form>

</section>

</template>

<script lang="ts">

export default {
  components: { AddChecklist },
    name: 'EditNote',
}

</script>