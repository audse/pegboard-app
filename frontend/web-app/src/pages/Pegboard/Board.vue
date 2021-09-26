
<script lang="ts" setup>

import ViewPage from '../../components/Pegboard/ViewPage.vue'
import EditBoard from '../../components/Pegboard/Edit/EditBoard.vue'

import BoardService from './../../services/board.service'

import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const id = route.params.id.toString()

let board:any = ref({})

const refreshBoard = async (boardId:string) => {
    BoardService.retrieveBoardAndChildren(boardId).then( (response:any) => {
        board.value = response.data
    })
}

onMounted( () => {
    refreshBoard(id)
})

</script>
<template>

<article v-if="board?.board">

    <h1>{{ board.board.name }}</h1>
    <h2>{{ board.board.description }}</h2>

    <section>
        <!-- <form @submit.prevent="addPage(addPageForm, board.id)">
            <label for="name">Page Name</label>
            <input v-model="addPageForm.name" name="name" type="text" />
            <button type="submit">Add Page</button>
        </form> -->
    </section>

    <section v-for="page in board.pages" :key="page.id" class="flex">
        <view-page :page="page" />
    </section>

    <edit-board :board="board.board" />

</article>

</template>
