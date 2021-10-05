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

const showModal = (event:any) => {
    event.stopPropagation()
    if ( !event.currentTarget.className.includes('comment-form') ) {
        emits('show-modal')
    }
}

</script>
<template>
    
<card bg="primary" hover @click="showModal">

    <template #header>
        <toolbar>
            <co-tag v-for="tag in note.tags" :key="tag.id" :label="tag.name" :color="tag.color.color" />
            <strong class="block font-medium mt-1">{{ note.name }}</strong>
            <template #right>
                <co-tag v-if="note.comments.length>0" :label="note.comments.length.toString()" var-color="alert" />
            </template>
        </toolbar>
    </template>

    <comments :comments="note.comments" :note-id="note.id" />
    <add-comment :note-id="note.id" class="comment-form pb-2" @click="showModal" />

</card>

</template>
<script lang="ts">

export default {
    components: { Toolbar },
    name: 'note-discussion',
}

</script>