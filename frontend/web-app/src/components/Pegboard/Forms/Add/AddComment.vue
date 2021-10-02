<script lang="ts" setup>

import { reactive } from 'vue'

import CommentService from './../../../../services/comment.service'

// const props = defineProps({
//     boardId: Number,
// })

// let addPageForm = reactive({
//     name: '',
//     board: props.boardId || undefined
// })

// const addPage = async (data:object) => {
//     await PageService.create(data)
// }
</script>
<template>

<card no-bg>
<!-- 
    <h2>Add Page</h2>

    <form @submit.prevent="addPage(addPageForm)">
        <label for="name">Page Name</label> 
        <input v-model="addPageForm.name" name="name" type="text" placeholder="Name" />
        <button type="submit">Add Page</button>
    </form> -->
</card>

</template>
<script lang="ts">

export default {
    name: 'AddPage'
}

</script>