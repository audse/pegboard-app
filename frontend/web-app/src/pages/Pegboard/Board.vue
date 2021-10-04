<script lang="ts" setup>

import { computed, onBeforeUnmount, ref, watch } from 'vue'
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'

import { EditBoard, Page, AddPage, Note, AddNote, } from '@/components'

const store = useStore()
const route = useRoute()
const router = useRouter()

let id = route.params.id
let url = route.params.url

const board = computed( () => store.state.boards.current )

const showEditModal = ref(false)
const showAddPageForm = ref(false)

let connectionUrl = `ws://localhost:8000/ws/api/boards/${id}/${url}`
let connection = new WebSocket(connectionUrl)

const openConnection = () => {
    connection.send(JSON.stringify({
        action: 'retrieve'
    }))
}

const getConnectionMssage =  (event:{data:string}) => {
    const data:{action:string,response:object} = JSON.parse(event.data)
    if (data.action === 'retrieve') {
        store.commit('boards/setCurrent', data.response)
    }
}

connection.onopen = () => openConnection()
connection.onmessage = (connectionEvent) => getConnectionMssage(connectionEvent)

watch(route, () => {
    console.log(route.path, route.params)

    id = route.params.id
    url = route.params.url
    connectionUrl = `ws://localhost:8000/ws/api/boards/${id}/${url}`

    connection.close()
    connection = new WebSocket(connectionUrl)
    
    connection.onopen = () => openConnection()
    connection.onmessage = (connectionEvent) => getConnectionMssage(connectionEvent)

})

onBeforeUnmount( () => {
    connection.close()
    store.commit('boards/setCurrent', {})
})

</script>
<template>

<page-layout v-if="board">
    <template #header>

        <toolbar>

            <h1 class="pb-1">
                {{ board.name }}
                <h2 class="font-light text-xl text-scale-text-700">
                    {{ board.description }}
                </h2>
            </h1>

            <template #right>
                <co-button @click="showEditModal=!showEditModal" subtle color="scale-text-500" class="flex-none px-4 py-4 ml-4">
                    <i class="gg-options icon-lg"></i>
                </co-button>
            </template>

        </toolbar>

        <toolbar class="mt-4" wrap>
            <router-link :to="{ name: 'Board', params: { id: id, url: url } }" v-slot="{ isActive }">
                <co-button :light="isActive" :subtle="!isActive" :color="isActive?'emphasis':'scale-text-500'">Kanban</co-button>
            </router-link>

            <router-link to="/" v-slot="{ isActive }">
                <co-button :light="isActive" :subtle="!isActive" :color="isActive?'emphasis':'scale-text-500'">Calendar</co-button>
            </router-link>

            <template #right>
                <co-button light color="alert" icon="user" class="hidden lg:block"></co-button>
                <co-button @click="showAddPageForm=!showAddPageForm" color="emphasis" class="flex items-center pl-2 my-2 lg:my-0">
                    <transition name="scale" mode="out-in">
                        <i v-if="!showAddPageForm" class="gg-math-plus block flex-none mr-2"></i>
                        <i v-else class="gg-math-minus block flex-none mr-2"></i>
                    </transition>

                    Add Page
                </co-button>
            </template>
        </toolbar>

        <section>
            <expandable :to-show="showAddPageForm">
                <add-page :board-id="board.id" class="mt-6 p-4 rounded-2xl bg-scale-secondary-700" />
            </expandable>
        </section>

    </template>

    <section class="flex flex-wrap">
        <page v-for="page in board.pages" :key="page.id" :page="page" class="flex-none w-full md:w-1/2 lg:w-4/12" />
    </section>

    <modal :show="showEditModal" @hide="showEditModal=false">
        <edit-board :board="board" :tags="board.tags" @save="showEditModal=false" />
    </modal>

    <article v-if="board?.notes?.length > 0" class="mt-8">
        <section class="flex items-center pl-2">
            <add-note :board-id="board.id" class="w-4/12" />
        </section>
        <section class="flex flex-wrap">
            <note v-for="note in board.notes" :key="note.id" :note="note" />
        </section>
    </article>

</page-layout>
<page-layout v-else></page-layout>

</template>
<style scoped>

.toolbar button {
    @apply mr-2;
}

.toolbar-right button {
    @apply ml-2 mr-0;
}

</style>
