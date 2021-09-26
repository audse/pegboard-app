<script lang="ts" setup>

import { reactive } from 'vue'

import BoardService from './../../../../services/board.service'

const props = defineProps({
    board: Object,
})

interface boardForm {
    name:string,
}

let editBoardForm:boardForm = reactive({
    name: props.board.name
})

const editBoard = async (boardId: string, data:boardForm) => {
    await BoardService.update(boardId, data)
}

</script>
<template>
    
<section class="pt-6">
    <h3>Edit {{ board.name }}</h3>
    <form @submit.prevent="editBoard(board.id, editBoardForm)">
        <label for="name">Board Name</label>
        <input v-model="editBoardForm.name" name="name" type="text" />
        <button type="submit" class="secondary">Save Edit</button>
    </form>
</section>

</template>
<script lang="ts">

export default {
    name: 'EditBoard',
}

</script>