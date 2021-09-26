<script lang="ts" setup>

import { reactive } from 'vue'

import PageService from './../../../../services/page.service'

const props = defineProps({
    boardId: Number,
})

interface pageForm {
    name:string,
    board:number|undefined
}

let addPageForm:pageForm = reactive({
    name: '',
    board: props.boardId || undefined
})

const addPage = async (boardId: string, data:pageForm) => {
    await PageService.create(data)
}
</script>
<template>
    
<form @submit.prevent="addPage(addPageForm, folder.id)">
    <label for="name">Page Name</label>
    <input v-model="addPageForm.name" name="name" type="text" />
    <button type="submit">Add Page</button>
</form>

</template>
<script lang="ts">

export default {
    name: 'AddPage'
}

</script>