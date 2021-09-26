<script lang="ts" setup>

import ViewNote from './ViewNote.vue'
import EditPage from './Forms/Edit/EditPage.vue'
import AddNote from './Forms/Add/AddNote.vue'

import { onMounted } from 'vue'

const props = defineProps({
    page: Object,
})

</script>
<template>

<article class="bg-gray-800 p-3 m-3">

    <section>
        <strong>{{ page.page.name }}</strong>
        {{ page.page.description }}
    </section>

    <section>
        <add-note :page-id="page.page.id" :board-id="page.page.board" />
    </section>

    <section v-for="note in page.notes" :key="note.id">
        <view-note :note="note" />
    </section>
    
    <section>
        <edit-page :page="page.page" />
    </section>

</article>

</template>
<script lang="ts">

export default {
    name: 'ViewPage',
    components: {
        ViewNote,
        EditPage,
        AddNote,
    },
}

</script>