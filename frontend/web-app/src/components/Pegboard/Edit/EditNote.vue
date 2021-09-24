<template>
    
<section class="pt-6">
    <h3>Edit {{ note.name }}</h3>
    <form @submit.prevent="editNote(note.id, editNoteForm)">
        <label for="name">Note Name</label>
        <input v-model="editNoteForm.name" name="name" type="text" />
        <button type="submit">Submit</button>
    </form>
</section>

</template>

<script lang="ts">

import { computed } from 'vue'

import useNote from './../../../mixins/useNote'

export default {

    name: 'EditNote',

    props: {
        note: Object,
    },

    setup ( props:{note:object} ) {

        const {
            editNote
        } = useNote()

        const editNoteForm = computed( () => Object.assign({}, props.note))

        return {
            editNote,
            editNoteForm,
        }

    }
}

</script>