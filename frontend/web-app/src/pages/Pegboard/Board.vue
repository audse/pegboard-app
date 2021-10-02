<script lang="ts" setup>

import Modal from './../../components/Elements/Modal.vue'
import ViewPage from '../../components/Pegboard/ViewPage.vue'
import ViewNote from '../../components/Pegboard/ViewNote.vue'
import EditBoard from '../../components/Pegboard/Forms/Edit/EditBoard.vue'
import AddPage from '../../components/Pegboard/Forms/Add/AddPage.vue'
import AddNote from '../../components/Pegboard/Forms/Add/AddNote.vue'

import { computed, onBeforeUnmount, ref, reactive } from 'vue'
import { useStore } from 'vuex'
import { useRoute } from 'vue-router'

const store = useStore()
const route = useRoute()

const id = route.params.id.toString()
const url = route.params.url

const board = computed( () => store.state.boards.current )

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
        store.commit('boards/setCurrent', data.response)
    }
}

onBeforeUnmount( () => {
    connection.close()
    store.commit('boards/setCurrent', {})
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
    <add-page :board-id="board.id" />

    <section class="flex flex-wrap">
        <view-page v-for="page in board.pages" :key="page.id" :page="page" class="flex-none w-4/12" />
    </section>

    <modal :show="showEditModal" @hide="showEditModal=false">
        <edit-board :board="board" :tags="board.tags" @save="showEditModal=false" />
    </modal>

    <article v-if="board.notes?.length > 0" class="mt-8">
        <section class="flex items-center pl-2">
            <add-note :board-id="board.id" class="w-4/12" />
        </section>
        <section class="flex items-center flex-wrap">
            <view-note v-for="note in board.notes" :key="note.id" :note="note" class="box-border w-4/12 flex-none" />
        </section>
    </article>

</article>

</template>
