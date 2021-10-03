<script lang="ts" setup>

import CoButton from './../../../Elements/Button.vue'
import Card from './../../../Elements/Card.vue'

import { reactive } from 'vue'

import PageService from './../../../../services/page.service'

const props = defineProps({
    boardId: Number,
})

const addPageForm = reactive({
    name: '',
    description: '',
    board: props.boardId || null,
})

const addPage = async (data:{name:string,board:number}) => {
    data.board = props.boardId
    await PageService.create(data)
    addPageForm.name = ''
}
</script>
<template>

<form @submit.prevent="addPage(addPageForm)">

    <section class="flex items-center">
        <label for="name" class="flex-none block w-24">Name</label>
        <input v-model="addPageForm.name" name="name" type="text" placeholder="Name" class="bg-scale-secondary-900" />
    </section>

    <section class="flex items-center">
        <label for="description" class="flex-none block w-24">Description</label>
        <textarea v-model="addPageForm.description" name="description" type="text" placeholder="Description" class="bg-scale-secondary-900" />
    </section>

    <co-button type="submit" light color="emphasis">+ Add Page</co-button>
</form>

</template>
<script lang="ts">

export default {
    name: 'AddPage'
}

</script>