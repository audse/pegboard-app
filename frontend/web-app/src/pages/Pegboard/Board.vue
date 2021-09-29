
<script lang="ts" setup>

import Modal from './../../components/Elements/Modal.vue'
import ViewPage from '../../components/Pegboard/ViewPage.vue'
import EditBoard from '../../components/Pegboard/Forms/Edit/EditBoard.vue'
import AddPage from '../../components/Pegboard/Forms/Add/AddPage.vue'

import BoardService from './../../services/board.service'

import { onMounted, computed, ref } from 'vue'
import { useStore } from 'vuex'
import { useRoute } from 'vue-router'

const store = useStore()
const route = useRoute()

const id = route.params.id.toString()

const board = computed( () => store.state.boards.currentBoard )

const refreshBoard = async (boardId:string) => {
    await BoardService.retrieveBoardAndChildren(boardId)
}

onMounted( () => {
    refreshBoard(id)
})

const showEditModal = ref(false)

</script>
<template>

<article v-if="board?.board">

    <h1>
        {{ board.board.name }}
        <br />
        <small class="flex">
            <span class="flex-grow">{{ board.board.description }}</span>
            <button @click="showEditModal=!showEditModal" class="secondary">Edit</button>
        </small>
    </h1>
    

    <section class="flex">
        <view-page v-for="page in board.pages" :key="page.page.id" :page="page" class="w-4/12" />
        <add-page :board-id="board.board.id" class="w-4/12" />
    </section>

    <modal :show="showEditModal" @hide="showEditModal=false">
        <edit-board :board="board.board" />
    </modal>

</article>

</template>
