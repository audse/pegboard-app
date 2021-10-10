<script lang="ts" setup>

import { computed } from 'vue'

import { Note } from '@/types'

const props = defineProps<{
    note:Note,
}>()

</script>
<template>
    
<card bg="main" hover dense>

    <template #header>
        <co-tag v-for="tag in note.tags" :key="tag.id" :label="tag.name" :tag="tag" dense />
        <strong class="font-medium">{{ note.name }}</strong>
    </template>
    
</card>

</template>
<script lang="ts">

export default {
    name: 'note-small',
}

</script>