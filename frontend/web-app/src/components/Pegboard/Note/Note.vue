<script lang="ts" setup>

import { NoteDefault, EditNote, NoteModal } from '@/components'

import { ref } from 'vue'

const props = defineProps({
    note:Object,
})

const showEditModal = ref(false)

</script>
<template>

<note-default v-if="note?.display=='n'" :note="note" @click="showEditModal=true" />
<note-modal :note="note" :show="showEditModal" @hide="showEditModal=false" />

</template>
<script lang="ts">

export default {
    name: 'note'
}

</script>
