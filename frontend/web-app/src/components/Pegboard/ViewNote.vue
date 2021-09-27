<script lang="ts" setup>

import Card from './../Elements/Card.vue'
import EditNote from './Forms/Edit/EditNote.vue'

const props = defineProps({
    note:Object,
})

</script>
<template>

<card>

    <template #header>
        {{ note.name }}
    </template>

    <p>{{ note.description }}</p>

    <!-- <template #footer> -->
        <!-- <edit-note :note="note" /> -->
    <!-- </template> -->

</card>

</template>
<script lang="ts">

export default {
    name: 'ViewNote'
}

</script>
