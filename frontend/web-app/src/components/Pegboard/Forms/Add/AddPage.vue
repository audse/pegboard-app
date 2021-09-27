<script lang="ts" setup>

import Card from './../../../Elements/Card.vue'

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

<card no-bg>

    <h2>Add Page</h2>

    <form @submit.prevent="addPage(addPageForm, folder.id)">
        <!-- <label for="name">Page Name</label> -->
        <input v-model="addPageForm.name" name="name" type="text" placeholder="Name" />
        <button type="submit">Add Page</button>
    </form>
</card>

</template>
<script lang="ts">

export default {
    name: 'AddPage'
}

</script>