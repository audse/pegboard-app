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

    <span class="flex items-center px-2">
        <span class="flex-grow">
            <h3 class="pt-3 text-base tracking-wide">{{ page.name }}</h3>
            <h4 class="font-normal text-base text-scale-text-500">{{ page.description }}</h4>
        </span>
        <co-button @click="showEditModal=!showEditModal" icon="options" subtle color="scale-text-500"></co-button>

        <modal :show="showEditModal" @hide="showEditModal=false">
            <edit-page :page="page" @save="showEditModal=false" />
        </modal>
    </span>

    <!-- <view-comments :page-id="page.id" :comments="page.comments" /> -->

    <section v-for="note in page.notes" :key="note.id">
        <note :note="note" />
    </section>
    
    <add-note :page-id="page.id" class="pb-8" />

</section>

</template>
<script lang="ts">

export default {
    name: 'ViewPage',
}

</script>