<script lang="ts" setup>

import { reactive } from 'vue'

import { Board, Page, Note } from '@/types'
import { CommentService } from '@/services'

const props = defineProps<{
    board?:Board,
    page?:Page,
    note?:Note,
}>()

const addCommentForm = reactive({
    content: '',
    board: props.board?.id,
    page: props.page?.id,
    note: props.note?.id,
})

const addComment = async (data:object) => {
    await CommentService.create(data)
    addCommentForm.content = ''
}

</script>
<template>

<form @submit.prevent="addComment(addCommentForm)" class="flex items-center">
    <input v-model="addCommentForm.content" name="name" type="text" placeholder="Comment" class="dark" />
    <co-button type="submit" subtle icon="chevron-double-right" class="ml-1" color="emphasis"></co-button>
</form>

</template>
<script lang="ts">

export default {
    name: 'add-comment'
}

</script>