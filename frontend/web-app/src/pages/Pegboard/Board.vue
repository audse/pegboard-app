
<script lang="ts" setup>

import ViewPage from '../../components/Pegboard/ViewPage.vue'
import EditBoard from '../../components/Pegboard/Forms/Edit/EditBoard.vue'
import AddPage from '../../components/Pegboard/Forms/Add/AddPage.vue'

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

    <h1>
        {{ board.board.name }}
        <br />
        <small>{{ board.board.description }}</small>
    </h1>

    <section class="flex">
        <view-page v-for="page in board.pages" :key="page.page.id" :page="page" class="w-4/12" />
        <add-page :board-id="board.board.id" class="w-4/12" />
    </section>

    <!-- <edit-board :board="board.board" /> -->

</article>

</template>
