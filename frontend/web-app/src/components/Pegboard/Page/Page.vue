<script lang="ts" setup>

import { ref } from 'vue'

import { EditPage, Note, AddNote, Comments } from '@/components'

const props = defineProps({
    page: Object,
})

const showEditModal = ref(false)

</script>
<template>

<section>

    <toolbar>
        <span class="pl-2">
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
    
    <add-note :page-id="page.id" class="pb-8" />

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