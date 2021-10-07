<script lang="ts" setup>

import { reactive } from 'vue'

import { Board } from '@/types'
import { PageService } from '@/services'

const props = defineProps<{
    board:Board,
}>()

const addPageForm = reactive({
    name: '',
    description: '',
    board: props.board.id || null,
})

const addPage = async (data:{name:string,board:number|undefined}) => {
    data.board = props.board.id
    await PageService.create(data)
    addPageForm.name = ''
}
</script>
<template>

<form @submit.prevent="addPage(addPageForm)">

    <section class="flex items-start flex-col md:items-center md:flex-row">
        <label for="name" class="flex-none block w-24">
            Name
            <small class="text-danger">Required.</small>
        </label>
        <input v-model="addPageForm.name" name="name" type="text" placeholder="Name" class="bg-main" />
    </section>

    <section class="mt-4 flex items-start flex-col md:items-center md:flex-row">
        <label for="description" class="flex-none block w-24">Description</label>
        <textarea v-model="addPageForm.description" name="description" type="text" placeholder="Description" class="bg-main" />
    </section>

    <co-button type="submit" light color="emphasis">+ Add Page</co-button>
</form>

</template>
<script lang="ts">

export default {
    name: 'AddPage'
}

</script>