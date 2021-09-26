<script lang="ts" setup>
import Card from './../Elements/Card.vue'
import EditNote from './Edit/EditNote.vue'

const props = defineProps({
    note:Object,
})

</script>
<template>

<card>

{{ note.name }}

<edit-note :note="note" />

</card>

</template>
