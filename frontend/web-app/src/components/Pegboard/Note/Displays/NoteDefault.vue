<script lang="ts" setup>

import { computed } from 'vue'

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
    
<card bg="main" hover>

    <template #header>
        <co-tag v-for="tag in note.tags" :key="tag.id" :label="tag.name" :tag="tag" />
        <strong class="block font-medium mt-1">{{ note.name }}</strong>
    </template>

    <p v-if="truncatedContent" class="my-0 py-0 mb-4 text-scale-text-500">
        {{ truncatedContent }}
    </p>
    
</card>

</template>
<script lang="ts">

export default {
    name: 'note-default',
}

</script>