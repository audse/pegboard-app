<script lang="ts" setup>

import Card from './../../../Elements/Card.vue'

import { reactive } from 'vue'

import PageService from './../../../../services/page.service'

const props = defineProps({
    boardId: Number,
})

const addPageForm = reactive({
    name: '',
    board: props.boardId || null,
})

const addPage = async (data:{name:string,board:number}) => {
    data.board = props.boardId
    await PageService.create(data)
    addPageForm.name = ''
}
</script>
<template>

<form @submit.prevent="addPage(addPageForm)" class="flex items-center p-2 my-2">
    <label for="name" class="flex-none">Add Page</label>
    <input v-model="addPageForm.name" name="name" type="text" placeholder="Name" />
    <button type="submit">+</button>
</form>

</template>
<script lang="ts">

export default {
    name: 'AddPage'
}

</script>