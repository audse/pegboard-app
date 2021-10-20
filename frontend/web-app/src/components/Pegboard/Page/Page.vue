<script lang="ts" setup>

import { computed, ref } from 'vue'
import draggable from 'vuedraggable'

import { Board, Page } from '@/types'
import { PageModal, Checklist, Note, AddNote, Comments } from '@/components'

const props = defineProps<{
    board?:Board,
    page:Page,
}>()

const showEditModal = ref(false)

</script>
<template>

<section>

    <toolbar no-col>
        <span class="pl-2 mb-2">
            <h3 class="text-base tracking-wide">{{ page.name }}</h3>
            <h4 class="font-normal text-base text-scale-text-500">{{ page.description }}</h4>
        </span>
        <template #right>
            <co-button @click="showEditModal=!showEditModal" icon="options" subtle color="scale-text-500"></co-button>
        </template>
    </toolbar>

    <section v-for="checklist in page.checklists" :key="checklist.id" class="mx-2 mt-2">
        <checklist :checklist="checklist" />
    </section>

    <draggable v-model="page.notes" :group="`${page.id}-notes`" item-key="id">
        <template #item="{ element }">
            <article class="cursor-pointer">
                <note :note="element" />
            </article>
        </template>
    </draggable>
    
    <add-note :page="page" :display="board?.default_note_display" class="pb-8" />

    <page-modal :show="showEditModal" @hide="showEditModal=false" :page="page" />

</section>

</template>
<script lang="ts">

export default {
    name: 'page',
}

</script>