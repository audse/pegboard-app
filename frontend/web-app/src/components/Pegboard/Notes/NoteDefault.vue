<script lang="ts" setup>

import EditNote from './../Forms/Edit/EditNote.vue'
import ViewChecklist from './../ViewChecklist.vue'
import ViewComments from './../ViewComments.vue'

import { computed, ref } from 'vue'

const props = defineProps({
    note:Object,
})

const truncatedContent = computed( () => {
    if (props.note?.content?.length > 140) {
        return `${props.note?.content.substr(0, 140)}...`
    } else return props.note?.content
})

</script>
<template>
    
<card bg="primary" hover>

    <template #header>
        <tag v-for="tag in note.tags" :key="tag.id" :label="tag.name" :color="tag.color.color" />
        <strong class="block font-semibold mt-1">{{ note.name }}</strong>
    </template>

    <p v-if="truncatedContent" class="my-0 py-0 mb-4 text-scale-text-500">
        {{ truncatedContent }}
    </p>

    <!-- <section v-if="note.checklists.length > 0" class="pt-2 mt-2 border-gray-500 border-t">
        <view-checklist v-for="checklist in note.checklists" :checklist="checklist" :key="checklist.id" />
    </section> -->

</card>

</template>
<script lang="ts">

export default {
    name: 'NoteDefault',
}

</script>