<script lang="ts" setup>

import Tag from './../../../Elements/Tag.vue'
import Expandable from './../../../Elements/Expandable.vue'
import AddTag from '../Add/AddTag.vue'

import { reactive } from 'vue'

import BoardService from './../../../../services/board.service'

const props = defineProps({
    board: Object,
    tags: Array,
})

const editBoardForm = reactive({...props.board})

const editBoard = async (boardId: string, data:object) => {
    await BoardService.update(boardId, data)
}

</script>
<template>

<section>
    <h3>Edit {{ board.name }}</h3>

    <form @submit.prevent="editBoard(board.id, editBoardForm)">

        <section class="pt-4 flex items-center">
            <label for="name" class="flex-none">Name</label>
            <input v-model="editBoardForm.name" name="name" type="text" />
        </section>

        <section class="pt-4 flex items-center">
            <label for="description" class="flex-none">Description</label>
            <textarea v-model="editBoardForm.description" name="description"></textarea>
        </section>

        <section class="pt-4">
            <label for="tags">Tags</label>
            
            <section class="pt-4">
                <tag v-for="tag in tags" :key="tag.id" :label="tag.name" :color="tag.color.color" />
            </section>

            <expandable class="pt-4">
                <template #label>Add Tag</template>
                <add-tag :boardId="board.id" />
            </expandable>
        </section>

        <section class="pt-8">
            <button type="submit" @click="this.$emit('save')" class="secondary">Save Edit</button>
        </section>
    </form>

</section>

</template>
<script lang="ts">

export default {
    name: 'EditBoard',
}

</script>