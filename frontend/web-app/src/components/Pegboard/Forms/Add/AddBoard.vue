<script lang="ts" setup>

import { reactive } from 'vue'

import BoardService from './../../../../services/board.service'

const props = defineProps({
    folderId: Number,
})

interface boardForm {
    name:string,
    folder:number|undefined
}

let addBoardForm:boardForm = reactive({
    name: '',
    folder: props.folderId || undefined
})

const addBoard = async (boardId: string, data:boardForm) => {
    await BoardService.create(data)
}

</script>
<template>

<form @submit.prevent="addBoard(addBoardForm, folder.id)">
    <label for="name">Board Name</label>
    <input v-model="addBoardForm.name" name="name" type="text" />
    <button type="submit">Add Board</button>
</form>
    
</template>
<script lang="ts">

export default {
    name: 'AddBoard'
}

</script>