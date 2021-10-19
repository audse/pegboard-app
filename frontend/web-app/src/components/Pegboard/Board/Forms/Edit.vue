<script lang="ts" setup>

import { ref } from 'vue'
import { useRouter } from 'vue-router'

import { Board } from '@/types'
import { BoardService } from '@/services'

const props = defineProps<{
    board:Board,
}>()

const router = useRouter()

const editBoardForm = ref({
    name: props.board.name,
    description: props.board.description
})

const editBoard = async (boardId:number, data:object) => {
    await BoardService.update(boardId, data)
}

const archiveBoard = async(boardId:number) => {
    await BoardService.archive(boardId)
    router.push('/folders')
}

</script>
<template>

<section>
    <h2 class="flex items-center my-4">
        <span class="block md:w-20 text-scale-text-500">Edit</span>
        <span class="block pl-4">{{ board.name }}</span>
    </h2>

    <form @submit.prevent="editBoard(board.id, editBoardForm)">

        <section class="pt-2 flex flex-col md:flex-row md:items-center">
            <label for="name" class="flex-none w-20">
                Name
                <small class="text text-danger">Required.</small>
            </label>
            <input v-model="editBoardForm.name" name="name" type="text" />
        </section>

        <section class="pt-2 flex flex-col md:flex-row md:items-center">
            <label for="description" class="flex-none w-20">Description</label>
            <textarea v-model="editBoardForm.description" name="description"></textarea>
        </section>

        <section class="pt-2">
            <co-button type="submit" @click="this.$emit('save')" light color="emphasis">Save Edit</co-button>
        </section>

        <section class="pt-4">
            <co-button @click.prevent="archiveBoard(board.id);this.$emit('save')" subtle color="scale-text-500">Archive</co-button>
        </section>
    </form>

</section>

</template>
<script lang="ts">

export default {
    name: 'edit-board',
}

</script>