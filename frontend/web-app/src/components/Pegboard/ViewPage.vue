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

<card class="bg-gray-800">

    <template #header>
        <strong>{{ page.page.name }}</strong>
        {{ page.page.description }}

        <section>
            <add-note :page-id="page.page.id" :board-id="page.page.board" />
        </section>
    </template>

    <section v-for="note in page.notes" :key="note.id">
        <view-note :note="note" />
    </section>
    
    <template #footer>
        <edit-page :page="page.page" />
    </template>

</card>

</template>
<script lang="ts">

export default {
    name: 'ViewPage',
}

</script>