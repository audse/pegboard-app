<script lang="ts" setup>

import { ref } from 'vue'

import { Board, Page } from '@/types'
import { EditPage, Note, AddNote, Comments } from '@/components'

const props = defineProps<{
    board?:Board,
    page:Page,
}>()

const showEditModal = ref(false)

</script>
<template>

<section>

    <toolbar>
        <span class="pl-2 mb-2">
            <h3 class="text-base tracking-wide">{{ page.name }}</h3>
            <h4 class="font-normal text-base text-scale-text-500">{{ page.description }}</h4>
        </span>
        <template #right>
            <co-button @click="showEditModal=!showEditModal" icon="options" subtle color="scale-text-500"></co-button>
        </template>
    </toolbar>

    <section v-for="note in page.notes" :key="note.id">
        <note :note="note" />
    </section>
    
    <add-note :page="page" :display="board?.default_note_display" class="pb-8" />

    <modal :show="showEditModal" @hide="showEditModal=false">
        <edit-page :page="page" @save="showEditModal=false" />
    </modal>

</section>

</template>
<script lang="ts">

export default {
    name: 'page',
}

</script>