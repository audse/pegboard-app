<script lang="ts" setup>

import { Board } from '@/types'

const props = defineProps<{
    board:Board,
}>()

</script>
<template>
    
<!-- Notes w/ Dates -->
<span v-for="page in board.pages" :key="page.id">
    <span v-for="note in page.notes" :key="note.id">
        <span v-if="note.date_due || note.date_todo">{{ note.date_due || note.date_todo }}</span>
    </span>
</span>

<!-- Unsorted Notes w/ Dates -->
<span v-for="note in board.notes" :key="note.id">
    <span v-if="note.date_due || note.date_todo">{{ note.date_due || note.date_todo }}</span>
</span>

</template>
<script lang="ts">
export default {
    name: 'Calendar'
}
</script>