<script lang="ts" setup>

import Card from './../Elements/Card.vue'
import Tag from './../Elements/Tag.vue'
import Modal from './../Elements/Modal.vue'
import EditNote from './Forms/Edit/EditNote.vue'
import ViewChecklist from './ViewChecklist.vue'

import { ref } from 'vue'

const props = defineProps({
    note:Object,
})

const showEditModal = ref(false)

</script>
<template>

<card>
    
    <tag v-for="tag in note.tags" :key="tag.id" :label="tag.name" :color="tag.color.color" />

    <section class="flex items-center">
        <strong class="flex-grow">{{ note.name }}</strong>
        <button class="secondary" @click="showEditModal=!showEditModal">Edit</button>
    </section>

    <section v-if="note.checklists.length > 0" class="pt-2 mt-2 border-gray-500 border-t">
        <!-- {{ note.checklists }} -->
        <view-checklist v-for="checklist in note.checklists" :checklist="checklist" :key="checklist.id" />
    </section>

    <modal :show="showEditModal" @hide="showEditModal=false">
        <edit-note :note="note" @save="showEditModal=false" />
    </modal>


</card>

</template>
<script lang="ts">

export default {
    name: 'ViewNote'
}

</script>
