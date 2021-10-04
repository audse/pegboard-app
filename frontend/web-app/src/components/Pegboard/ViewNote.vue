<script lang="ts" setup>

import NoteDefault from './Notes/NoteDefault.vue'
import EditNote from './Forms/Edit/EditNote.vue'

import { ref } from 'vue'

const props = defineProps({
    note:Object,
})

const showEditModal = ref(false)

</script>
<template>

<note-default v-if="note?.display=='n'" :note="note" @click="showEditModal=true" />

<modal :show="showEditModal" @hide="showEditModal=false">
    <edit-note :note="note" @save="showEditModal=false" />
</modal>

</template>
<script lang="ts">

export default {
    name: 'ViewNote'
}

</script>
