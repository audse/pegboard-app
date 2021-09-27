<script lang="ts" setup>

import Card from '../Elements/Card.vue'
import ViewNote from './ViewNote.vue'
import EditPage from './Forms/Edit/EditPage.vue'
import AddNote from './Forms/Add/AddNote.vue'

const props = defineProps({
    page: Object,
})

</script>
<template>

<card no-bg>

    <template #header>
        <h2>
            {{ page.page.name }}
            <br />
            <small>{{ page.page.description }}</small>
        </h2>
    </template>

    <section v-for="note in page.notes" :key="note.id">
        <view-note :note="note" />
    </section>
    
    <template #footer>
        <!-- <edit-page :page="page.page" /> -->
        <add-note :page-id="page.page.id" :board-id="page.page.board" />
    </template>

</card>

</template>
<script lang="ts">

export default {
    name: 'ViewPage',
}

</script>