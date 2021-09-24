
<template>

<article class="bg-gray-800 p-3 m-3">

    <section>
        <strong>{{ page.name }}</strong>
        {{ page.description }}
    </section>

    <section>
        <form @submit.prevent="addNote(addNoteForm, page.board, page.id)">
            <label for="name">Note Name</label>
            <input v-model="addNoteForm.name" name="name" type="text" />
            <button type="submit">Add Note</button>
        </form>
    </section>

    <section v-for="note in notes" :key="note.id">
        <view-note :note="note" />
    </section>
    
    <section>
        <edit-page :page="page" />
    </section>

</article>

</template>
<script lang="ts">

import ViewNote from './ViewNote.vue'

import { onMounted } from 'vue'

import useBoard from './../../mixins/useBoard'
import useNote from './../../mixins/useNote'
import EditPage from './Edit/EditPage.vue'


export default {

    name: 'ViewPage',

    components: {
        ViewNote,
        EditPage,
    },

    props: {
        page:Object,
    },

    setup ( props:{page:any} ) {

        const {
            notes,
            refreshNotes,
        } = useBoard()

        onMounted( () => {
            refreshNotes(props.page.board, props.page.id)
        })

        const {
            addNoteForm,
            addNote
        } = useNote()

        return {
            notes,
            addNoteForm,
            addNote
        }

    }

}

</script>