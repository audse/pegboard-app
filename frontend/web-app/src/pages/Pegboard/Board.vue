
<script lang="ts" setup>

import Modal from './../../components/Elements/Modal.vue'
import ViewPage from '../../components/Pegboard/ViewPage.vue'
import EditBoard from '../../components/Pegboard/Forms/Edit/EditBoard.vue'
import AddPage from '../../components/Pegboard/Forms/Add/AddPage.vue'

import BoardService from './../../services/board.service'

import { computed, onBeforeUnmount, ref } from 'vue'
import { useStore } from 'vuex'
import { useRoute } from 'vue-router'

const store = useStore()
const route = useRoute()

const id = route.params.id.toString()
const url = route.params.url

const board = computed( () => store.state.boards.currentBoard )

const showEditModal = ref(false)

const connection = new WebSocket(`ws://localhost:8000/ws/api/boards/${id}/${url}`)

connection.onopen = () => {
    connection.send(JSON.stringify({
        action: 'retrieve'
    }))
}

connection.onmessage = (event:{data:string}) => {
    const data:{action:string,response:object} = JSON.parse(event.data)
    if (data.action === 'retrieve') {
        console.log(data.response)
        store.commit('boards/setCurrentBoard', data.response)
    }
}

onBeforeUnmount( () => {
    connection.close()
    store.commit('boards/setCurrentBoard', {})
})

</script>
<template>

<article v-if="board">

    <h1>
        {{ board.name }}
        <br />
        <small class="flex">
            <span class="flex-grow">{{ board.description }}</span>
            <button @click="showEditModal=!showEditModal" class="secondary">Edit</button>
        </small>
    </h1>
    

    <section class="flex">
        <view-page v-for="page in board.pages" :key="page.id" :page="page" class="w-4/12" />
        <add-page :board-id="board.id" class="w-4/12" />
    </section>

    <modal :show="showEditModal" @hide="showEditModal=false">
        <edit-board :board="board" :tags="board.tags" @save="showEditModal=false" />
    </modal>

</article>

</template>
