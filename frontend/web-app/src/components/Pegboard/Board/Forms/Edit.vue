<script lang="ts" setup>

import { ref } from 'vue'
// import { useRouter } from 'vue-router'

import { Board } from '@/types'
import { BoardService } from '@/services'

const props = defineProps<{
    board:Board,
}>()

// const router = useRouter()

const editBoardForm = ref({...props.board})

const displayChoices = [
    { value: 'n', key: 'Note' },
    { value: 'h', key: 'Heading' },
    // { value: 'i', key: 'Image' },
    { value: 'c', key: 'Checkbox' },
    // { value: 'a', key: 'Assignee' },
    { value: 'r', key: 'Readme' },
    { value: 's', key: 'Small' },
    { value: 'l', key: 'Checklist' },
    // { value: 'd', key: 'Date' },
    // { value: 'o', key: 'Countdown' },
    { value: 't', key: 'Discussion' },
    
]

const editBoard = async (boardId:number, data:object) => {
    await BoardService.update(boardId, data)
}

// const archiveBoard = async(boardId:number) => {
//     await BoardService.archive(boardId)
//     router.push('/folders')
// }

</script>
<template>

<section>
    <h2 class="flex items-center my-4">
        <span class="block md:w-20 text-scale-text-500">Edit</span>
        <span class="block pl-4">{{ board.name }}</span>
    </h2>

    <form @submit.prevent="editBoard(board.id, editBoardForm)" v-if="editBoardForm.name!==undefined">

        <form-text-field v-model="editBoardForm.name" name="name" label="Name" required />
        <form-textarea-field v-model="editBoardForm.description" name="description" label="Description" />

        <section class="pt-4 flex flex-col md:flex-row md:items-center">
            <label for="display" class="flex-none w-20 my-1 md:my-0">Display</label>
            <div class="select-control">
                <select v-model="editBoardForm.default_note_display" name="display" class="bg-scale-text-100">
                    <option v-for="choice of displayChoices" :key="choice.value" :value="choice.value">
                        {{ choice.key }}
                    </option>
                </select>
            </div>
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