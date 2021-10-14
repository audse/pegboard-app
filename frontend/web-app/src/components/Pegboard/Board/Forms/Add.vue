<script lang="ts" setup>

import { reactive } from 'vue'

import { Folder } from '@/types'
import { BoardService } from '@/services'

const props = defineProps<{
    folder?:Folder,
}>()

const addBoardForm = reactive({
    name: '',
    folder: props.folder?.id
})

const addBoard = async (data:object) => {
    if (props.folder != undefined) {
        await BoardService.createInFolder(data, props.folder)
    } else {
        await BoardService.create(data)
    }
    
    addBoardForm.name = ''
}

</script>
<template>

<form @submit.prevent="addBoard(addBoardForm)" class="flex items-center">
    <label for="name" class="flex-none text-scale-text-700">Add Board</label>
    <input v-model="addBoardForm.name" name="name" type="text" placeholder="Board Name" class="bg-main" />
    <co-button type="submit" class="flex-none ml-4" icon="math-plus" light color="emphasis">Add Board</co-button>
</form>
    
</template>
<script lang="ts">

export default {
    name: 'AddBoard'
}

</script>