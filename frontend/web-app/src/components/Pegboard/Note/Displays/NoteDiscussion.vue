<script lang="ts" setup>

import { computed } from 'vue'
import { Comments, AddComment } from '@/components'
import Toolbar from '@/components/Elements/Toolbar.vue'

const props = defineProps({
    note:Object,
})

const emits = defineEmits([
    'show-modal'
])

</script>
<template>
    
<card bg="primary" hover>

    <template #header>
        <toolbar @click="$emit('show-modal')">
            <co-tag v-for="tag in note.tags" :key="tag.id" :label="tag.name" :color="tag.color.color" />
            <strong class="block font-medium mt-1">{{ note.name }}</strong>
            <template #right>
                <co-tag v-if="note.comments.length>0" :label="note.comments.length.toString()" var-color="alert" />
            </template>
        </toolbar>
    </template>

    <section class="max-h-60 overflow-y-scroll">
        <comments :comments="note.comments" :noteId="note.id" />
    </section>
    <add-comment :note-id="noteId" class="pb-2" />

</card>

</template>
<script lang="ts">

export default {
    components: { Toolbar },
    name: 'note-discussion',
}

</script>