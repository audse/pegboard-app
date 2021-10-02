<script lang="ts" setup>

import Expandable from '../../../Elements/Expandable.vue'
import SelectTags from '../Select/SelectTags.vue'
import AddChecklist from '../Add/AddChecklist.vue'

import { reactive, ref } from 'vue'

import NoteService from './../../../../services/note.service'
import ChecklistService from './../../../../services/checklist.service'

const props = defineProps({
    note: Object,
})

const editNoteForm = reactive({
    name: props.note.name,
    content: props.note.content,
    tags: props.note.tags,
    checklists: props.note.checklists
})

const editNote = async (noteId: string, data:any) => {
    if ( newChecklist.value ) {
        console.log(newChecklist.value)
        ChecklistService.create(newChecklist.value)
    }
    await NoteService.update(noteId, data)
}

const newChecklist = ref(null)
const updateChecklist = (event:object) => newChecklist.value = event

</script>
<template>
    
<section>
    <h3>Edit {{ note.name }}</h3>

    <form @submit.prevent="editNote(note.id, editNoteForm)">

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
            <add-checklist :noteId="note.id" @update-checklist="updateChecklist" />
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