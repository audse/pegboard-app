<script lang="ts" setup>

import { Page, Note, AddNote } from '@/components'
import { Board } from '@/types'

const props = defineProps<{
    board:Board,
}>()

</script>
<template>

<!-- All Pages -->
<section class="flex overflow-x-scroll h-auto no-scrollbar page-padding">
    <page v-for="page in board.pages" :key="page.id" :page="page" :board="board" class="flex-none w-11/12 md:w-5/12 lg:w-4/12" />
</section>

<!-- Unsorted Notes -->
<article class="mt-8 page-padding">
    <section class="flex flex-col md:flex-row md:items-center pl-2 py-4">
        <h2 class="text-scale-text-500 px-4">Unsorted Notes</h2>
        <add-note :board="board" class="md:w-4/12" />
    </section>
    <section class="flex flex-wrap pl-2" v-if="board?.notes?.length > 0">
        <div v-for="note in board.notes" :key="note.id" class="flex-none w-11/12 md:w-5/12 lg:w-4/12">
            <note :note="note" />
        </div>
    </section>
</article>  

</template>
<script lang="ts">
export default {
    name: 'Kanban'
}
</script>