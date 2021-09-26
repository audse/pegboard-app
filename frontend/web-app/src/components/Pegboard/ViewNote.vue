<script lang="ts" setup>

import Card from './../Elements/Card.vue'
import EditNote from './Forms/Edit/EditNote.vue'

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
<script lang="ts">

export default {
    name: 'ViewNote'
}

</script>
