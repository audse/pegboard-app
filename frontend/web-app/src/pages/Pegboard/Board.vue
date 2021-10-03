<script lang="ts" setup>

import Page from './../../layouts/Page.layout.vue'
import Modal from './../../components/Elements/Modal.vue'
import Toolbar from './../../components/Elements/Toolbar.vue'
import CoButton from './../../components/Elements/Button.vue'
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

<page v-if="board">
    <template #header>

        <h1 class="pb-1">
            {{ board.name }}
        </h1>
        <h2 class="flex font-light">
            <span class="flex-grow">{{ board.description }}</span>
            <button @click="showEditModal=!showEditModal" class="secondary">Edit</button>
        </h2>

        <toolbar class="mt-4">
            <router-link :to="{ name: 'Board', params: { id: board.id, url: board.url } }" v-slot="{ isActive }">
                <co-button :light="isActive" :subtle="!isActive" :color="isActive?'scale-text-700':'scale-text-500'">Kanban</co-button>
            </router-link>

            <router-link :to="{ name: 'Board', params: { id: 0, url: board.url } }" v-slot="{ isActive }">
                <co-button :light="isActive" :subtle="!isActive" :color="isActive?'scale-text-700':'scale-text-500'">Calendar</co-button>
            </router-link>

            <template #right>
                <co-button light color="emphasis">+ Add Page</co-button>
            </template>
        </toolbar>

        <!-- <add-page :board-id="board.id" /> -->

    </template>

    <section class="flex flex-wrap">
        <view-page v-for="page in board.pages" :key="page.id" :page="page" class="flex-none w-4/12" />
    </section>

    <modal :show="showEditModal" @hide="showEditModal=false">
        <edit-board :board="board" :tags="board.tags" @save="showEditModal=false" />
    </modal>

    <article v-if="board?.notes?.length > 0" class="mt-8">
        <section class="flex items-center pl-2">
            <add-note :board-id="board.id" class="w-4/12" />
        </section>
        <section class="flex items-center flex-wrap">
            <view-note v-for="note in board.notes" :key="note.id" :note="note" class="box-border w-4/12 flex-none" />
        </section>
    </article>

</page>

</template>
<style scoped>

.toolbar button {
    @apply mr-2;
}

.toolbar-right button {
    @apply ml-2 mr-0;
}

</style>
