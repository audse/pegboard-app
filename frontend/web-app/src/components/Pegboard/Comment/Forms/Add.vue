<script lang="ts" setup>

import { reactive } from 'vue'

import { CommentService } from '@/services'

const props = defineProps({
    boardId:Number,
    pageId:Number,
    noteId:Number,
})

const addCommentForm = reactive({
    content: '',
    board: props.boardId || null,
    page: props.pageId || null,
    note: props.noteId || null,
})

const addComment = async (data:object) => {
    await CommentService.create(data)
    addCommentForm.content = ''
}

</script>
<template>

<form @submit.prevent="addComment(addCommentForm)" class="flex items-center">
    <input v-model="addCommentForm.content" name="name" type="text" placeholder="Comment" class="dark" />
    <button type="submit" class="secondary">Send</button>
</form>

</template>
<script lang="ts">

export default {
    name: 'AddComment'
}

</script>