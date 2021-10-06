<script lang="ts" setup>

import { computed } from 'vue'

const props = defineProps({
    note:Object,
})

</script>
<template>
    
<card bg="primary" hover>

    <template #header>
        <co-tag v-for="tag in note.tags" :key="tag.id" :label="tag.name" :tag="tag" />
        <strong class="block font-medium mt-1">{{ note.name }}</strong>
    </template>

    <p v-if="note.content" class="my-0 py-0 mb-4 text-scale-text-500 readme">
        {{ note.content }}
    </p>
    
</card>

</template>
<script lang="ts">

export default {
    name: 'note-readme',
}

</script>
<style>

.readme {
    white-space: pre-line;
}

</style>