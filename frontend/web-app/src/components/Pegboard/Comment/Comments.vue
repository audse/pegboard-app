<script lang="ts" setup>

import { Comment, AddComment } from '@/components'

const props = defineProps({
    comments:Array,
    boardId:Number,
    pageId:Number,
    noteId:Number,
})

</script>
<template>

<card border no-bg>
    <expandable>
        <template #label>
            <small class="mr-2">Comments</small>
            <tag v-if="comments.length>0" :label="comments.length.toString()" color="aaaaff" />
        </template>
        <view-comment v-for="comment in comments" :comment="comment" :key="comment.id" />
        <add-comment :board-id="boardId" :page-id="pageId" :note-id="noteId" />
    </expandable>
</card>

</template>
<script lang="ts">

export default {
    name: 'ViewComments'
}

</script>