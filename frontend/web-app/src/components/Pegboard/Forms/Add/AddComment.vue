<script lang="ts" setup>

import { reactive } from 'vue'

import CommentService from './../../../../services/comment.service'

const props = defineProps({
    boardId:Number,
    pageId:Number,
    noteId:Number,
})

const addCommentForm = reactive({
    content: '',
    board: props.boardId || undefined,
    page: props.pageId || undefined,
    note: props.noteId || undefined,
})

const addComment = async (data:object) => {
    await CommentService.create(data)
}

</script>
<template>

<card no-bg>

    <h2>Add Comment</h2>

    <form @submit.prevent="addComment(addCommentForm)">
        <input v-model="addCommentForm.content" name="name" type="text" placeholder="Comment..." />
        <button type="submit">+</button>
    </form>

</card>

</template>
<script lang="ts">

export default {
    name: 'AddComment'
}

</script>