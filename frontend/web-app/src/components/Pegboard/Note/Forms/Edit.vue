<script lang="ts" setup>

import { reactive, Ref, ref } from 'vue'

import { SelectTags, AddChecklist } from '@/components'
import { NoteService, ChecklistService } from '@/services'
import { Note } from '@/types/pegboard.types'

const props = defineProps<{
    note:Note,
}>()

const emits = defineEmits([
    'save'
])

const editNoteForm = reactive({
    name: props.note.name,
    content: props.note.content,
    tags: props.note.tags,
    checklists: props.note.checklists
})


const newChecklist:Ref = ref(null)
const updateChecklist = (event:object) => newChecklist.value = event

const editNote = async (noteId: string, data:any) => {
    if ( newChecklist.value ) {
        console.log(newChecklist.value)
        ChecklistService.create(newChecklist.value)
    }
    await NoteService.update(noteId, data)
}

const archiveNote = async(noteId:number) => {
    await NoteService.archive(noteId)
}

</script>
<template>
    
<section>
    <h3>{{ note.name }}</h3>

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

        <section class="pt-8">
            <button @click.prevent="archiveNote(note.id);this.$emit('save')" class="bg-transparent text-red-500">Archive</button>
        </section>
    </form>

</section>

</template>

<script lang="ts">

export default {
    name: 'EditNote',
}

</script>