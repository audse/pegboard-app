<script lang="ts" setup>

import Card from '../Elements/Card.vue'
import Modal from '../Elements/Modal.vue'
import ViewNote from './ViewNote.vue'
import EditPage from './Forms/Edit/EditPage.vue'
import AddNote from './Forms/Add/AddNote.vue'

import { ref } from 'vue'

const props = defineProps({
    page: Object,
})

const showEditModal = ref(false)

</script>
<template>

<card no-bg>

    <template #header>
        <span class="flex items-center">
            <h2 class="flex-grow">
                {{ page.name }}
                <br />
                <small>{{ page.description }}</small>
            </h2>
            <button @click="showEditModal=!showEditModal" class="secondary">Edit</button>

            <modal :show="showEditModal" @hide="showEditModal=false">
                <edit-page :page="page" @save="showEditModal=false" />
            </modal>
        </span>
    </template>

    <section v-for="note in page.notes" :key="note.id">
        <view-note :note="note" />
    </section>
    
    <template #footer>
        <add-note :page-id="page.id" />
    </template>

</card>

</template>
<script lang="ts">

export default {
    name: 'ViewPage',
}

</script>