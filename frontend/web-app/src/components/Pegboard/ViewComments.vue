<script lang="ts" setup>

import Card from '../Elements/Card.vue'
import Tag from '../Elements/Tag.vue'
import Expandable from '../Elements/Expandable.vue'
import ViewComment from './ViewComment.vue'
import AddComment from './Forms/Add/AddComment.vue'

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