<script lang="ts" setup>

import { Comment } from '@/components'

const props = defineProps({
    comments:Array,
    boardId:Number,
    pageId:Number,
    noteId:Number,
})

</script>
<template>

<comment v-for="comment in comments" :comment="comment" :key="comment.id" />

</template>
<script lang="ts">

export default {
    name: 'comments'
}

</script>