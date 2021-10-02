<script lang="ts" setup>

import { reactive } from 'vue'

import BoardService from './../../../../services/board.service'

const props = defineProps({
    folderId: Number,
})

const addBoardForm = reactive({
    name: '',
    folder: props.folderId || undefined
})

const addBoard = async (boardId: string, data:object) => {
    await BoardService.create(data)
    addBoardForm.name = ''
}

</script>
<template>

<form @submit.prevent="addBoard(addBoardForm, folder.id)" class="flex items-center">
    <label for="name" class="flex-none">Board Name</label>
    <input v-model="addBoardForm.name" name="name" type="text" placeholder="Board Name" />
    <button type="submit" class="flex-none">Add Board</button>
</form>
    
</template>
<script lang="ts">

export default {
    name: 'AddBoard'
}

</script>