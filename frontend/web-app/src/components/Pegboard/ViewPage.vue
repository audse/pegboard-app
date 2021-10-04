<script lang="ts" setup>

import Card from '../Elements/Card.vue'
import Modal from '../Elements/Modal.vue'
import ViewNote from './ViewNote.vue'
import ViewComments from './ViewComments.vue'
import EditPage from './Forms/Edit/EditPage.vue'
import AddNote from './Forms/Add/AddNote.vue'

import { ref } from 'vue'

const props = defineProps({
    page: Object,
})

const showEditModal = ref(false)

</script>
<template>

<section>

    <span class="flex items-center px-2">
        <span class="flex-grow">
            <h3 class="pt-3 text-base tracking-wide">{{ page.name }}</h3>
            <h4 class="font-normal text-base text-scale-text-500">{{ page.description }}</h4>
        </span>
        <co-button @click="showEditModal=!showEditModal" icon="options" subtle color="scale-text-500"></co-button>

        <modal :show="showEditModal" @hide="showEditModal=false">
            <edit-page :page="page" @save="showEditModal=false" />
        </modal>
    </span>

    <!-- <view-comments :page-id="page.id" :comments="page.comments" /> -->

    <section v-for="note in page.notes" :key="note.id">
        <view-note :note="note" />
    </section>
    
    <add-note :page-id="page.id" class="pb-8" />

</section>

</template>
<script lang="ts">

export default {
    name: 'ViewPage',
}

</script>