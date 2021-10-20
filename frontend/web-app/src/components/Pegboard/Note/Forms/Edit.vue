<script lang="ts" setup>

import { reactive, Ref, ref } from 'vue'

import { SelectTags, AddChecklist } from '@/components'
import { NoteService, ChecklistService } from '@/services'
import { Note, Board } from '@/types'

const props = defineProps<{
    note:Note,
}>()

const emits = defineEmits([
    'save'
])

const displayChoices = [
    { value: 'n', key: 'Note' },
    { value: 'h', key: 'Heading' },
    // { value: 'i', key: 'Image' },
    { value: 'c', key: 'Checkbox' },
    // { value: 'a', key: 'Assignee' },
    { value: 'r', key: 'Readme' },
    { value: 's', key: 'Small' },
    { value: 'l', key: 'Checklist' },
    // { value: 'd', key: 'Date' },
    // { value: 'o', key: 'Countdown' },
    { value: 't', key: 'Discussion' },
    
]

const editNoteForm = reactive({
    name: props.note.name,
    content: props.note.content,
    tags: props.note.tags,
    checklists: props.note.checklists,
    display: props.note.display
})

const newChecklist:Ref = ref(null)
const updateChecklist = (event:object) => newChecklist.value = event

const editNote = async (noteId:number, data:Note) => {
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
    <h3 class="flex flex-col md:flex-row md:items-center">
        <span class="text-scale-text-500 block w-20">Edit</span>
        <span class="block md:pl-5">{{ note.name }}</span>
    </h3>

    <form @submit.prevent="editNote(note.id, editNoteForm)">

        <section class="pt-8 flex flex-col md:flex-row md:items-center">
            <label for="name" class="flex-none w-20 my-1 md:my-0">
                Name
                <small class="text-danger">Required.</small>
            </label>
            <input v-model="editNoteForm.name" name="name" type="text" class="py-2" />
        </section>

        <section class="pt-6 md:pt-2 flex flex-col md:flex-row md:items-center">
            <label for="content" class="flex-none w-20 my-1 md:my-0">Content</label>
            <textarea v-model="editNoteForm.content" name="content"></textarea>
        </section>

        <section class="pt-4 flex flex-col md:flex-row md:items-center">
            <label for="display" class="flex-none w-20 my-1 md:my-0">Display</label>
            <div class="select-control">
                <select v-model="editNoteForm.display" name="display" class="bg-scale-text-100">
                    <option v-for="choice of displayChoices" :key="choice.value" :value="choice.value">
                        {{ choice.key }}
                    </option>
                </select>
            </div>
        </section>

        <section class="pt-4 flex flex-col md:flex-row md:items-center">
            <label for="tags" class="flex-none w-20">Tags</label>
            <select-tags v-model="editNoteForm.tags" />
        </section>

        <section class="pt-16">
            <add-checklist :note="note" @update-checklist="updateChecklist" />
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
    name: 'edit-note',
}

</script>