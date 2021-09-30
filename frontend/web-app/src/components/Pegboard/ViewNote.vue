<script lang="ts" setup>

import Card from './../Elements/Card.vue'
import Tag from './../Elements/Tag.vue'
import Modal from './../Elements/Modal.vue'
import EditNote from './Forms/Edit/EditNote.vue'

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

    <modal :show="showEditModal" @hide="showEditModal=false">
        <edit-note :note="note" @save="showEditModal=false" />
    </modal>


</card>

</template>
<script lang="ts">

export default {
  components: { Modal },
    name: 'ViewNote'
}

</script>
